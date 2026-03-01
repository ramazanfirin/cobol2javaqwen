# COBOL to Java Converter with CrewAI 🚀

CrewAI kullanarak COBOL programlarını Java Spring Boot servislerine dönüştüren bir proje.

## 📋 Özellikler

- ✅ COBOL dosyalarını analiz eder (.cbl, .cob)
- ✅ PROGRAM-ID ve CALL bağımlılıklarını tespit eder
- ✅ Her COBOL programını `@Service` anotasyonlu Java sınıfına dönüştürür
- ✅ Spring Boot projesi oluşturur ve derler
- ✅ Bağımlılık analizi yapar (CALL → @Autowired)

## 🏗️ Proje Yapısı

```
crewai-grok-copy/
├── main.py                 # CrewAI ana script
├── config/
│   └── llm.py             # LLM ayarları
├── agents/
│   └── __init__.py        # Agent tanımları
├── tasks/
│   └── __init__.py        # Task tanımları
├── cobol_files/           # Kaynak COBOL dosyaları
├── java_project/          # Hedef Spring Boot projesi
│   └── demo/
│       └── src/
│           └── main/java/com/example/service/
│               ├── HelloService.java
│               ├── MainprogService.java
│               ├── AnaProgramService.java
│               └── DigerIslemService.java
└── venv/                  # Python virtual environment
```

## 🚀 Kurulum

### 1. Python Ortamı

```bash
# Virtual environment oluştur
python3 -m venv venv

# Aktif et
source venv/bin/activate

# Bağımlılıkları yükle
pip install crewai==0.1.7 python-dotenv
```

### 2. API Key Ayarı

`.env` dosyası oluştur ve OpenAI API key ekle:

```bash
echo "OPENAI_API_KEY=sk-proj-xxx" > .env
```

## 📖 Kullanım

### CrewAI ile Dönüşüm

```bash
source venv/bin/activate
python main.py
```

### Spring Boot Derleme

```bash
cd java_project/demo
mvn clean compile
```

### Spring Boot Çalıştırma

```bash
cd java_project/demo
mvn spring-boot:run
```

## 🤖 CrewAI Agentları

| Agent | Görevi |
|-------|--------|
| **COBOL Code Analyst** | COBOL dosyalarını analiz eder, PROGRAM-ID çıkarır |
| **Dependency Analyst** | CALL bağımlılıklarını tespit eder |
| **COBOL-to-Java Converter** | Java @Service sınıflarına dönüştürür |

## 📊 Dönüşüm Kuralları

| COBOL | Java |
|-------|------|
| `PROGRAM-ID. HELLO` | `public class HelloService` |
| `PROCEDURE DIVISION` | `public void execute()` |
| `DISPLAY 'text'` | `System.out.println("text")` |
| `CALL 'PROG'` | `@Autowired ProgService progService` |
| `STOP RUN` | (return) |

## 🛠️ Gereksinimler

- Python 3.8+
- Java 17+
- Maven 3.6+
- OpenAI API Key

## 📝 Örnek Çıktı

### COBOL (hello.cbl)
```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. HELLO.
PROCEDURE DIVISION.
    DISPLAY 'Merhaba'.
    STOP RUN.
```

### Java (HelloService.java)
```java
@Service
public class HelloService {
    public void execute() {
        System.out.println("Merhaba");
    }
}
```

## 📄 Lisans

MIT

## 👨‍💻 Yazar

Ramazan
