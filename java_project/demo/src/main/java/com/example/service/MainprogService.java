package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MainprogService {
    @Autowired
    private HelloService helloService;

    public void execute() {
        System.out.println("Ana program başlıyor");
        helloService.execute();
        System.out.println("Ana program bitti");
    }
}
