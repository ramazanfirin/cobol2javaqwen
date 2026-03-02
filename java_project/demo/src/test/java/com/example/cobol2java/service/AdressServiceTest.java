package com.example.cobol2java.service;

import com.example.cobol2java.dto.AddressData;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class AdressServiceTest {

    @Autowired
    private AdressService adressService;

    @Test
    void testGetAddress() {
        AddressData result = adressService.getAddress(1);
        assertNotNull(result);
        assertEquals("123 Main Street, New York, NY 10001", result.getAddress());
    }

    @Test
    void testGetAddressUnknown() {
        AddressData result = adressService.getAddress(99);
        assertNotNull(result);
        assertEquals("Unknown Address, City, Country", result.getAddress());
    }
}
