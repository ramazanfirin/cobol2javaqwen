package com.example.service;

public class UserData {
    private Integer id;
    private String name;
    private String surname;
    private String address;

    public UserData(Integer id, String name, String surname, String address) {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.address = address;
    }

    public Integer getId() { return id; }
    public String getName() { return name; }
    public String getSurname() { return surname; }
    public String getAddress() { return address; }

    @Override
    public String toString() {
        return "UserData{id=" + id + ", name='" + name + "', surname='" + surname + "', address='" + address + "'}";
    }
}
