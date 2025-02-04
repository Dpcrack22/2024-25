/* 1. Crear Taules de Base de Dades (3 punts)
Conceptos clave:
Sintaxis básica para crear tablas: */
 
CREATE TABLE nom_taula (
    nom_camp tipus_dada [restricció],
    ...
    PRIMARY KEY (nom_camp),
    FOREIGN KEY (nom_camp) REFERENCES altra_taula(camp_referenciat)
);
/*
Tipus de dades comuns:

    VARCHAR(n): Cadena de text de longitud variable.
    INT: Enter.
    BIGINT: Enter més gran.
    DATE: Data.
    DECIMAL(m, n): Números decimals amb precisió.
    BOOLEAN: Cert o fals.
    Restriccions:
    NOT NULL: El camp no pot ser buit.
    DEFAULT: Valor per defecte.
    CHECK: Condició que han de complir els valors.
    PRIMARY KEY: Clau primària (identificador únic de la fila).
    FOREIGN KEY: Clau forana (relació amb altres taules).
    Exemple:
    Crear una taula clients i una taula comandes amb relacions:
*/

CREATE TABLE clients (
    idclient INT PRIMARY KEY,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(100)
);

CREATE TABLE comandes (
    idcomanda INT PRIMARY KEY,
    data DATE NOT NULL,
    idclient INT,
    FOREIGN KEY (idclient) REFERENCES clients(idclient)
);

/* 2. Modificar Dades (UPDATE/INSERT/DELETE) (2 punts)
Operacions bàsiques: */

/* Insertar dades (INSERT): */
INSERT INTO nom_taula (camp1, camp2, ...) VALUES (valor1, valor2, ...);
INSERT INTO clients (idclient, nom, email) VALUES (1, 'Anna', 'anna@example.com');

/* Modificar dades (UPDATE): */
UPDATE nom_taula SET camp = valor WHERE condició;
UPDATE clients SET email = 'noucorreu@example.com' WHERE idclient = 1;

/* Eliminar dades (DELETE): */
DELETE FROM nom_taula WHERE condició;
DELETE FROM clients WHERE idclient = 1;


/* 3. Alterar Taules (1 punt)
Operacions bàsiques amb ALTER TABLE: */

/* Afegir una columna: */
ALTER TABLE nom_taula ADD nom_camp tipus_dada;
ALTER TABLE clients ADD telefon VARCHAR(15);


/* Eliminar una columna: */
ALTER TABLE nom_taula DROP COLUMN nom_camp;
ALTER TABLE clients DROP COLUMN telefon;

/* Modificar una columna: */
ALTER TABLE nom_taula MODIFY nom_camp nou_tipus_dada;
ALTER TABLE clients MODIFY email VARCHAR(150);

/* Afegir una clau forana: */
ALTER TABLE nom_taula ADD CONSTRAINT nom_clau FOREIGN KEY (camp) REFERENCES altra_taula(camp);
ALTER TABLE comandes ADD CONSTRAINT fk_client FOREIGN KEY (idclient) REFERENCES clients(idclient);


/* 4. Consultes a la Base de Dades (4 punts)
Operacions bàsiques amb SELECT: */

/* Filtrar dades amb WHERE: */
SELECT * FROM nom_taula WHERE condició;
SELECT * FROM clients WHERE email LIKE '%example.com';

/* Ordenar resultats amb ORDER BY */
SELECT * FROM nom_taula ORDER BY camp ASC/DESC;
SELECT * FROM clients ORDER BY nom ASC;

/* Agrupar dades amb GROUP BY: */
SELECT camp, COUNT(*) FROM nom_taula GROUP BY camp;
SELECT idclient, COUNT(*) FROM comandes GROUP BY idclient;

/* Unir taules amb JOIN: */
SELECT t1.camp1, t2.camp2
FROM taula1 t1
JOIN taula2 t2 ON t1.camp = t2.camp;

SELECT clients.nom, comandes.data
FROM clients
JOIN comandes ON clients.idclient = comandes.idclient;

/* Condicions amb funcions d'agregació: */
SELECT COUNT(*) FROM nom_taula WHERE condició;
SELECT COUNT(*) FROM comandes WHERE data > '2025-01-01';

/* Crear vistes: */
CREATE VIEW nom_vista AS SELECT ... FROM ... WHERE ...;
CREATE VIEW ClientsActius AS
SELECT nom, email FROM clients WHERE idclient IN (SELECT idclient FROM comandes);

