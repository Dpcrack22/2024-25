id_emp number;
nom_emp varchar2(50);
PROCEDURE findemp(id iN number, nameemp OUT varchar2) IS
begin
    select first_name|| ' ' || last_name as name_emp
        into nameemp
    from employees
    where employee_id = id;
end;
begin
   id_emp:=100;
   findemp(id_emp,nom_emp);
   dbms_output.put_line(nom_emp);
   id_emp:=101;
   findemp(id_emp,nom_emp);
   dbms_output.put_line(nom_emp);
   id_emp:=102;
   findemp(id_emp,nom_emp);
   dbms_output.put_line(nom_emp);
end;