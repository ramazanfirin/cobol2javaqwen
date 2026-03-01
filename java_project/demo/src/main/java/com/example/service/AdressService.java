package com.example.service;

import org.springframework.stereotype.Service;

@Service
public class AdressService {

    private Integer wsUserId;
    private String wsAddress;

    public String getAddress(Integer userId) {
        System.out.println("  [ADRESS Program] Called with ID: " + userId);

        this.wsUserId = userId;

        System.out.println("  [ADRESS Program] SQL: SELECT address FROM users WHERE id = " + wsUserId);

        simulateSqlAddress();

        System.out.println("  [ADRESS Program] Address found: " + wsAddress);
        System.out.println("  [ADRESS Program] Returning to caller...");

        return wsAddress;
    }

    private void simulateSqlAddress() {
        switch (wsUserId) {
            case 1:
                wsAddress = "123 Main Street, New York, NY 10001";
                break;
            case 2:
                wsAddress = "456 Oak Avenue, London, UK SW1A 1AA";
                break;
            case 3:
                wsAddress = "789 Istiklal Cad, Istanbul, Turkey 34433";
                break;
            default:
                wsAddress = "Unknown Address, City, Country";
                break;
        }
    }
}
