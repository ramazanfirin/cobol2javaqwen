package com.example.cobol2java.dto;

public class AddressData {
    private int userId;
    private String address;

    public int getUserId() {
        return userId;
    }

    public void setUserId(int userId) {
        this.userId = userId;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "AddressData{" +
                "userId=" + userId +
                ", address='" + address + '\'' +
                '}';
    }
}
