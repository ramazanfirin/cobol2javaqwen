from crewai import Task


def create_analyze_task(agent, cobol_files: dict):
    """COBOL dosyalarını analiz etme görevi"""
    return Task(
        description=f"""
        Analyze these COBOL files and extract PROGRAM-ID from each:

        {chr(10).join([f'=== {name} ==={chr(10)}{content}' for name, content in cobol_files.items()])}

        Create a summary table with: File, PROGRAM-ID, Line Count
        """,
        expected_output="Table with columns: File, PROGRAM-ID, Line Count",
        agent=agent
    )


def create_dependency_task(agent, cobol_files: dict):
    """CALL bağımlılıklarını analiz etme görevi"""
    return Task(
        description=f"""
        Find all CALL statements in these COBOL files:

        {chr(10).join([f'=== {name} ==={chr(10)}{content}' for name, content in cobol_files.items()])}

        Build a dependency map showing which programs call which.
        Format: PROGRAM_NAME -> [called_program1, called_program2]
        """,
        expected_output="Dependency map: program_name -> [called_programs]",
        agent=agent
    )


def create_conversion_task(agent, cobol_files: dict):
    """COBOL'dan Java'ya dönüştürme görevi"""
    return Task(
        description=f"""
        Convert these COBOL programs to Java @Service classes.

        COBOL Files:
        {chr(10).join([f'=== {name} ==={chr(10)}{content}' for name, content in cobol_files.items()])}

        Package Structure:
        - Service classes: com.example.cobol2java.service
        - DTO classes: com.example.cobol2java.dto
        
        Rules:
        1. PROGRAM-ID → ClassName (HELLO → HelloService)
        2. Add @Service annotation
        3. CALL 'PROG' → @Autowired ProgService progService
        4. DISPLAY → System.out.println
        5. PROCEDURE DIVISION → public method (e.g., execute() or getUser())
        
        DTO Rules:
        - Create DTO classes for data structures (e.g., UserData, AddressData)
        - Place DTO classes in com.example.cobol2java.dto package (NOT as subpackage)
        - Use standard Java bean conventions (private fields, getters, setters)
        - Include toString() method for debugging
        - Include all necessary fields based on COBOL WORKING-STORAGE variables
        
        Service Rules:
        - Place Service classes in com.example.cobol2java.service package
        - Use @Autowired for service dependencies (from CALL statements)
        - Methods should return DTOs when data is being returned
        
        Output Format:
        For each COBOL program, generate:
        1. Service class in com.example.cobol2java.service
        2. DTO class(es) in com.example.cobol2java.dto (if data structures are needed)
        
        Important: dto is a SIBLING package, not a child of service!
        - com.example.cobol2java.service (for @Service classes)
        - com.example.cobol2java.dto (for DTO classes)
        """,
        expected_output="Complete Java code with service in com.example.cobol2java.service and DTOs in com.example.cobol2java.dto",
        agent=agent
    )
