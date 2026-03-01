import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process

# Load environment variables
load_dotenv()

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
    
    # Agent 1: COBOL Analyst
    analyst = Agent(
        role="COBOL Code Analyst",
        goal="Analyze COBOL source files and extract PROGRAM-ID from each file",
        backstory="""You are a senior COBOL developer with 20+ years of experience.
        You understand PROGRAM-ID, PROCEDURE DIVISION, CALL statements.""",
        verbose=True
    )
    
    # Agent 2: Dependency Analyst
    dependency_agent = Agent(
        role="Dependency Analyst",
        goal="Find all CALL relationships between COBOL programs",
        backstory="""You specialize in finding program dependencies.
        You identify CALL 'PROGRAM-NAME' patterns and build dependency graphs.""",
        verbose=True
    )
    
    # Agent 3: Java Converter
    converter = Agent(
        role="COBOL-to-Java Converter",
        goal="Convert COBOL programs to Spring Boot @Service classes",
        backstory="""You are an expert in both COBOL and Java/Spring Boot.
        You convert PROCEDURE DIVISION to Java methods, CALL to @Autowired services,
        DISPLAY to System.out.println.""",
        verbose=True
    )
    
    # Task 1: Analyze COBOL files
    analyze_task = Task(
        description=f"""
        Analyze these COBOL files and extract PROGRAM-ID from each:
        
        {chr(10).join([f'=== {name} ==={chr(10)}{content}' for name, content in cobol_files.items()])}
        
        Create a summary table with: File, PROGRAM-ID, Line Count
        """,
        expected_output="Table with columns: File, PROGRAM-ID, Line Count",
        agent=analyst
    )
    
    # Task 2: Find dependencies
    dependency_task = Task(
        description=f"""
        Find all CALL statements in these COBOL files:
        
        {chr(10).join([f'=== {name} ==={chr(10)}{content}' for name, content in cobol_files.items()])}
        
        Build a dependency map showing which programs call which.
        Format: PROGRAM_NAME -> [called_program1, called_program2]
        """,
        expected_output="Dependency map: program_name -> [called_programs]",
        agent=dependency_agent
    )
    
    # Task 3: Convert to Java
    conversion_task = Task(
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
        agent=converter
    )
    
    # Create crew
    crew = Crew(
        agents=[analyst, dependency_agent, converter],
        tasks=[analyze_task, dependency_task, conversion_task],
        verbose=True,
        process=Process.sequential
    )
    
    # Execute
    print("\n📊 Starting CrewAI execution...")
    result = crew.kickoff()
    print("\n✅ Conversion complete!")
    print(f"Result:\n{result}")

if __name__ == "__main__":
    main()
