package com.example.carerserver.controllers;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.carerserver.pojo.Relationship;
import com.example.carerserver.pojo.User;
import com.example.carerserver.service.RelationshipService;
import com.example.carerserver.service.UserService;
import com.example.carerserver.vo.Result;
import com.example.carerserver.vo.UserVo;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.ArrayList;
import java.util.List;

@RestController
@Slf4j
//程序的访问地址，以及资源
@RequestMapping("/friend")
public class FriendshipController {
    @Autowired
    private RelationshipService relationshipService;
    @Autowired
    private UserService userService;

    @GetMapping("/getfriend/{id}")
    public Result friendlist(@PathVariable int id){
        QueryWrapper query = new QueryWrapper();
        query.eq("user_id",id);

        List<Relationship> relationships=relationshipService.list(query);
        return Result.success(relationships);
    }

    @GetMapping("/findfriend/{phone}")
    public Result findfriend(@PathVariable String phone){
        QueryWrapper query = new QueryWrapper();
        query.eq("phone",phone);
        User user = userService.getOne(query);
        UserVo userVo = new UserVo();
        BeanUtils.copyProperties(user,userVo);
        return Result.success(userVo);
    }

    @GetMapping("/addfriend/{userId}/{friendId}/{relation}")
    public Result addFriend(@PathVariable Integer friendId,@PathVariable Integer userId,@PathVariable String relation){
        Relationship relationship1 = new Relationship();
        relationship1.setUserId(userId);
        relationship1.setFriendId(friendId);
        relationship1.setRelationship(relation);
        QueryWrapper query = new QueryWrapper();
        query.eq("user_id",userId);
        query.eq("friend_id",friendId);
        List<Relationship> list = relationshipService.list(query);
        if(list.size()==0){
            relationshipService.save(relationship1);
            return Result.success(list);
        }else{
            return Result.fail("repeat");
        }
    }

    @DeleteMapping("/deletefriend/{userId}/{friendId}")
    public Result deleteFriend(@PathVariable int userId,@PathVariable int friendId){
        QueryWrapper query = new QueryWrapper();
        query.eq("user_id",userId);
        query.eq("friend_id",friendId);
        relationshipService.remove(query);
        return Result.success();
    }
}
