package com.example.carerserver.controllers;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.carerserver.form.UserInfo;
import com.example.carerserver.pojo.Message;
import com.example.carerserver.pojo.User;
import com.example.carerserver.service.MessageService;
import com.example.carerserver.service.UserService;
import com.example.carerserver.vo.Result;
import com.example.carerserver.vo.UserVo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

import static com.sun.org.apache.xml.internal.serializer.utils.Utils.messages;

@RestController
@Slf4j
@RequestMapping("/personal")
public class PersonalContorller {
    @Autowired
    private UserService userService;
    @Autowired
    private MessageService messageService;

    @GetMapping("/getinfo/{id}")
    public Result getInfo(@PathVariable int id){
        //UserVo userVo = new UserVo();
        User user=userService.getById(id);
        //BeanUtils.copyProperties(user,userVo);
        return Result.success(user);
    }
    @PutMapping("/editinfo/{id}")
    public Result edit(@RequestBody UserInfo userInfo,@PathVariable int id){
        User user = new User();
        BeanUtils.copyProperties(userInfo,user);
        user.setId(id);
        userService.updateById(user);
        UserVo userVo = new UserVo();
       user=userService.getById(id);
       BeanUtils.copyProperties(user,userVo);
        return Result.success(userVo);
    }

    @GetMapping("/messagelist/{userId}")
    public Result getmessagelist(@PathVariable int userId){
        QueryWrapper query=new QueryWrapper();
        query.eq("user_id",userId);
        List<Message> messages=messageService.list(query);
        return Result.success(messages);
    }

    @GetMapping("/messagecontent/{id}")
    public Result getmessageDetail(@PathVariable int id){
        Message message = new Message();
        message=messageService.getById(id);
        return Result.success(message.getMessageContent());
    }
    //
    @GetMapping("/statistic/{id}")
    public Result getmessageDetail(){

        return Result.success();
    }

}
