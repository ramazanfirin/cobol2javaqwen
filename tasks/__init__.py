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

        Rules:
        1. PROGRAM-ID → ClassName (HELLO → HelloService)
        2. Add @Service annotation
        3. CALL 'PROG' → @Autowired ProgService progService
        4. DISPLAY → System.out.println
        5. PROCEDURE DIVISION → public void execute() method

        Generate complete Java code for each COBOL program.
        """,
        expected_output="Complete Java code for each COBOL program",
        agent=agent
    )
