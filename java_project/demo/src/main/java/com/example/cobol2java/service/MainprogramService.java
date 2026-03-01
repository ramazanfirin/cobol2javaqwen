package com.example.cobol2java.service;

import com.example.cobol2java.dto.UserData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MainprogramService {

    @Autowired
    private AdressService adressService;

    public UserData getUser(int id) {
        System.out.println("=== MAIN PROGRAM STARTED ===");

        System.out.println("SQL: SELECT name, surname FROM users WHERE id = " + id);
        UserData userData = simulateSQLQuery(id);

        System.out.println("User Found: " + userData.getName() + " " + userData.getSurname());

        System.out.println("Calling ADRESS program...");
        String address = adressService.getAddress(id);
        userData.setAddress(address);

        System.out.println("==============================");
        System.out.println("RESULT:");
        System.out.println("  ID:       " + userData.getId());
        System.out.println("  Name:     " + userData.getName());
        System.out.println("  Surname:  " + userData.getSurname());
        System.out.println("  Address:  " + userData.getAddress());
        System.out.println("==============================");

        return userData;
    }

    private UserData simulateSQLQuery(int id) {
        UserData userData = new UserData();
        userData.setId(id);
        switch (id) {
            case 1:
                userData.setName("John");
                userData.setSurname("Doe");
                break;
            case 2:
                userData.setName("Jane");
                userData.setSurname("Smith");
                break;
            case 3:
                userData.setName("Ahmet");
                userData.setSurname("Yilmaz");
                break;
            default:
                userData.setName("Unknown");
                userData.setSurname("User");
                break;
        }
        return userData;
    }
}
