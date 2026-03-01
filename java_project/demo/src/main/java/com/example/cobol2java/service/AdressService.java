package com.example.cobol2java.service;

import com.example.cobol2java.dto.AddressData;
import org.springframework.stereotype.Service;

@Service
public class AdressService {

    public AddressData getAddress(int userId) {
        System.out.println("  [ADRESS Program] Called with ID: " + userId);
        
        System.out.println("  [ADRESS Program] SQL: SELECT address FROM users WHERE id = " + userId);
        
        AddressData addressData = simulateSqlAddress(userId);
        
        System.out.println("  [ADRESS Program] Address found: " + addressData.getAddress());
        
        return addressData;
    }
    
    private AddressData simulateSqlAddress(int userId) {
        AddressData addressData = new AddressData();
        addressData.setUserId(userId);
        
        switch (userId) {
            case 1:
                addressData.setAddress("123 Main Street, New York, NY 10001");
                break;
            case 2:
                addressData.setAddress("456 Oak Avenue, London, UK SW1A 1AA");
                break;
            case 3:
                addressData.setAddress("789 Istiklal Cad, Istanbul, Turkey 34433");
                break;
            default:
                addressData.setAddress("Unknown Address, City, Country");
                break;
        }
        
        return addressData;
    }
}
