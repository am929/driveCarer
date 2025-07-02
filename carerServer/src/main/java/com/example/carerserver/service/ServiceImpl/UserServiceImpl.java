package com.example.carerserver.service.ServiceImpl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.carerserver.mapper.UserMapper;
import com.example.carerserver.pojo.Login;
import com.example.carerserver.pojo.User;
import com.example.carerserver.service.LoginService;
import com.example.carerserver.service.UserService;
import org.springframework.stereotype.Service;

@Service
public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {


}
