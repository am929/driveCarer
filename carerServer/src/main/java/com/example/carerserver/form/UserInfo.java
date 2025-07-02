package com.example.carerserver.form;

import lombok.Data;

@Data
public class UserInfo {
    private Integer id;
    private String account;
    private String password;

    private String nickName;
    private String phone;
 //   private String avatarImage;
    private Integer status;
}


//         "account":"20202005212"
//         "password":"8688"
//         "nickName":"yiliu"
//         "phone":"20202005212"
//         "status":"0"