package com.example.cobol2java.service;

import com.example.cobol2java.dto.UserData;
import com.example.cobol2java.dto.AddressData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class MainprogramService {

    @Autowired
    private AdressService adressService;

    public UserData getUser(int userId) {
        System.out.println("=== MAIN PROGRAM STARTED ===");
        UserData userData = simulateSqlQuery(userId);
        System.out.println("User Found: " + userData.getName() + " " + userData.getSurname());
        System.out.println("Calling ADRESS program...");
        AddressData addressData = adressService.getAddress(userId);
        System.out.println("==============================");
        System.out.println("RESULT:");
        System.out.println("  ID:       " + userId);
        System.out.println("  Name:     " + userData.getName());
        System.out.println("  Surname:  " + userData.getSurname());
        System.out.println("  Address:  " + addressData.getAddress());
        System.out.println("==============================");
        return userData;
    }

    private UserData simulateSqlQuery(int userId) {
        UserData userData = new UserData();
        userData.setUserId(userId);
        switch (userId) {
            case 1: userData.setName("John"); userData.setSurname("Doe"); break;
            case 2: userData.setName("Jane"); userData.setSurname("Smith"); break;
            case 3: userData.setName("Ahmet"); userData.setSurname("Yilmaz"); break;
            default: userData.setName("Unknown"); userData.setSurname("User"); break;
        }
        return userData;
    }
}
