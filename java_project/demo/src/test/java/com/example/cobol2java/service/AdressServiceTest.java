package com.example.cobol2java.service;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(classes = {AdressService.class})
class AdressServiceTest {

    @Autowired
    private AdressService adressService;

    @Test
    void testGetAddress_ValidId() {
        String result = adressService.getAddress(1);
        assertNotNull(result);
        assertEquals("123 Main Street, New York, NY 10001", result);
    }

    @Test
    void testGetAddress_InvalidId() {
        String result = adressService.getAddress(999);
        assertNotNull(result);
        assertEquals("Unknown Address, City, Country", result);
    }

    @Test
    void testGetAddress_AllAddresses() {
        String[] expectedAddresses = {
            "123 Main Street, New York, NY 10001",
            "456 Oak Avenue, London, UK SW1A 1AA",
            "789 Istiklal Cad, Istanbul, Turkey 34433"
        };

        for (int i = 0; i < expectedAddresses.length; i++) {
            String result = adressService.getAddress(i + 1);
            assertEquals(expectedAddresses[i], result);
        }
    }
}
