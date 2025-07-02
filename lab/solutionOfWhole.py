import os
import re
import sys
import random
import cv2
import dlib
import math
from collections import OrderedDict
import openpyxl
from scipy.spatial import distance as dist
from timeit import time
import xlwt
import pickle
import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from xgboost import XGBClassifier, Booster
import xgboost as xgb
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import LSTM
from keras.models import Sequential, load_model
from sklearn.preprocessing import MinMaxScaler

#load model first
# dlib库
print("LoadModel")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
xgb_model = pickle.load(open("./XGBModel/xgb.pickle(train97.48_test90.92_whole96.17).dat", "rb"))
lstm_model = load_model(os.path.join("LSTMModel","LSTMTest(train96.09%_test86.19%)" + ".h5"))

#变量说明
flag = True  # flag：是否成功打开摄像头
count0 = 0  #清醒状态的次数
count1 = 0  #中度疲劳的状态
count2 = 0  #重度疲劳的状态
pre_Label = []  #用于存储3s内每一帧图像的Label(疲劳状态)
MakeUp = 0  #最终的状态判定，0对应清醒、1中度疲劳对应语音及音乐、2重度疲劳对应打电话

ear = 0
mar = 0
har = 0

# 疲劳特征阈值
# EAR
EYE_AR_THRESH = 0.3   #EAR阈值
EYE_AR_CONSEC_FRAMES = 3  #如果EAR数值超过了三帧及以上我们就可以把他认定为一次闭眼
# MAR
# https://www.xjishu.com/zhuanli/55/202010338222.html(查资料的时候看到顺便加的，增加检测讲话功能->检测人有没有在打电话？)
MAR_THRESH = 0.8  #MAR阈值(打哈欠)
# PERCLOS
# 阈值参考：基于FPGA+ARM的疲劳检测系统设计与实现_王涌.caj
PERCLOS_THRESH = 0.2
HAR_THRESH = 0.3
# 计数器
PERCLOS_THRESH = 0.8    # perclos阈值
MAR_THRESH = 0.8
MOUTH_AR_CONSEC_FRAMES = 3
HAR_THRESH = 0.3
NOD_AR_CONSEC_FRAMES = 3
hCOUNTER = 0
hTOTAL = 0
COUNTER = 0
TOTAL = 0
mTOTAL = 0
mCOUNTER = 0

ZBData = []  #指标数据，分别为Ear、Mar、Har


# 人脸字典
FACIAL_LANDMARKS_68_IDXS = OrderedDict([
	("mouth", (48, 68)),
	("right_eyebrow", (17, 22)),
	("left_eyebrow", (22, 27)),
	("right_eye", (36, 42)),
	("left_eye", (42, 48)),
	("nose", (27, 36)),
	("jaw", (0, 17))
])

object_pts = np.float32([[6.825897, 6.760612, 4.402142],  #33左眉左上角
                         [1.330353, 7.122144, 6.903745],  #29左眉右角
                         [-1.330353, 7.122144, 6.903745], #34右眉左角
                         [-6.825897, 6.760612, 4.402142], #38右眉右上角
                         [5.311432, 5.485328, 3.987654],  #13左眼左上角
                         [1.789930, 5.393625, 4.413414],  #17左眼右上角
                         [-1.789930, 5.393625, 4.413414], #25右眼左上角
                         [-5.311432, 5.485328, 3.987654], #21右眼右上角
                         [2.005628, 1.409845, 6.165652],  #55鼻子左上角
                         [-2.005628, 1.409845, 6.165652], #49鼻子右上角
                         [2.774015, -2.080775, 5.048531], #43嘴左上角
                         [-2.774015, -2.080775, 5.048531],#39嘴右上角
                         [0.000000, -3.116408, 6.097667], #45嘴中央下角
                         [0.000000, -7.415691, 4.070434]])#6下巴角
K = [6.5308391993466671e+002, 0.0, 3.1950000000000000e+002,
     0.0, 6.5308391993466671e+002, 2.3950000000000000e+002,
     0.0, 0.0, 1.0]# 等价于矩阵[fx, 0, cx; 0, fy, cy; 0, 0, 1]
