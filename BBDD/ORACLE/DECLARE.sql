DECLARE
    -- Cursor para obtener los gerentes y el número de empleados a su cargo
    CURSOR c_gerentes IS
        SELECT e.employee_id AS manager_id, 
               (SELECT COUNT(*) 
                FROM employees 
                WHERE manager_id = e.employee_id) AS num_empleats
        FROM employees e
        WHERE e.employee_id IN (SELECT DISTINCT manager_id FROM employees WHERE manager_id IS NOT NULL);

    -- Variable para almacenar cada fila del cursor
    r_gerente c_gerentes%ROWTYPE;

    v_aumento NUMBER; -- Variable para almacenar el aumento de salario
BEGIN
    -- Recorrer el cursor de gerentes
    FOR r_gerente IN c_gerentes LOOP
        -- Calcular el aumento de salario
        IF r_gerente.num_empleats <= 5 THEN
            v_aumento := r_gerente.num_empleats * 100;
        ELSE
            v_aumento := r_gerente.num_empleats * 85;
        END IF;

        -- Mostrar el resultado del aumento
        DBMS_OUTPUT.PUT_LINE(
            'Gerente ID: ' || r_gerente.manager_id || 
            ', Empleados a cargo: ' || r_gerente.num_empleats || 
            ', Aumento calculado: $' || v_aumento
        );
    END LOOP;
END;
/