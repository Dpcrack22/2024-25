CREATE OR REPLACE FUNCTION search_warehouse_for_product (
    p_product_id IN NUMBER,
    p_country_code IN VARCHAR2
) RETURN NUMBER IS
    v_warehouse_id NUMBER;
    v_quantity NUMBER;
    v_product_exists BOOLEAN := FALSE;
    v_product_count NUMBER;
BEGIN
    -- Comprobar si el producto existe
    SELECT COUNT(*)
    INTO v_product_count
    FROM products
    WHERE product_id = p_product_id;

    IF v_product_count = 0 THEN
        RETURN NULL; -- El producto no existe
    END IF;

    -- Buscar el almacén con mayor cantidad en el país
    FOR rec IN (
        SELECT i.warehouse_id, SUM(i.quantity) AS total_quantity
        FROM inventories i
        JOIN warehouses w ON i.warehouse_id = w.warehouse_id
        JOIN locations l ON w.location_id = l.location_id
        WHERE i.product_id = p_product_id
        AND l.country_id = p_country_code
        GROUP BY i.warehouse_id
        ORDER BY total_quantity DESC
    ) LOOP
        IF rec.total_quantity > 0 THEN
            v_warehouse_id := rec.warehouse_id;
            RETURN v_warehouse_id; -- Retorna el primer almacén con mayor cantidad
        END IF;
    END LOOP;

    RETURN -1; -- El producto existe pero no hay cantidad en ningún almacén del país
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        RETURN NULL;
END search_warehouse_for_product;

