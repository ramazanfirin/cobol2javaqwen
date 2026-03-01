       IDENTIFICATION DIVISION.
       PROGRAM-ID. ADRESS.
       AUTHOR. Ramazan.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-USER-ID           PIC 9(5).
       01  WS-ADDRESS           PIC X(50).
       
       LINKAGE SECTION.
       01  LS-USER-ID           PIC 9(5).
       01  LS-ADDRESS           PIC X(50).
       
       PROCEDURE DIVISION USING LS-USER-ID LS-ADDRESS.
       ADRESS-PROCEDURE.
           DISPLAY "  [ADRESS Program] Called with ID: " LS-USER-ID.
           
           MOVE LS-USER-ID TO WS-USER-ID.
           
           DISPLAY "  [ADRESS Program] SQL: SELECT address FROM users"
                   " WHERE id = " WS-USER-ID.
           
           PERFORM SIMULATE-SQL-ADDRESS.
           
           MOVE WS-ADDRESS TO LS-ADDRESS.
           
           DISPLAY "  [ADRESS Program] Address found: " LS-ADDRESS.
           DISPLAY "  [ADRESS Program] Returning to caller...".
           
           EXIT PROGRAM.
       
       SIMULATE-SQL-ADDRESS.
           EVALUATE WS-USER-ID
               WHEN 1
                   MOVE "123 Main Street, New York, NY 10001" 
                        TO WS-ADDRESS
               WHEN 2
                   MOVE "456 Oak Avenue, London, UK SW1A 1AA" 
                        TO WS-ADDRESS
               WHEN 3
                   MOVE "789 Istiklal Cad, Istanbul, Turkey 34433" 
                        TO WS-ADDRESS
               WHEN OTHER
                   MOVE "Unknown Address, City, Country" TO WS-ADDRESS
           END-EVALUATE.
