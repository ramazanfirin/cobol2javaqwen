package com.example.cobol2java.service;

import com.example.cobol2java.dto.UserData;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class MainprogramServiceTest {

    @Autowired
    private MainprogramService mainprogramService;

    @Test
    void testGetUser() {
        UserData result = mainprogramService.getUser(1);
        assertNotNull(result);
        assertEquals("John", result.getName());
        assertEquals("Doe", result.getSurname());
    }

    @Test
    void testGetUserUnknown() {
        UserData result = mainprogramService.getUser(99);
        assertNotNull(result);
        assertEquals("Unknown", result.getName());
        assertEquals("User", result.getSurname());
    }
}
