package com.example.carerserver.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("user")
public class User {
  private Integer id;
  private String nickName;
  private String phone;
  private String avatarImage;
  private Integer status;
}
