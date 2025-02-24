-- EXERCICI 3: Procediment per trobar el treballador amb la comissió més alta en "Sales"
CREATE OR REPLACE PROCEDURE p1_findCommisioPereraDavid
IS
    v_dept_id departments.department_id%TYPE;
    v_max_comm employees.commission_pct%TYPE;
    v_first_name employees.first_name%TYPE;
    v_last_name employees.last_name%TYPE;
    v_email employees.email%TYPE;
    v_hire_date employees.hire_date%TYPE;
BEGIN
    -- 1. Obtenir l'ID del departament 'Sales'
    v_dept_id := f1_finddept('Sales');

    -- 2. Si el departament existeix, obtenir la màxima comissió
    IF v_dept_id IS NOT NULL THEN
        v_max_comm := f2_finddeptcom(v_dept_id);

        -- 3. Si hi ha comissió, obtenir les dades del treballador amb la comissió més alta
        IF v_max_comm > 0 THEN
            SELECT first_name, last_name, email, hire_date
            INTO v_first_name, v_last_name, v_email, v_hire_date
            FROM EMPLOYEES
            WHERE department_id = v_dept_id
            AND commission_pct = v_max_comm
            FETCH FIRST 1 ROWS ONLY; -- En cas d'empat, agafem el primer

            -- 4. Mostrar les dades
            DBMS_OUTPUT.PUT_LINE('---------------- TREBALLADOR DE VENDES ----------------');
            DBMS_OUTPUT.PUT_LINE('NOM: ' || v_first_name || ' ' || v_last_name);
            DBMS_OUTPUT.PUT_LINE('EMAIL: ' || v_email);
            DBMS_OUTPUT.PUT_LINE('HIRE DATE: ' || TO_CHAR(v_hire_date, 'DD/MM/YYYY'));
            DBMS_OUTPUT.PUT_LINE('COMISSIÓ: ' || TO_CHAR(v_max_comm * 100) || ' %');
            DBMS_OUTPUT.PUT_LINE('------------------------------------------------------');
        ELSE
            DBMS_OUTPUT.PUT_LINE('No hi ha treballadors amb comissió en aquest departament.');
        END IF;
    ELSE
        DBMS_OUTPUT.PUT_LINE('No s''ha trobat el departament "Sales".');
    END IF;
END;
/
