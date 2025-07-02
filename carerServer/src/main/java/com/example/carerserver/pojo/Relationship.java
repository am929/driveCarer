package com.example.carerserver.pojo;

import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("relationship")
public class Relationship {
    private Integer id;
    private Integer userId;
    private Integer friendId;
    private String relationship;
}
