package com.example.carerserver;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.example.carerserver.mapper")
public class CarerServerApplication {

    public static void main(String[] args) {
        SpringApplication.run(CarerServerApplication.class, args);
    }

}