# 图像中心坐标系(uv)：相机畸变参数[k1, k2, p1, p2, k3]
D = [7.0834633684407095e-002, 6.9140193737175351e-002, 0.0, 0.0, -1.3073460323689292e+000]
reprojectsrc = np.float32([[10.0, 10.0, 10.0],
                           [10.0, 10.0, -10.0],
                           [10.0, -10.0, -10.0],
                           [10.0, -10.0, 10.0],
                           [-10.0, 10.0, 10.0],
                           [-10.0, 10.0, -10.0],
                           [-10.0, -10.0, -10.0],
                           [-10.0, -10.0, 10.0]])

# 绘制正方体12轴
line_pairs = [[0, 1], [1, 2], [2, 3], [3, 0],
              [4, 5], [5, 6], [6, 7], [7, 4],
              [0, 4], [1, 5], [2, 6], [3, 7]]

cam_matrix = np.array(K).reshape(3, 3).astype(np.float32)
dist_coeffs = np.array(D).reshape(5, 1).astype(np.float32)

print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor(args["shape_predictor"])
(lStart, lEnd) = FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = FACIAL_LANDMARKS_68_IDXS["right_eye"]
(mStart, mEnd) = FACIAL_LANDMARKS_68_IDXS["mouth"]

L_abel = []
E_ar = []
M_ar = []
H_ar = []
data = []

def shape_to_np(shape, dtype="int"):
	# 创建68*2
	coords = np.zeros((shape.num_parts, 2), dtype=dtype)
	# 遍历每一个关键点
	# 得到坐标
	for i in range(0, shape.num_parts):
		coords[i] = (shape.part(i).x, shape.part(i).y)
	return coords

def eye_aspect_ratio(eye):
	# 计算距离，竖直的
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    # 计算距离，水平的
    C = dist.euclidean(eye[0], eye[3])
    # ear值
    # print(A)
    # print(B)
    # print(2 * C)
    ear = (A + B) / (2.0 * C)
    return ear

def get_head_pose(shape):  # 头部姿态估计z
	# （像素坐标集合）填写2D参考点，注释遵循https://ibug.doc.ic.ac.uk/resources/300-W/
	# 17左眉左上角/21左眉右角/22右眉左上角/26右眉右上角/36左眼左上角/39左眼右上角/42右眼左上角/
	# 45右眼右上角/31鼻子左上角/35鼻子右上角/48左上角/54嘴右上角/57嘴中央下角/8下巴角
	image_pts = np.float32([shape[17], shape[21], shape[22], shape[26], shape[36],
							shape[39], shape[42], shape[45], shape[31], shape[35],
							shape[48], shape[54], shape[57], shape[8]])
	# solvePnP计算姿势——求解旋转和平移矩阵：
	# rotation_vec表示旋转矩阵，translation_vec表示平移矩阵，cam_matrix与K矩阵对应，dist_coeffs与D矩阵对应。
	_, rotation_vec, translation_vec = cv2.solvePnP(object_pts, image_pts, cam_matrix, dist_coeffs)
	# projectPoints重新投影误差：原2d点和重投影2d点的距离（输入3d点、相机内参、相机畸变、r、t，输出重投影2d点）
	reprojectdst, _ = cv2.projectPoints(reprojectsrc, rotation_vec, translation_vec, cam_matrix, dist_coeffs)
	reprojectdst = tuple(map(tuple, reprojectdst.reshape(8, 2)))  # 以8行2列显示

	# 计算欧拉角calc euler angle
	# 参考https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#decomposeprojectionmatrix
	rotation_mat, _ = cv2.Rodrigues(rotation_vec)  # 罗德里格斯公式（将旋转矩阵转换为旋转向量）
	pose_mat = cv2.hconcat((rotation_mat, translation_vec))  # 水平拼接，vconcat垂直拼接
	# decomposeProjectionMatrix将投影矩阵分解为旋转矩阵和相机矩阵
	_, _, _, _, _, _, euler_angle = cv2.decomposeProjectionMatrix(pose_mat)

	pitch, yaw, roll = [math.radians(_) for _ in euler_angle]

	pitch = math.degrees(math.asin(math.sin(pitch)))
	roll = -math.degrees(math.asin(math.sin(roll)))
	yaw = math.degrees(math.asin(math.sin(yaw)))
	# print('pitch:{}, yaw:{}, roll:{}'.format(pitch, yaw, roll))

	return reprojectdst, euler_angle  # 投影误差，欧拉角

