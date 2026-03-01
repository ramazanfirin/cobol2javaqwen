import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_cobol_analyst, create_dependency_analyst, create_java_converter, create_mermaid_creator
from tasks import create_analyze_task, create_dependency_task, create_mermaid_task, create_conversion_task

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
    print("\n✅ Conversion complete!")
    print(f"Result:\n{result}")

if __name__ == "__main__":
    main()
