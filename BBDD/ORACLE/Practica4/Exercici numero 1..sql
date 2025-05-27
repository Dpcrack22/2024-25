/* David Perera Gonzalez
   MP02. Bases de dades
   RA5. Llenguatge PL-SQL
   Exercici 1 */

/* 1. Secuencia SEQ_INVENTORIES_LOG */
CREATE SEQUENCE SEQ_INVENTORIES_LOG
START WITH 1
INCREMENT BY 1
NOCACHE
NOCYCLE;

/* 2. Función Secundaria  */
CREATE OR REPLACE FUNCTION F_update_inventory_Perera_David(
    p_product_id IN NUMBER,
    p_warehouse_id IN NUMBER,
    p_quantity IN NUMBER
) RETURN BOOLEAN IS
    v_count NUMBER;
    v_success BOOLEAN := TRUE;
BEGIN
    -- Verificar si el producto existe en el almacén
    SELECT COUNT(*) INTO v_count
    FROM inventories
    WHERE product_id = p_product_id AND warehouse_id = p_warehouse_id;
    
    -- Actualizar o insertar
    BEGIN
        IF v_count > 0 THEN
            UPDATE inventories
            SET quantity = quantity + p_quantity
            WHERE product_id = p_product_id AND warehouse_id = p_warehouse_id;
        ELSE
            INSERT INTO inventories (product_id, warehouse_id, quantity)
            VALUES (p_product_id, p_warehouse_id, p_quantity);
        END IF;
        COMMIT;
    EXCEPTION
        WHEN OTHERS THEN
            ROLLBACK;
            v_success := FALSE;
    END;
    
    RETURN v_success;
END F_update_inventory_Perera_David;
/

/*  */


/*  */


/*  */


/*  */


/*  */


/*  */


/*  */
/*  */
/*  */