def readVedio():
    print("readVedio")
    #通过摄像头读取帧图像
    # 输入流：实时视频/本地视频
    # 实时视频
    # video = cv2.VideoCapture(0)
    # 本地视频
    video = cv2.VideoCapture(r'./Video/R.mp4')
    # size = (960, 540)
    # size = (1920, 1080)
    flag = True
    while flag:
        flag, img = video.read()  # flag：是否成功打开摄像头
        if img is None:
            break
        # 调整窗口大小
        # cv2.namedWindow("video", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一直
        # cv2.resizeWindow("video", 306, 544)  # 设置长和宽
        # 转换成灰度图像
        # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # img = cv2.imdecode(data, 1)  # BGR mode, but need RGB mode,把1换成cv2.IMREAD_COLOR+cv2.IMREAD_IGNORE_ORIENTATION即可
        cv2.imshow('video', img)
        k = cv2.waitKey(1)

        # ESC退出
        if k == 27:
            break
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        getData(img, img_gray)
    video.release()
    # return img,img_gray

def getData(img, img_gray):
    # print("getData")
    #获取每一帧图像的Ear Mar Har值
    global E_ar,M_ar,H_ar,data,ear,mar,har, ZBData
    global EYE_AR_THRESH,EYE_AR_CONSEC_FRAMES,MAR_THRESH,PERCLOS_THRESH,HAR_THRESH,EYE_AR_THRESH,EYE_AR_CONSEC_FRAMES
    global PERCLOS_THRESH,MAR_THRESH,MOUTH_AR_CONSEC_FRAMES,HAR_THRESH,NOD_AR_CONSEC_FRAMES
    global hCOUNTER,hTOTAL,COUNTER,TOTAL,mTOTAL,mCOUNTER

    rects = detector(img_gray, 0)
    for i in range(len(rects)):
        landmarks = np.matrix([[p.x, p.y] for p in predictor(img, rects[i]).parts()])
        # 矩阵转为列表
        point_list = landmarks.getA()

        # 点坐标
        point_51 = (point_list[51][0], point_list[51][1])
        point_57 = (point_list[57][0], point_list[57][1])
        point_60 = (point_list[60][0], point_list[60][1])
        point_64 = (point_list[64][0], point_list[64][1])

        shape = predictor(img_gray, rects[i])
        shape = shape_to_np(shape)

        # 【指标】
        # EAR
        # EAR公式计算
        leftEye = shape[lStart:lEnd]
        leftEAR = eye_aspect_ratio(leftEye)
        leftEAR = eye_aspect_ratio(leftEye)

        rightEye = shape[rStart:rEnd]
        rightEAR = eye_aspect_ratio(rightEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0
        # print("EAR：" + "%.6f" % ear)

        # EAR阈值判断
        if ear < EYE_AR_THRESH:
            COUNTER += 1
        else:
            # 如果连续几帧都是闭眼的，总数算一次
            if COUNTER >= EYE_AR_CONSEC_FRAMES:
                TOTAL += 1
            # 重置
            COUNTER = 0

        # MAR
        mar_A = dist.euclidean(point_51, point_57)  # 51, 57
        mar_B = dist.euclidean(point_60, point_64)  # 60, 64
        mar = mar_A / mar_B
        # print("MAR：" + "%.6f" % mar)

        # MAR阈值判断
        if mar > MAR_THRESH:  # 张嘴阈值0.8
            mCOUNTER += 1
        elif mar <= MAR_THRESH and mar >= 0.5:  # 讲话阈值0.5-0.8
           None
        else:
            # 如果连续3次都小于阈值，则表示打了一次哈欠
            if mCOUNTER >= MOUTH_AR_CONSEC_FRAMES:  # 阈值：3
                mTOTAL += 1
            # 重置嘴帧计数器
            mCOUNTER = 0

        # HAR
        reprojectdst, euler_angle = get_head_pose(shape)

        har = euler_angle[0, 0]  # 取pitch旋转角度
        # print("har:" + "%.6f" % har)
        # HAR阈值判断
        if har > HAR_THRESH:  # 点头阈值0.3
            hCOUNTER += 1
        else:
            # 如果连续3次都小于阈值，则表示瞌睡点头一次
            if hCOUNTER >= NOD_AR_CONSEC_FRAMES:  # 阈值：3
                hTOTAL += 1
            # 重置点头帧计数器
            hCOUNTER = 0
    ZBData = np.array([ear,mar,har])
    # print(ZBData)
    getLabel(ZBData)

data = []
allData = []

def getLabel(ZBData):
    # print("getLabel")
    #根据每一帧图像的Ear Mar Har 输出其状态值Label
    global  pre_Label,data,allData
    # ZBData = np.array([ZBData])
    # load model from file
    # loaded_model = pickle.load(open("./XGBModel/xgb.pickle(39.15%).dat", "rb"))
    thisData = xgb.DMatrix([ZBData])
    # make predictions for test data
    Label = xgb_model.predict(thisData).astype(int)
    # print("XGBoostPredict:")
    # print(Label)
    data = list(ZBData).__add__(list(Label))
    allData.append(data)
    pre_Label.append(Label)

    if len(pre_Label)== 90:
        a = pre_Label
        pre_Label = []
        # print(len(pre_Label))
        LSTMPredict(a)
        # pre_Label = []
    # predictions = [round(value) for value in y_pred]

def LSTMPredict(preLabel):
    print("LSTMPredict")
    # global img
    #根据输入的90帧图像（3s视频）进行该段时间内状态的预测判断
    scaler = MinMaxScaler(feature_range=(0, 1))
    preLabel = np.array(preLabel)
    preLabel = scaler.fit_transform(preLabel)
    # model = load_model(os.path.join("DATA", "LSTMTest" + ".h5"))
    fatiguePredict = lstm_model.predict(preLabel)
    # 反归一化
    fatiguePredict = scaler.inverse_transform(fatiguePredict)
    fatiguePredict = fatiguePredict[0][0].astype(int)
    print("fatiguePredict:")
    print(fatiguePredict)

    global count0, count1, count2
    # 进行疲劳唤醒，规定连续5次计数时（即15s，1s30帧），哪个状态计数更多即判为那个状态
    if count0 + count1 + count2 < 4:
        if fatiguePredict == 0:
            count0 += 1
        elif fatiguePredict == 1:
            count1 += 1
        elif fatiguePredict == 2:
            count2 += 1
    elif count0 + count1 + count2 == 4:
        if fatiguePredict == 0:
            count0 += 1
        elif fatiguePredict == 1:
            count1 += 1
        elif fatiguePredict == 2:
            count2 += 1
        a=count0
        b=count1
        c=count2
        count0 = 0
        count1 = 0
        count2 = 0
        countFatigue(fatiguePredict,a,b,c)

def countFatigue(fatiguePredict, count0, count1, count2):
    print("countFatigue")
    #最终的疲劳状态判定+采取措施（15s一次）
    global MakeUp
    if count0!=count1 or count0!=count2 or count1!=count2:
        if count1 == count2 and count2 != 0:
            MakeUp = 2
        elif count0 == count2 and count2 != 0:
            MakeUp = 2
        elif count0 == count1 and count1 != 0:
            MakeUp = 1
        elif max(count0,count1,count2)==count0:
            MakeUp = 0 #清醒，不需要做什么
        elif max(count0,count1,count2)==count1:
            MakeUp = 1 #中度疲劳，先语音提醒再播放一段音乐
        elif max(count0,count1,count2)==count2:
            MakeUp = 2 #重度疲劳状态，需要提醒家属/管理者 并拨打电话
    elif count1 == count2 and count2!=0:
        MakeUp = 2
    elif count0 == count2 and count2!=0:
        MakeUp = 2
    elif count0 == count1 and count1!=0:
        MakeUp = 1
    # print(count0)
    # print(count1)
    # print(count2)
    #在语音/音乐or打电话途中，MakeUp始终为0
    print("MakeUp:")
    print(MakeUp)


# print("111111")
readVedio()
print(allData)
Ear = []
Mar = []
Har = []
Label = []
for x in allData:
    Ear.append(x[0])
    Mar.append(x[1])
    Har.append(x[2])
    Label.append(x[3])

data1 = { 'Ear': Ear, 'Mar': Mar, 'Har': Har, 'Label': Label}

pd.DataFrame(data1).to_excel(os.path.join('D:/ImageSolu/lab/data.xls'), sheet_name='Sheet1', index=False, engine='openpyxl')
