package com.example.carerserver.controllers;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.example.carerserver.form.UserInfo;
import com.example.carerserver.pojo.Login;
import com.example.carerserver.pojo.User;
import com.example.carerserver.service.UserService;
import com.example.carerserver.vo.Result;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.web.bind.annotation.*;
import com.example.carerserver.service.LoginService;

import java.util.ArrayList;
import java.util.List;

@RestController
@Slf4j
@RequestMapping("/login")
public class LoginController {
    @Autowired
    private LoginService loginService;
    @Autowired
    private UserService userService;

    @PostMapping("/signup")
    public Result sginup(@RequestBody UserInfo userInfo){
        Login login = new Login();
        BeanUtils.copyProperties(userInfo,login);
        User user = new User();
        BeanUtils.copyProperties(userInfo,user);
        log.info("userinfo:{}",userInfo);
        QueryWrapper queryWrapper=new QueryWrapper();
        queryWrapper.eq("account",login.getAccount());
        if(loginService.count(queryWrapper)==0) {
            loginService.save(login);
            user.setId(login.getUserId());
            userService.save(user);
            return Result.success();
        }else{
            return Result.fail("Repeat registered");
        }
    }

    @PostMapping("/signin")
    public Result signin(@RequestBody Login login){
        QueryWrapper queryWrapper=new QueryWrapper();
        queryWrapper.eq("account",login.getAccount());

        Login login1 = loginService.getOne(queryWrapper);
        log.info("aaa={}",loginService.count(queryWrapper));
        if(login.getPassword().equals(login1.getPassword()))
            return Result.success(login);
        else
            return Result.fail();
    }




}
