create or replace function f2_finddeptcom (p_id number)
return employees.COMMISSION_PCT%type
is
v_count number;
v_max employees.COMMISSION_PCT%type;
begin
    -- si el parametre es null retornar null
    if p_id is null THEN
        return null;
    end if;
    select count(*) into v_count
    from DEPARTMENTS
    where DEPARTMENT_id=p_id;    
    -- si el departament no existeix retornar null
    if v_count = 1 THEN 
        v_max:=0;
        select count(*) into v_count
        from EMPLOYEES
        where DEPARTMENT_id=p_id;  
        -- si el departament te treballadors cercar max comm
        if v_count>=1 THEN
            select max(COMMISSION_PCT) into v_max
            from EMPLOYEES
            where DEPARTMENT_id=p_id;
        end if;
        return v_max;
    ELSE
        return null;
    end if;
end;