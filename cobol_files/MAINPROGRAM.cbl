       IDENTIFICATION DIVISION.
       PROGRAM-ID. MAINPROGRAM.
       AUTHOR. Ramazan.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT USER-FILE ASSIGN TO "USER.DAT"
           ORGANIZATION IS INDEXED.
       
       DATA DIVISION.
       FILE SECTION.
       FD  USER-FILE.
       01  USER-RECORD.
           05  USER-ID          PIC 9(5).
           05  USER-NAME        PIC X(20).
           05  USER-SURNAME     PIC X(20).
       
       WORKING-STORAGE SECTION.
       01  WS-USER-ID           PIC 9(5).
       01  WS-NAME              PIC X(20).
       01  WS-SURNAME           PIC X(20).
       01  WS-ADDRESS           PIC X(50).
       01  WS-STATUS            PIC X(10).
       
       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           DISPLAY "=== MAIN PROGRAM STARTED ===".
           
           DISPLAY "Enter User ID: ".
           ACCEPT WS-USER-ID.
           
           DISPLAY "SQL: SELECT name, surname FROM users WHERE id = "
                   WS-USER-ID.
           
           PERFORM SIMULATE-SQL-QUERY.
           
           DISPLAY "User Found: " WS-NAME " " WS-SURNAME.
           
           DISPLAY "Calling ADRESS program...".
           CALL "ADRESS" USING WS-USER-ID WS-ADDRESS.
           
           DISPLAY "==============================".
           DISPLAY "RESULT:".
           DISPLAY "  ID:       " WS-USER-ID.
           DISPLAY "  Name:     " WS-NAME.
           DISPLAY "  Surname:  " WS-SURNAME.
           DISPLAY "  Address:  " WS-ADDRESS.
           DISPLAY "==============================".
           
           STOP RUN.
       
       SIMULATE-SQL-QUERY.
           EVALUATE WS-USER-ID
               WHEN 1
                   MOVE "John" TO WS-NAME
                   MOVE "Doe" TO WS-SURNAME
               WHEN 2
                   MOVE "Jane" TO WS-NAME
                   MOVE "Smith" TO WS-SURNAME
               WHEN 3
                   MOVE "Ahmet" TO WS-NAME
                   MOVE "Yilmaz" TO WS-SURNAME
               WHEN OTHER
                   MOVE "Unknown" TO WS-NAME
                   MOVE "User" TO WS-SURNAME
           END-EVALUATE.
