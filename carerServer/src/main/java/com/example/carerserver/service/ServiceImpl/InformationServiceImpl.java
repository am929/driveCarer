package com.example.carerserver.service.ServiceImpl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.carerserver.mapper.InformationMapper;
import com.example.carerserver.mapper.LoginMapper;
import com.example.carerserver.pojo.Information;
import com.example.carerserver.pojo.Login;
import com.example.carerserver.service.InformationService;
import com.example.carerserver.service.LoginService;
import org.springframework.stereotype.Service;

@Service
public class InformationServiceImpl extends ServiceImpl<InformationMapper, Information> implements InformationService {


}
