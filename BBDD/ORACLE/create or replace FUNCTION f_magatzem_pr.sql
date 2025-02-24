create or replace FUNCTION f_magatzem_prod ( in_id_product products.product_id%type,
                                        in_id_country countries.country_id%type)
RETURN number IS
v_num number;
v_max number;
v_id  number;
BEGIN
    --comprovar producte si no existeix retornar null
    begin        
        select 1 into v_num
        from products p 
        where p.product_id=in_id_product;
    exception
        when no_data_found then return null;
    end;
    -- Si el producte existeix però no n’hi ha a cap magatzem del país RETURN -1.
    begin         
        select 1 into v_num
        from products p 
        join inventories i on p.PRODUCT_ID=i.PRODUCT_ID
        join WAREHOUSES w  on i.WAREHOUSE_ID=w.WAREHOUSE_ID
        join LOCATIONS l   on w.LOCATION_ID=l.LOCATION_ID
        where p.product_id=in_id_product 
        and l.COUNTRY_ID=in_id_country;    
    exception
        when no_data_found then return -1;
        when too_many_rows then null;
    end;
    -- Si el producte existeix al país llavors retornar el magatzem que en té més quantitat,
    -- RETURN WAREHOUSE_ID.
    -- 1era query per obtenir max
    select max(i.quantity) into v_max
    from products p 
    join inventories i on p.PRODUCT_ID=i.PRODUCT_ID
    join WAREHOUSES w  on i.WAREHOUSE_ID=w.WAREHOUSE_ID
    join LOCATIONS l   on w.LOCATION_ID=l.LOCATION_ID
    where p.product_id=in_id_product 
    and l.COUNTRY_ID=in_id_country;    
    --2ona query per obtenir el magatzem que té quantitat=max
    begin
        select w.WAREHOUSE_ID into v_id
        from products p 
        join inventories i on p.PRODUCT_ID=i.PRODUCT_ID
        join WAREHOUSES w  on i.WAREHOUSE_ID=w.WAREHOUSE_ID
        join LOCATIONS l   on w.LOCATION_ID=l.LOCATION_ID
        where p.product_id=in_id_product 
        and l.COUNTRY_ID=in_id_country     
        and i.quantity=v_max;
    EXCEPTION
        when too_many_rows then             
            select w.WAREHOUSE_ID into v_id
            from products p 
            join inventories i on p.PRODUCT_ID=i.PRODUCT_ID
            join WAREHOUSES w  on i.WAREHOUSE_ID=w.WAREHOUSE_ID
            join LOCATIONS l   on w.LOCATION_ID=l.LOCATION_ID
            where p.product_id=in_id_product 
            and l.COUNTRY_ID=in_id_country     
            and i.quantity=v_max
            and ROWNUM=1;
    end;
    return v_id;
exception
    when others then return null;
end;