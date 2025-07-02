package com.example.carerserver.service.ServiceImpl;

import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.carerserver.mapper.MessageMapper;
import com.example.carerserver.mapper.UserMapper;
import com.example.carerserver.pojo.Message;
import com.example.carerserver.pojo.User;
import com.example.carerserver.service.MessageService;
import com.example.carerserver.service.UserService;
import org.springframework.stereotype.Service;

@Service
public class MessageServiceImpl extends ServiceImpl<MessageMapper, Message> implements MessageService {


}
