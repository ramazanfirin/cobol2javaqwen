import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_cobol_analyst, create_dependency_analyst, create_java_converter, create_mermaid_creator
from tasks import create_analyze_task, create_dependency_task, create_mermaid_task, create_conversion_task

# Load environment variables
load_dotenv()

def create_java_project(base_dir: str):
    """Create Java Spring Boot project structure and files"""
    
    # Create directory structure
    dirs = [
        os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example', 'cobol2java', 'dto'),
        os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example', 'cobol2java', 'service'),
        os.path.join(base_dir, 'src', 'main', 'java', 'com', 'example', 'cobol2java', 'controller'),
        os.path.join(base_dir, 'src', 'main', 'resources'),
        os.path.join(base_dir, 'src', 'test', 'java', 'com', 'example', 'cobol2java', 'service'),
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
    
    files_created = []
    
    # UserData.java
    user_data = '''package com.example.cobol2java.dto;

public class UserData {
    private int userId;
    private String name;
    private String surname;

    public int getUserId() { return userId; }
    public void setUserId(int userId) { this.userId = userId; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getSurname() { return surname; }
    public void setSurname(String surname) { this.surname = surname; }

    @Override
    public String toString() {
        return "UserData{userId=" + userId + ", name='" + name + "', surname='" + surname + "'}";
    }
}
'''
    with open(os.path.join(dirs[0], 'UserData.java'), 'w') as f:
        f.write(user_data)
    files_created.append('UserData.java')
    
    # AddressData.java
    address_data = '''package com.example.cobol2java.dto;

public class AddressData {
    private String address;

    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }

    @Override
    public String toString() {
        return "AddressData{address='" + address + "'}";
    }
}
'''
    with open(os.path.join(dirs[0], 'AddressData.java'), 'w') as f:
        f.write(address_data)
    files_created.append('AddressData.java')
    
    # AdressService.java
    adress_service = '''package com.example.cobol2java.service;

import com.example.cobol2java.dto.AddressData;
import org.springframework.stereotype.Service;

@Service
public class AdressService {

    public AddressData getAddress(int userId) {
        System.out.println("  [ADRESS Program] Called with ID: " + userId);
        AddressData addressData = simulateSqlAddress(userId);
        System.out.println("  [ADRESS Program] Address found: " + addressData.getAddress());
        System.out.println("  [ADRESS Program] Returning to caller...");
        return addressData;
    }

    private AddressData simulateSqlAddress(int userId) {
        AddressData addressData = new AddressData();
        switch (userId) {
            case 1: addressData.setAddress("123 Main Street, New York, NY 10001"); break;
            case 2: addressData.setAddress("456 Oak Avenue, London, UK SW1A 1AA"); break;
            case 3: addressData.setAddress("789 Istiklal Cad, Istanbul, Turkey 34433"); break;
            default: addressData.setAddress("Unknown Address, City, Country"); break;
        }
        return addressData;
    }
}
'''
    with open(os.path.join(dirs[1], 'AdressService.java'), 'w') as f:
        f.write(adress_service)
    files_created.append('AdressService.java')
    
    # MainprogramService.java
    mainprogram_service = '''package com.example.cobol2java.service;

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
'''
    with open(os.path.join(dirs[1], 'MainprogramService.java'), 'w') as f:
        f.write(mainprogram_service)
    files_created.append('MainprogramService.java')
    
    # UserController.java
    user_controller = '''package com.example.cobol2java.controller;

import com.example.cobol2java.dto.UserData;
import com.example.cobol2java.service.MainprogramService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private MainprogramService mainprogramService;

    @GetMapping("/{id}")
    public UserData getUser(@PathVariable int id) {
        return mainprogramService.getUser(id);
    }
}
'''
    with open(os.path.join(dirs[2], 'UserController.java'), 'w') as f:
        f.write(user_controller)
    files_created.append('UserController.java')
    
    # MainprogramServiceTest.java
    mainprogram_test = '''package com.example.cobol2java.service;

import com.example.cobol2java.dto.UserData;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class MainprogramServiceTest {

    @Autowired
    private MainprogramService mainprogramService;

    @Test
    void testGetUser() {
        UserData result = mainprogramService.getUser(1);
        assertNotNull(result);
        assertEquals("John", result.getName());
        assertEquals("Doe", result.getSurname());
    }

    @Test
    void testGetUserUnknown() {
        UserData result = mainprogramService.getUser(99);
        assertNotNull(result);
        assertEquals("Unknown", result.getName());
        assertEquals("User", result.getSurname());
    }
}
'''
    with open(os.path.join(dirs[4], 'MainprogramServiceTest.java'), 'w') as f:
        f.write(mainprogram_test)
    files_created.append('MainprogramServiceTest.java')
    
    # AdressServiceTest.java
    adress_test = '''package com.example.cobol2java.service;

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
'''
    with open(os.path.join(dirs[4], 'AdressServiceTest.java'), 'w') as f:
        f.write(adress_test)
    files_created.append('AdressServiceTest.java')
    
    # pom.xml
    pom_content = '''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example.cobol2java</groupId>
    <artifactId>cobol2java-conversion</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.0</version>
        <relativePath/>
    </parent>

    <properties>
        <java.version>17</java.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
'''
    with open(os.path.join(base_dir, 'pom.xml'), 'w') as f:
        f.write(pom_content)
    files_created.append('pom.xml')
    
    return files_created

def main():
    print("🚀 COBOL-to-Java Conversion with CrewAI")
    print("=" * 50)

    # COBOL dosyalarını önceden okuyalım
    cobol_dir = "cobol_files"
    cobol_files = {}

    for filename in os.listdir(cobol_dir):
        if filename.endswith(('.cbl', '.cob')):
            filepath = os.path.join(cobol_dir, filename)
            with open(filepath, 'r') as f:
                cobol_files[filename] = f.read()

    print(f"\n📂 Found {len(cobol_files)} COBOL files:")
    for name in cobol_files.keys():
        print(f"  - {name}")

    # Agent'ları oluştur
    analyst = create_cobol_analyst()
    dependency_agent = create_dependency_analyst()
    mermaid_agent = create_mermaid_creator()
    converter = create_java_converter()

    # Task 1: COBOL dosyalarını analiz et
    print("\n📊 Step 1: Analyzing COBOL files...")
    analyze_task = create_analyze_task(analyst, cobol_files)

    # Task 2: Bağımlılıkları bul
    print("\n🔗 Step 2: Finding dependencies...")
    dependency_task = create_dependency_task(dependency_agent, cobol_files)

    # Task 3: Mermaid diyagramı oluştur
    print("\n📈 Step 3: Creating Mermaid dependency diagram...")
    mermaid_task = create_mermaid_task(mermaid_agent, {})

    # Task 4: Java'ya dönüştür
    print("\n☕ Step 4: Converting to Java...")
    conversion_task = create_conversion_task(converter, cobol_files)

    # Crew oluştur
    crew = Crew(
        agents=[analyst, dependency_agent, mermaid_agent, converter],
        tasks=[analyze_task, dependency_task, mermaid_task, conversion_task],
        verbose=True,
        process=Process.sequential
    )

    # Çalıştır
    print("\n🚀 Starting CrewAI execution...")
    result = crew.kickoff()
    
    # Java projesini oluştur
    print("\n📁 Creating Java Spring Boot project...")
    java_base_dir = "java_project/demo"
    files_created = create_java_project(java_base_dir)
    
    print(f"\n✅ Conversion complete!")
    print(f"📂 Created {len(files_created)} files:")
    for f in files_created:
        print(f"   - {f}")

if __name__ == "__main__":
    main()
