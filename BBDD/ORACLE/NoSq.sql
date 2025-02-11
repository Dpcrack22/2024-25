/*Augmenta el sou del treballador segons el seu departament
- dept < 50 augment 20%
- dept >=50 i < 100 augment 30%
- dept >= 100 augment 25%
mostrar sou del treballador abans i despres de l'increment de sou
buscar un treballador per a cadascun dels 3 casos possibles
*/
declare
  v_deptid  employees.department_id%type;
  v_salary  employees.salary%type;
  v_new_salary  employees.salary%type;
  v_emp     employees.EMPLOYEE_ID%TYPE;
  procedure find_emp (v_emp in employees.EMPLOYEE_ID%TYPE,
                    v_deptid out employees.department_id%type,
                    v_salary out employees.salary%type   ) is
   begin
        select department_id,salary
        into v_deptid,v_salary
        from employees
        where EMPLOYEE_ID=v_emp;
        DBMS_OUTPUT.PUT_LINE(v_emp||' '||nvl(v_deptid,-1)||' '
										||nvl(v_salary,0));
   end;
   procedure update_emp (v_emp in employees.EMPLOYEE_ID%TYPE,
                        v_deptid in employees.department_id%type   ,
                        v_salary in employees.salary%type   ,
                        v_new_salary out employees.salary%type   )  is
   begin
        if v_deptid < 50 THEN
                v_new_salary:=v_salary*1.20;
        elsif v_deptid >= 50 and v_deptid < 100 then
                v_new_salary:=v_salary*1.30;
        else 
                v_new_salary:=v_salary*1.25;
        end if;
        update EMPLOYEES
        set salary=v_new_salary
        where EMPLOYEE_ID=v_emp;
        DBMS_OUTPUT.PUT_LINE(v_emp||' '||nvl(v_deptid,-1)||' '
										||nvl(v_salary,0)||' '
										||nvl(v_new_salary,0));
   end;
begin
    v_emp:=200; -- treballador del department 30
    find_emp(v_emp,v_deptid,v_salary);
    update_emp(v_emp,v_deptid,v_salary,v_new_salary);
    v_emp:=120; -- treballador del departament 90
    find_emp(v_emp,v_deptid,v_salary);
    update_emp(v_emp,v_deptid,v_salary,v_new_salary);
    v_emp:=108; -- treballador del departament 100
    find_emp(v_emp,v_deptid,v_salary);
    update_emp(v_emp,v_deptid,v_salary,v_new_salary);
end;