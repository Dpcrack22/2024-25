alter session set container = FREEPDB1;
create User botiga identified by botiga;
grant connect to botiga;
grant create session to botiga;
grant unlimited tablespace to botiga;
grant dba to botiga;
grant create view to botiga;
commit;