from crewai import Agent
from config.llm import get_openai_api_key

def create_cobol_analyst():
    """COBOL dosyalarını analiz eden agent"""
    return Agent(
        role="COBOL Code Analyst",
        goal="Analyze COBOL source files and extract program structure",
        backstory="""You are a senior COBOL developer with 20+ years of experience.
        You understand PROGRAM-ID, PROCEDURE DIVISION, CALL statements.""",
        verbose=True
    )

def create_dependency_analyst():
    """CALL bağımlılıklarını analiz eden agent"""
    return Agent(
        role="Dependency Analyst",
        goal="Find all CALL relationships between COBOL programs",
        backstory="""You specialize in finding program dependencies.
        You identify CALL 'PROGRAM-NAME' patterns and build dependency graphs.""",
        verbose=True
    )

def create_java_converter():
    """COBOL'dan Java'ya dönüştüren agent"""
    return Agent(
        role="COBOL-to-Java Converter",
        goal="Convert COBOL programs to Spring Boot @Service classes",
        backstory="""You are an expert in both COBOL and Java/Spring Boot.
        You convert PROCEDURE DIVISION to Java methods, CALL to @Autowired services,
        DISPLAY to System.out.println.""",
        verbose=True
    )
