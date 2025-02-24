CREATE OR REPLACE FUNCTION search_customer_for_product (
    p_product_id IN NUMBER,
    p_start_date IN DATE,
    p_end_date IN DATE
) RETURN NUMBER IS
    v_customer_id NUMBER;
    v_order_quantity NUMBER;
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

    FOR rec IN (
        SELECT o.customer_id, SUM(oi.quantity) AS total_quantity
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        WHERE oi.product_id = p_product_id
        AND o.order_date BETWEEN p_start_date AND p_end_date
        GROUP BY o.customer_id
        ORDER BY total_quantity DESC
    ) LOOP
        IF rec.total_quantity > 0 THEN
            v_customer_id := rec.customer_id;
            RETURN v_customer_id; -- Retorna el primer cliente con más cantidad pedida
        END IF;
    END LOOP;

    RETURN -1; -- No se han encontrado pedidos para este producto en el intervalo de fechas
EXCEPTION
    WHEN OTHERS THEN
        DBMS_OUTPUT.PUT_LINE('Error: ' || SQLERRM);
        RETURN NULL;
END search_customer_for_product;
