package com.example.carerserver.service;

import com.baomidou.mybatisplus.extension.service.IService;
import com.example.carerserver.pojo.Relationship;
import com.example.carerserver.pojo.User;


public interface RelationshipService extends IService<Relationship> {

    void repeat(Integer userId, Integer friendId);
}
