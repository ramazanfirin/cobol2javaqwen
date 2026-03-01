package com.example.cobol2java.controller;

import com.example.cobol2java.dto.UserData;
import com.example.cobol2java.service.MainprogramService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private MainprogramService mainprogramService;

    @GetMapping("/{id}")
    public UserData getUser(@PathVariable int id) {
        return mainprogramService.getUser(id);
    }
}
