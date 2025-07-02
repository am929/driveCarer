package com.example.carerserver.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
@TableName("login")
@Data
public class Login {
 private Integer userId;
 private String account;
 private String password;
 private Integer isManager;

}
