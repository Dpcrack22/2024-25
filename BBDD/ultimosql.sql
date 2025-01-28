1. Crear Taules de Base de Dades (3 punts)
Conceptos clave:
Sintaxis básica para crear tablas:



CREATE TABLE nom_taula (
    nom_camp tipus_dada [restricció],
    ...
    PRIMARY KEY (nom_camp),
    FOREIGN KEY (nom_camp) REFERENCES altra_taula(camp_referenciat)
);
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
2. r Dades (UPDATE/INSERT/DELETE) (2 punts)
Operacions bàsiques:
Insertar dades (INSERT):
INSERT INTO nom_taula (camp1, camp2, ...) VALUES (valor1, valor2, ...);

Exemple:
INSERT INTO clients (idclient, nom, email) VALUES (1, 'Anna', 'anna@example.com');

r dades (UPDATE):
UPDATE nom_taula SET camp = valor WHERE condició;

Exemple:
UPDATE clients SET email = 'noucorreu@example.com' WHERE idclient = 1;

Eliminar dades (DELETE):
DELETE FROM nom_taula WHERE condició;ç

Exemple:
DELETE FROM clients WHERE idclient = 1;

3. Alterar Taules (1 punt)
Operacions bàsiques amb ALTER TABLE:
Afegir una columna:

ALTER TABLE nom_taula ADD nom_camp tipus_dada;
Exemple:

ALTER TABLE clients ADD telefon VARCHAR(15);
Eliminar una columna:

ALTER TABLE nom_taula DROP COLUMN nom_camp;
Exemple:



ALTER TABLE clients DROP COLUMN telefon;
r una columna:




ALTER TABLE nom_taula MODIFY nom_camp nou_tipus_dada;
Exemple:



ALTER TABLE clients MODIFY email VARCHAR(150);
Afegir una clau forana:




ALTER TABLE nom_taula ADD CONSTRAINT nom_clau FOREIGN KEY (camp) REFERENCES altra_taula(camp);
Exemple:



ALTER TABLE comandes ADD CONSTRAINT fk_client FOREIGN KEY (idclient) REFERENCES clients(idclient);
4. Consultes a la Base de Dades (4 punts)
Operacions bàsiques amb SELECT:
Seleccionar totes les dades d'una taula:




SELECT * FROM nom_taula;
Filtrar dades amb WHERE:




SELECT * FROM nom_taula WHERE condició;
Exemple:



SELECT * FROM clients WHERE email LIKE '%example.com';
Ordenar resultats amb ORDER BY:




SELECT * FROM nom_taula ORDER BY camp ASC/DESC;
Exemple:



SELECT * FROM clients ORDER BY nom ASC;
Agrupar dades amb GROUP BY:




SELECT camp, COUNT(*) FROM nom_taula GROUP BY camp;
Exemple:



SELECT idclient, COUNT(*) FROM comandes GROUP BY idclient;
Unir taules amb JOIN:




SELECT t1.camp1, t2.camp2
FROM taula1 t1
JOIN taula2 t2 ON t1.camp = t2.camp;
Exemple:



SELECT clients.nom, comandes.data
FROM clients
JOIN comandes ON clients.idclient = comandes.idclient;
Condicions amb funcions d'agregació:

Comptar files:



SELECT COUNT(*) FROM nom_taula WHERE condició;
Exemple:



SELECT COUNT(*) FROM comandes WHERE data > '2025-01-01';
Crear vistes:




CREATE VIEW nom_vista AS SELECT ... FROM ... WHERE ...;
Exemple:



CREATE VIEW ClientsActius AS
SELECT nom, email FROM clients WHERE idclient IN (SELECT idclient FROM comandes);
Resum:
Crear taules: Saber definir estructures amb clau primària, forana, tipus de dades i restriccions.
r dades: Saber inserir, actualitzar i eliminar registres.
Alterar taules: Afegir, r o eliminar columnes i crear restriccions.
Consultes: Utilitzar SELECT amb filtres (WHERE), agrupacions (GROUP BY), unions (JOIN), i crear vistes per dades específiques.