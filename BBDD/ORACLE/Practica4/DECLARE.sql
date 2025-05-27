DECLARE
    v_result NUMBER;
    v_test_product_id NUMBER := 1;          -- Cambia al ID de un producto que EXISTA
    v_test_countries VARCHAR2(100) := 'US'; -- Cambia a países que EXISTAN (ej: 'US,ES')
    v_test_qty NUMBER := 5;
BEGIN
    -- 1. Inicializar log (limpia y carga datos actuales)
    BEGIN
        P_inventories_log_init_Perera_David;
        DBMS_OUTPUT.PUT_LINE('✔ Log inicializado correctamente');
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('✖ Error en P_inventories_log_init: ' || SQLERRM);
            RETURN;
    END;
    
    -- 2. Mostrar datos de prueba
    DBMS_OUTPUT.PUT_LINE('─────────────────────────────');
    DBMS_OUTPUT.PUT_LINE('Parámetros de prueba:');
    DBMS_OUTPUT.PUT_LINE('Producto ID: ' || v_test_product_id);
    DBMS_OUTPUT.PUT_LINE('Países: ' || v_test_countries);
    DBMS_OUTPUT.PUT_LINE('Cantidad: ' || v_test_qty);
    
    -- 3. Ejecutar función principal
    BEGIN
        v_result := F_update_inventories_Perera_David(
            v_test_product_id, 
            v_test_countries, 
            v_test_qty
        );
    EXCEPTION
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('✖ Error en F_update_inventories: ' || SQLERRM);
            RETURN;
    END;
    
    -- 4. Interpretar resultado
    DBMS_OUTPUT.PUT_LINE('─────────────────────────────');
    DBMS_OUTPUT.PUT_LINE('RESULTADO:');
    
    CASE v_result
        WHEN -2 THEN 
            DBMS_OUTPUT.PUT_LINE('❌ El producto ' || v_test_product_id || ' no existe');
            DBMS_OUTPUT.PUT_LINE('ℹ Ejecuta esto para ver productos válidos:');
            DBMS_OUTPUT.PUT_LINE('   SELECT product_id, product_name FROM products WHERE ROWNUM < 5;');
        WHEN -1 THEN 
            DBMS_OUTPUT.PUT_LINE('❌ Uno o más países no existen: ' || v_test_countries);
            DBMS_OUTPUT.PUT_LINE('ℹ Ejecuta esto para ver países válidos:');
            DBMS_OUTPUT.PUT_LINE('   SELECT DISTINCT country_id FROM warehouses WHERE ROWNUM < 5;');
        WHEN 0 THEN 
            DBMS_OUTPUT.PUT_LINE('⚠ Países válidos, pero NO tienen almacenes: ' || v_test_countries);
        ELSE 
            DBMS_OUTPUT.PUT_LINE('✅ ÉXITO: Se añadieron ' || v_result || ' unidades');
            DBMS_OUTPUT.PUT_LINE('ℹ Verifica el log con:');
            DBMS_OUTPUT.PUT_LINE('   SELECT * FROM inventories_log ORDER BY created_at DESC;');
    END CASE;
END;
/