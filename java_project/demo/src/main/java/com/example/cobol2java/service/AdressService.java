package com.example.cobol2java.service;

import org.springframework.stereotype.Service;

@Service
public class AdressService {

    public String getAddress(int id) {
        System.out.println("[ADRESS Program] Called with ID: " + id);

        System.out.println("[ADRESS Program] SQL: SELECT address FROM users WHERE id = " + id);
        String address = simulateSQLAddress(id);

        System.out.println("[ADRESS Program] Address found: " + address);
        System.out.println("[ADRESS Program] Returning to caller...");

        return address;
    }

    private String simulateSQLAddress(int id) {
        switch (id) {
            case 1:
                return "123 Main Street, New York, NY 10001";
            case 2:
                return "456 Oak Avenue, London, UK SW1A 1AA";
            case 3:
                return "789 Istiklal Cad, Istanbul, Turkey 34433";
            default:
                return "Unknown Address, City, Country";
        }
    }
}
