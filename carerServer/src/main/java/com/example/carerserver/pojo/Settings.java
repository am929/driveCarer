package com.example.carerserver.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("information")
public class Settings {
  private Integer userId;
  private Integer closeEyeStatus;
  private Integer closeEyeTime;
  private Integer yawnStatus;
  private Integer yawnTime;
  private Integer turnStatus;
  private Integer turnTime;
  private Integer distractedStatus;
  private Integer distractedTime;
}
