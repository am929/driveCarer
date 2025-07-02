package com.example.carerserver.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.sql.Timestamp;

@Data
@TableName("message")
public class Message {
    private Integer id;
    private Integer userId;
    private Integer messageType;
    private String messageContent;
    private Timestamp time;
}
