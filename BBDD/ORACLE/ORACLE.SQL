/* Variables */

DECLARE
i NUMBER;
BEGIN
i:=1;
WHILE i!=5 LOOP
 IF MOD(i,2)!=0 THEN
 DBMS_OUTPUT.PUT_LINE('HOLA'|| i);
 ELSE
 DBMS_OUTPUT.PUT_LINE ('ADIOS'||i);
 END IF;
 i:=i+1;
END LOOP;
END;

DECLARE
i NUMBER;
BEGIN
i:=1;
WHILE i<11 LOOP
 IF i mod 2 != 0 THEN
 DBMS_OUTPUT.PUT_LINE('HOLA'||i);
 ELSE
 DBMS_OUTPUT.PUT_LINE ('ADIOS'||i);
 END IF;
 i:=i+1;
END LOOP;
END;

DECLARE
i number;
f number;
r number;
BEGIN
i:=33;
f:=33;
r:=33;



DECLARE
inicio NUMBER := 0;
final NUMBER :=10;
resultado NUMBER :=0;
BEGIN
FOR i IN 33..43 LOOP
    DBMS_OUTPUT.PUT_LINE(' ');
    DBMS_OUTPUT.PUT_LINE('Tabla de multiplicar del '||i);
    FOR j IN inicio..final LOOP
        resultado := i*j;
        DBMS_OUTPUT.PUT_LINE(i||'x'||j||'='||resultado);
    END LOOP;
END LOOP;
END;
