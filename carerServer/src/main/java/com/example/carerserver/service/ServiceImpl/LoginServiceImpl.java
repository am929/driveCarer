package com.example.carerserver.service.ServiceImpl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.carerserver.mapper.LoginMapper;
import com.example.carerserver.pojo.Login;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.example.carerserver.service.LoginService;

@Service
public class LoginServiceImpl extends ServiceImpl<LoginMapper, Login> implements LoginService {


}
