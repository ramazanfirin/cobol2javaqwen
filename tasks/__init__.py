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


def create_mermaid_task(agent, dependency_map: dict):
    """Mermaid flow diyagramı oluşturma görevi"""
    return Task(
        description=f"""
        Create a Mermaid flow diagram showing the COBOL program dependencies.

        Dependency Map:
        {dependency_map}

        Rules:
        1. Use Mermaid flowchart syntax (flowchart TD)
        2. Each program is a node (e.g., A[MAINPROGRAM])
        3. CALL relationships are arrows (e.g., A --> B)
        4. Add descriptive labels to arrows showing "CALL"
        5. Use proper Mermaid syntax with subgraphs if needed

        Example Output Format:
        ```mermaid
        flowchart TD
            A[MAINPROGRAM] -->|CALL| B[ADRESS]
            B -->|CALL| C[UTILS]
        ```

        Create a complete Mermaid diagram file that can be rendered in:
        - GitHub Markdown
        - Mermaid Live Editor
        - Documentation tools

        Save the diagram as: dependency-diagram.md
        """,
        expected_output="Mermaid flowchart code in a markdown file",
        agent=agent
    )


def create_conversion_task(agent, cobol_files: dict):
    """COBOL'dan Java'ya dönüştürme görevi"""

    controller_example = '''
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

    test_example = '''
@SpringBootTest
class MainprogramServiceTest {

    @Autowired
    private MainprogramService mainprogramService;

    @Test
    void testGetUser() {
        UserData result = mainprogramService.getUser(1);
        assertNotNull(result);
        assertEquals("John", result.getName());
    }
}
'''

    naming_convention = "{ServiceName}Test.java or {ControllerName}Test.java"

    return Task(
        description=f"""
        Convert these COBOL programs to Java Spring Boot classes WITH unit tests.

        COBOL Files:
        {chr(10).join([f'=== {name} ==={chr(10)}{content}' for name, content in cobol_files.items()])}

        Package Structure:
        - Service classes: com.example.cobol2java.service
        - DTO classes: com.example.cobol2java.dto
        - Controller classes: com.example.cobol2java.controller
        - Test classes: src/test/java/com/example/cobol2java/service/
                       src/test/java/com/example/cobol2java/controller/

        Rules for Services:
        1. PROGRAM-ID → ClassName (MAINPROGRAM → MainprogramService)
        2. Add @Service annotation
        3. CALL 'PROG' → @Autowired ProgService progService
        4. DISPLAY → System.out.println
        5. PROCEDURE DIVISION → public method (e.g., getUser(), getAdress())
        6. Methods should return DTOs when data is being returned

        Rules for DTOs:
        - Create DTO classes for data structures (e.g., UserData, AddressData)
        - Place DTO classes in com.example.cobol2java.dto package
        - Use standard Java bean conventions (private fields, getters, setters)
        - Include toString() method for debugging

        Rules for Controllers:
        - Create @RestController classes for each main service
        - Place Controller classes in com.example.cobol2java.controller package
        - Use @RestController annotation
        - Use @RequestMapping for base path (e.g., "/api/users")
        - Use @GetMapping, @PostMapping for HTTP methods
        - Use @PathVariable for URL parameters
        - Use @Autowired to inject services
        - Return DTOs or ResponseEntity<DTO>

        Rules for Unit Tests:
        - Create JUnit 5 test classes for each Service and Controller
        - Place Service tests in src/test/java/com/example/cobol2java/service/
        - Place Controller tests in src/test/java/com/example/cobol2java/controller/
        - Use @SpringBootTest for integration tests
        - Use @WebMvcTest for controller tests
        - Use @MockBean to mock dependencies
        - Use AssertJ or JUnit assertions (assertNotNull, assertEquals, etc.)
        - Test happy path and edge cases (invalid input, null values)
        - Name tests: {naming_convention}

        Test Dependencies (pom.xml):
        - spring-boot-starter-test (includes JUnit 5, Mockito, AssertJ)

        Output Format:
        For each COBOL program, generate:
        1. Service class in com.example.cobol2java.service
        2. DTO class(es) in com.example.cobol2java.dto
        3. Controller class in com.example.cobol2java.controller (for main programs)
        4. Unit test class(es) in src/test/java/com/example/cobol2java/...

        Example Controller:
        {controller_example}

        Example Test:
        {test_example}
        """,
        expected_output="Complete Java code with services, DTOs, Controllers, and Unit Tests",
        agent=agent
    )
