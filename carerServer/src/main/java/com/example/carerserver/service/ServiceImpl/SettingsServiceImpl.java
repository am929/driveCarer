package com.example.carerserver.service.ServiceImpl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.carerserver.mapper.LoginMapper;
import com.example.carerserver.mapper.SettingsMapper;
import com.example.carerserver.pojo.Login;
import com.example.carerserver.pojo.Settings;
import com.example.carerserver.service.LoginService;
import com.example.carerserver.service.SettingsService;
import org.springframework.stereotype.Service;

@Service
public class SettingsServiceImpl extends ServiceImpl<SettingsMapper, Settings> implements SettingsService {


}
