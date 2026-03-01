package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class AnaProgramService {

    @Autowired
    private HelloService helloService;

    @Autowired
    private DigerIslemService digerIslemService;

    public void execute() {
        System.out.println("Ana program basladi");
        helloService.execute();
        digerIslemService.execute();
        System.out.println("Ana program bitti");
    }
}
