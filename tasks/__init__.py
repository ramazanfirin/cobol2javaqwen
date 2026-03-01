from crewai import Task

def create_analyze_task(agent):
    return Task(
        description="""
        1. List all .cbl and .cob files in cobol_files/ directory
        2. For each file, identify PROGRAM-ID
        3. Create a summary table
        """,
        expected_output="Table with columns: File, Program-ID, Line Count",
        agent=agent
    )

def create_dependency_task(agent):
    return Task(
        description="""
        1. Read each COBOL file in cobol_files/
        2. Find all CALL statements
        3. Build dependency map showing which programs call which
        """,
        expected_output="Dependency map: program_name -> [called_programs]",
        agent=agent
    )

def create_conversion_task(agent):
    return Task(
        description="""
        1. Convert each COBOL program to a Java @Service class
        2. PROGRAM-ID becomes class name (HELLO -> HelloService)
        3. CALL statements become @Autowired service calls
        4. DISPLAY becomes System.out.println
        5. PROCEDURE DIVISION becomes execute() method
        """,
        expected_output="Complete Java code for each COBOL program",
        agent=agent
    )
