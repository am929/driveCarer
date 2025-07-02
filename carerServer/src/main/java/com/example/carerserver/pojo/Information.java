package com.example.carerserver.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("information")
public class Information {
  private Integer id;
  private Integer userId;
  private Integer driveTime;
  private Integer triedTime;
  private Integer clearTime;
  private Integer slightTriedTime;
  private Integer verTriedTime;
}
