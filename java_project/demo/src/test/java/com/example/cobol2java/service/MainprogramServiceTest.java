package com.example.cobol2java.service;

import com.example.cobol2java.dto.UserData;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(classes = {MainprogramService.class, AdressService.class})
class MainprogramServiceTest {

    @Autowired
    private MainprogramService mainprogramService;

    @Test
    void testGetUser_UserExists() {
        UserData result = mainprogramService.getUser(1);
        assertNotNull(result);
        assertEquals("John", result.getName());
        assertEquals("Doe", result.getSurname());
        assertEquals("123 Main Street, New York, NY 10001", result.getAddress());
    }

    @Test
    void testGetUser_UserNotFound() {
        UserData result = mainprogramService.getUser(999);
        assertNotNull(result);
        assertEquals("Unknown", result.getName());
        assertEquals("User", result.getSurname());
    }

    @Test
    void testGetUser_AllUsers() {
        for (int i = 1; i <= 3; i++) {
            UserData result = mainprogramService.getUser(i);
            assertNotNull(result);
            assertNotNull(result.getName());
            assertNotNull(result.getSurname());
            assertNotNull(result.getAddress());
        }
    }
}
