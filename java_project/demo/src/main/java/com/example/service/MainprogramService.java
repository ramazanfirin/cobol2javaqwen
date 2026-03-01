package com.example.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MainprogramService {

    @Autowired
    private AdressService adressService;

    private Integer wsUserId;
    private String wsName;
    private String wsSurname;
    private String wsAddress;

    public UserData execute(Integer userId) {
        System.out.println("=== MAIN PROGRAM STARTED ===");

        this.wsUserId = userId;

        System.out.println("SQL: SELECT name, surname FROM users WHERE id = " + wsUserId);

        simulateSqlQuery();

        System.out.println("User Found: " + wsName + " " + wsSurname);

        System.out.println("Calling ADRESS program...");
        this.wsAddress = adressService.getAddress(wsUserId);

        System.out.println("==============================");
        System.out.println("RESULT:");
        System.out.println("  ID:       " + wsUserId);
        System.out.println("  Name:     " + wsName);
        System.out.println("  Surname:  " + wsSurname);
        System.out.println("  Address:  " + wsAddress);
        System.out.println("==============================");

        return new UserData(wsUserId, wsName, wsSurname, wsAddress);
    }

    private void simulateSqlQuery() {
        switch (wsUserId) {
            case 1:
                wsName = "John";
                wsSurname = "Doe";
                break;
            case 2:
                wsName = "Jane";
                wsSurname = "Smith";
                break;
            case 3:
                wsName = "Ahmet";
                wsSurname = "Yilmaz";
                break;
            default:
                wsName = "Unknown";
                wsSurname = "User";
                break;
        }
    }
}