/* 
Resum:
Crear taules: Saber definir estructures amb clau primària, forana, tipus de dades i restriccions.
Modificar dades: Saber inserir, actualitzar i eliminar registres.
Alterar taules: Afegir, modificar o eliminar columnes i crear restriccions.
Consultes: Utilitzar SELECT amb filtres (WHERE), agrupacions (GROUP BY), unions (JOIN), i crear vistes per dades específiques.
 */









 1. Representants de vendes (salesRepEmployeeNumber) que tenen mes de 6 clients.
Mostrar dades del representador de vendes: numero dempleat, nom, cognom i la quantitat de clients

2. Comandes dels clients del representatn de vendes 1370 (Gerard Hernandez) realitzades al 2005
Mostrar del client el seu nom i de la comanda (numero, data de la comanda i status)

3. Pagaments realitzats pels clients. Nomes aquells pagaments d'import(amount) superior a 55000
Mostrar nom del client, quantitat de pagament(superior a 55000) i suma total pagada ordenar per suma total pagada descendentment

4. Comandes ralitzades de productes del vendedor "Welly DieCast Productions" el primer semeste de 2003
Mostrar vendedor del producte (producVendor), nom del producte, quantitat demanada (quantityOrdered), preu unitat(priceEach) i data de la comanda
Ordenar per nom del producte i data de la comanda de la mes nova a la mes antiga

Ten la base de datos y azme lo siguiente:
CREATE DATABASE private_clinic_PereraDavid;

use private_clinic_PereraDavid;

CREATE TABLE  Appointment(
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT,
    SpecialistID INT,
    AppointmentDateTime DATETIME,
    Reason TEXT(30),
    Status ENUM("Scheduled","Completed" , "Canceled")
);

CREATE TABLE  Client(
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName Varchar(50),
    LastName Varchar(50),
    DateOfBirth Date,
    PhoneNumber Varchar(15),
    Email Varchar(100),
    Address TEXT
);
ALTER TABLE appointment ADD FOREIGN KEY (ClientID) REFERENCES client(ClientID);


CREATE TABLE  Specialist(
    SpecialistID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName Varchar(50),
    LastName Varchar(50),
    Specialy Varchar(100),
    PhoneNumber Varchar(15),
    Email Varchar(100)
);
ALTER TABLE appointment ADD FOREIGN KEY (SpecialistID) REFERENCES specialist(SpecialistID);

CREATE TABLE  Invoice(
    invoiceID INT AUTO_INCREMENT PRIMARY KEY,
    AppointmentID INT,
    IssueDate DATE,
    TotalAmount Decimal(10,2),
    PaidStatus ENUM("Unpaid", "Paid", "Partial"),
    FOREIGN KEY (AppointmentID) REFERENCES appointment(AppointmentID)
);

CREATE TABLE Intervention (
    InterventionID INT AUTO_INCREMENT PRIMARY KEY,
    AppointmentID INT,
    Description TEXT,
    FOREIGN KEY (AppointmentID) REFERENCES appointment(AppointmentID)

);


/* 2 */
Crea una cita pels clients anteriors amb la especialista cardiologica recorda que no es poden fer servir les id per el WHERE
( los clientes de antes se llaman Caroline Perry i William Green)
esto en una sola queri o linia sabes como hacerlo ?

/* 3 */
Elimina els clients q no tinguin cap cita


/* 4 */
Fent servir sentencies alter feu les modificaccions seguents a les taules de la bd
Afegir una columna nova a la intervencion(intervention) La columna a afegir es diu scheduledDate, data planificada, no es obligatoria
Despres de crearla fer una sentencia update per actualizarla, el valor sheduleDate es el del dia posterior a la cita amb la que esta lligada

-- Buscar el ID del especialista en cardiología
SELECT SpecialistID FROM Specialist WHERE Specialy = 'Cardiology';

-- Buscar los IDs de los clientes Caroline Perry y William Green
SELECT ClientID FROM Client WHERE FirstName = 'Caroline' AND LastName = 'Perry';
SELECT ClientID FROM Client WHERE FirstName = 'William' AND LastName = 'Green';

-- Crear las citas
INSERT INTO Appointment (ClientID, SpecialistID, AppointmentDateTime, Reason, Status)
SELECT c.ClientID, s.SpecialistID, '2025-02-01 10:00:00', 'General checkup', 'Scheduled'
FROM Client c, Specialist s
WHERE c.FirstName = 'Caroline' AND c.LastName = 'Perry'
AND s.Specialy = 'Cardiology';

INSERT INTO Appointment (ClientID, SpecialistID, AppointmentDateTime, Reason, Status)
SELECT c.ClientID, s.SpecialistID, '2025-02-01 11:00:00', 'General checkup', 'Scheduled'
FROM Client c, Specialist s
WHERE c.FirstName = 'William' AND c.LastName = 'Green'
AND s.Specialy = 'Cardiology';
