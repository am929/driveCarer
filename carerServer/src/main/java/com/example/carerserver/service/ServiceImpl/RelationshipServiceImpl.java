package com.example.carerserver.service.ServiceImpl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.carerserver.mapper.RelationshipMapper;
import com.example.carerserver.mapper.UserMapper;
import com.example.carerserver.pojo.Relationship;
import com.example.carerserver.pojo.User;
import com.example.carerserver.service.RelationshipService;
import com.example.carerserver.service.UserService;
import org.springframework.stereotype.Service;

@Service
public class RelationshipServiceImpl extends ServiceImpl<RelationshipMapper, Relationship> implements RelationshipService {


    @Override
    public void repeat(Integer userId, Integer friendId) {

    }
}
