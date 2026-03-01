import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_cobol_analyst, create_dependency_analyst, create_java_converter
from tasks import create_analyze_task, create_dependency_task, create_conversion_task

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

    # Agent'ları oluştur
    analyst = create_cobol_analyst()
    dependency_agent = create_dependency_analyst()
    converter = create_java_converter()

    # Task'ları oluştur
    analyze_task = create_analyze_task(analyst, cobol_files)
    dependency_task = create_dependency_task(dependency_agent, cobol_files)
    conversion_task = create_conversion_task(converter, cobol_files)

    # Crew oluştur
    crew = Crew(
        agents=[analyst, dependency_agent, converter],
        tasks=[analyze_task, dependency_task, conversion_task],
        verbose=True,
        process=Process.sequential
    )

    # Çalıştır
    print("\n📊 Starting CrewAI execution...")
    result = crew.kickoff()
    print("\n✅ Conversion complete!")
    print(f"Result:\n{result}")

if __name__ == "__main__":
    main()
