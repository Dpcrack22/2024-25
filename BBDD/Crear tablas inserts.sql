/* 1. Crear Tablas (CREATE TABLE)
Las tablas son la base de las bases de datos. Para crearlas, usamos el comando CREATE TABLE.
 Por ejemplo: */
 CREATE TABLE producto (
    codigo INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DOUBLE NOT NULL,
    codigo_fabricante INT UNSIGNED NOT NULL,
    FOREIGN KEY (codigo_fabricante) REFERENCES fabricante(codigo)
);

/* codigo: Es una columna con un número único para cada producto. 
Es clave primaria (PRIMARY KEY), lo que significa que no puede repetirse.
nombre: Un campo de texto (hasta 100 caracteres) que no puede ser nulo (NOT NULL).
precio: Es un número decimal (puede incluir centavos).
codigo_fabricante: Hace referencia a otra tabla (fabricante) y se asegura de que no se pueda 
insertar un valor que no exista en dicha tabla, gracias a la clave foránea (FOREIGN KEY). */


/* 2. Modificar Tablas (ALTER TABLE)
Si ya tienes una tabla pero necesitas cambiar su estructura, usas ALTER TABLE. Por ejemplo: */

/* Añadir una columna: 
Esto añade una nueva columna llamada stock con un valor predeterminado de 0. */
ALTER TABLE producto ADD COLUMN stock INT DEFAULT 0;

/* Modificar una columna existente:
Esto cambia la columna precio para que sea un número decimal con dos decimales. */
ALTER TABLE producto MODIFY COLUMN precio DECIMAL(10, 2);

/* Eliminar una columna: */
ALTER TABLE producto DROP COLUMN stock;


/* 3. Insertar Datos (INSERT)
Usamos INSERT para añadir datos a una tabla. Por ejemplo: 
Esto añade un producto llamado "Laptop" con un precio de 1200.50 y un fabricante con código 1.*/
INSERT INTO producto (nombre, precio, codigo_fabricante)
VALUES ('Laptop', 1200.50, 1);

/* 4. Actualizar Datos (UPDATE)
Si necesitas cambiar datos existentes, usas UPDATE. Ejemplo:
Esto incrementa un 10% el precio de todos los productos del fabricante con código 2. */
UPDATE producto
SET precio = precio * 1.10
WHERE codigo_fabricante = 2;

/* 5. Eliminar Datos (DELETE)
Para eliminar datos, usas DELETE. Ejemplo:
Esto elimina el producto con código 5. ¡Cuidado! 
Si no usas WHERE, borrarás todos los datos de la tabla. */
DELETE FROM producto
WHERE codigo = 5;

/* 6. Crear Vistas (CREATE VIEW)
Una vista es una consulta guardada, como una "ventana" a los datos que quieres ver. 
Por ejemplo:
Esto crea una vista llamada vista_productos que muestra solo los productos con precio mayor 
a 100. Después puedes usarla como si fuera una tabla: */
CREATE VIEW vista_productos AS
SELECT nombre, precio
FROM producto
WHERE precio > 100;


/* Errores comunes al trabajar con tablas
Claves primarias duplicadas: Si intentas insertar un valor en una columna clave
primaria que ya existe, obtendrás un error.

Violación de claves foráneas: No puedes insertar o actualizar un valor en una 
columna que referencia otra tabla, si ese valor no existe en la tabla referenciada.

Violación de restricciones NOT NULL: Si intentas dejar un campo obligatorio vacío, 
obtendrás un error. */

/* 7. Ejemplo Práctico
Supongamos que estás trabajando con una base de datos de una tienda. 
Primero, creamos las tablas necesarias: */

CREATE TABLE tienda (
    id_tienda INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    ciudad VARCHAR(50)
);

CREATE TABLE producto (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

CREATE TABLE venta (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_tienda INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    FOREIGN KEY (id_tienda) REFERENCES tienda(id_tienda),
    FOREIGN KEY (id_producto) REFERENCES producto(id_producto)
);

/* Insertar datos: */
INSERT INTO tienda (nombre, ciudad) VALUES ('Tienda A', 'Barcelona');
INSERT INTO producto (nombre, precio) VALUES ('Producto X', 25.00);
INSERT INTO venta (id_tienda, id_producto, cantidad) VALUES (1, 1, 5);

/* Actualizar datos: */
UPDATE producto SET precio = precio * 1.10 WHERE id_producto = 1;

/* Eliminar datos: */
DELETE FROM venta WHERE id_venta = 1;

/* Crear una vista: */
CREATE VIEW ventas_totales AS
SELECT t.nombre AS tienda, p.nombre AS producto, v.cantidad, (p.precio * v.cantidad) AS total
FROM venta v
JOIN tienda t ON v.id_tienda = t.id_tienda
JOIN producto p ON v.id_producto = p.id_producto;

/* Consultar la vista: */
SELECT * FROM ventas_totales;





-- 1. Copiar estructura y datos de una tabla (Estructura y Datos)
-- Este comando crea una nueva tabla 'nueva_tabla' con la misma estructura
-- y los mismos datos que 'tabla_original'.
CREATE TABLE nueva_tabla AS
SELECT * FROM tabla_original;

-- Ejemplo:
-- CREATE TABLE producto_copy AS
-- SELECT * FROM producto;


-- 2. Copiar solo la estructura (sin los datos)
-- Este comando crea una nueva tabla 'nueva_tabla' con la misma estructura
-- que 'tabla_original', pero sin copiar los datos.
CREATE TABLE nueva_tabla LIKE tabla_original;

-- Ejemplo:
-- CREATE TABLE producto_copy LIKE producto;


-- 3. Copiar solo los datos (sin la estructura)
-- Si ya tienes una tabla creada y solo necesitas copiar los datos de una tabla
-- a otra, usa el siguiente comando.
-- Asegúrate de que las tablas tengan la misma estructura.
INSERT INTO nueva_tabla SELECT * FROM tabla_original;

-- Ejemplo:
-- INSERT INTO producto_copy SELECT * FROM producto;


-- 4. Copiar con condiciones (solo algunos registros)
-- Si solo deseas copiar parte de los registros de la tabla original a la nueva tabla,
-- puedes agregar una cláusula WHERE para aplicar condiciones.
INSERT INTO nueva_tabla SELECT * FROM tabla_original WHERE precio > 100;

-- Ejemplo:
-- INSERT INTO producto_copy SELECT * FROM producto WHERE precio > 100;




/* VARCHAR y CHAR son para texto, donde VARCHAR es de longitud variable y CHAR es de longitud fija.
INT, BIGINT, SMALLINT son para números enteros.
DECIMAL y FLOAT/DOUBLE son para números con decimales (usados según la precisión requerida).
DATE, DATETIME, TIMESTAMP y TIME son para fechas y horas.
BOOLEAN se usa para valores lógicos (verdadero/falso).
BLOB es para datos binarios y TEXT es para textos largos. */


/* ¿Qué es una clave foránea (Foreign Key)?
Una clave foránea es una columna (o conjunto de columnas) en una tabla que hace referencia a la clave primaria de otra tabla. 
Este mecanismo garantiza que los datos en la tabla que contiene la clave foránea sean consistentes con los datos en la tabla referenciada.

Ejemplo Básico de Relación de Tablas
Supongamos que tienes dos tablas: clientes y pedidos.

En la tabla clientes tendrás información sobre los clientes (por ejemplo, su ID, nombre, etc.).
En la tabla pedidos tendrás información sobre los pedidos realizados, y cada pedido debe estar asociado a un cliente.
La relación entre estas dos tablas se hará a través de la clave foránea.

Paso 1: Crear la tabla principal (la que tendrá la clave primaria)
Primero, creamos la tabla clientes. Esta tabla tendrá una clave primaria, que será el id_cliente. */
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,  -- Clave primaria
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL
);

/* Paso 2: Crear la tabla secundaria (la que tendrá la clave foránea)
Luego, creamos la tabla pedidos, donde cada pedido estará vinculado a un cliente a través de la clave foránea id_cliente. */
CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,   -- Clave primaria
    id_cliente INT,                             -- Clave foránea
    fecha DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)  -- Estableciendo la relación
);

/* id_cliente INT: Es la columna en la tabla pedidos que almacenará el ID del cliente.
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente): Esta es la clave foránea que indica que la columna id_cliente en la tabla pedidos hace referencia a la columna id_cliente en la tabla clientes. 
Esto asegura que solo se puedan insertar en la tabla pedidos valores de id_cliente que existan en la tabla clientes. 

¿Cómo funciona la integridad referencial con claves foráneas?
Al usar claves foráneas, MySQL asegura que:

No puedes insertar un valor en pedidos.id_cliente que no exista en clientes.id_cliente.
Si intentas borrar un cliente de la tabla clientes y ese cliente tiene pedidos, MySQL te impedirá borrar el cliente, a menos que tomes medidas adicionales (como eliminar los pedidos asociados).
Acciones de Integridad Referencial
Cuando trabajas con claves foráneas, puedes definir cómo deben comportarse las relaciones cuando realices operaciones de UPDATE o DELETE. Las acciones más comunes son:

CASCADE: Si eliminas o actualizas un registro en la tabla referenciada (por ejemplo, clientes), 
los registros correspondientes en la tabla que contiene la clave foránea (pedidos) también se actualizarán o eliminarán automáticamente.*/
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE CASCADE ON UPDATE CASCADE;

/* SET NULL: Si eliminas o actualizas un registro en la tabla referenciada, el valor de la clave foránea en la tabla hija se pondrá a NULL. */
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE SET NULL ON UPDATE SET NULL;


/* RESTRICT: No permite la eliminación ni la actualización del registro referenciado si hay registros dependientes en la tabla hija. 
Es el comportamiento predeterminado si no se especifica ninguna acción. */
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE RESTRICT ON UPDATE RESTRICT;

/* NO ACTION: Similar a RESTRICT, pero se verifica la restricción de forma diferida (después de que la transacción se complete). */
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente) ON DELETE NO ACTION ON UPDATE NO ACTION;



-- Crear la base de dades, si no existeix
CREATE DATABASE IF NOT EXISTS prestecLlibres;
USE prestecLlibres;

-- Crear la taula soci amb totes les restriccions especificades
CREATE TABLE soci (
    idsoci VARCHAR(5) PRIMARY KEY,  -- Identificador únic del soci
    Nom VARCHAR(20) NOT NULL,  -- Nom del soci (no pot ser nul)
    cognoms VARCHAR(40),  -- Cognoms del soci
    dni VARCHAR(9),  -- DNI del soci
    telefon VARCHAR(9),  -- Telèfon del soci (pot ser nul)
    email VARCHAR(20),  -- Email del soci
    CONSTRAINT id_nom_ck CHECK (Nom = UPPER(Nom))  -- El nom s'ha de guardar en majúscules
);

-- Crear la taula llibre amb les restriccions
CREATE TABLE llibre (
    idllibre VARCHAR(10) PRIMARY KEY,  -- Identificador únic del llibre
    isbn VARCHAR(10) NOT NULL,  -- ISBN del llibre (no pot ser nul)
    titol VARCHAR(40),  -- Títol del llibre
    autor VARCHAR(40)  -- Autor del llibre
);

-- Crear la taula préstec amb les relacions i restriccions indicades
CREATE TABLE prestec (
    idprestec BIGINT PRIMARY KEY,  -- Identificador únic del préstec
    idllibre VARCHAR(10),  -- Fa referència a la taula llibre
    dataPres DATE,  -- Data d'inici del préstec
    dataRet DATE,  -- Data de retorn del llibre
    idsoci VARCHAR(5),  -- Fa referència a la taula soci
    estat VARCHAR(1) CHECK (estat = 'O' OR estat = 'T'),  -- Estat del préstec ('O' per obert, 'T' per tancat)
    penalitzacio INT DEFAULT 0 CHECK (penalitzacio >= 0),  -- Penalització (ha de ser >= 0 i per defecte 0)
    CONSTRAINT llibre_fk FOREIGN KEY (idllibre) REFERENCES llibre (idllibre),  -- Clau forana que fa referència a llibre
    CONSTRAINT soci_fk FOREIGN KEY (idsoci) REFERENCES soci (idsoci),  -- Clau forana que fa referència a soci
    CONSTRAINT penalitzacio_ck CHECK (penalitzacio >= 0)  -- La penalització ha de ser >= 0
);

-- b. Eliminar la columna telefon de la taula soci
ALTER TABLE soci
DROP COLUMN telefon;

-- c. Tornar a crear la columna telefon a la taula soci
ALTER TABLE soci
ADD COLUMN telefon VARCHAR(9);

-- d. Inserir 4 noves files a cada taula (en ordre correcte)
-- Inserir dades a la taula soci
INSERT INTO soci (idsoci, Nom, cognoms, dni, email, telefon)
VALUES ('1', 'ANNA', 'Perez', '123456789', 'ana@gmail.com', '989898987');

INSERT INTO soci (idsoci, Nom, cognoms, dni, email, telefon)
VALUES ('2', 'JOAN', 'Lopez', '123456781', 'joan@gmail.com', NULL);

INSERT INTO soci (idsoci, Nom, cognoms, dni, email, telefon)
VALUES ('3', 'MARC', 'Garcia', '123456782', 'marc@gmail.com', NULL);

INSERT INTO soci (idsoci, Nom, cognoms, dni, email, telefon)
VALUES ('4', 'SONIA', 'Jurado', '123456783', 'sonia@gmail.com', NULL);

-- Inserir dades a la taula llibre
INSERT INTO llibre (idllibre, isbn, titol, autor)
VALUES ('A', '12345678', 'Mysql', 'Joan');

INSERT INTO llibre (idllibre, isbn, titol, autor)
VALUES ('B', '12345682', 'Mysql2', 'Pere');

INSERT INTO llibre (idllibre, isbn, titol, autor)
VALUES ('C', '12343567', 'Mysql3', 'Claudia');

INSERT INTO llibre (idllibre, isbn, titol, autor)
VALUES ('D', '12345679', 'Mysql4', 'Manel');

-- Inserir dades a la taula préstec
INSERT INTO prestec (idprestec, idllibre, dataPres, dataRet, idsoci, estat, penalitzacio)
VALUES (10, 'A', '2016-01-01', NULL, '1', 'O', 1);

INSERT INTO prestec (idprestec, idllibre, dataPres, dataRet, idsoci, estat, penalitzacio)
VALUES (20, 'B', '2016-01-02', NULL, '1', 'T', 3);

INSERT INTO prestec (idprestec, idllibre, dataPres, dataRet, idsoci, estat, penalitzacio)
VALUES (30, 'C', '2016-01-03', NULL, '1', 'O', 3);

INSERT INTO prestec (idprestec, idllibre, dataPres, dataRet, idsoci, estat, penalitzacio)
VALUES (40, 'D', '2016-01-04', NULL, '1', 'T', 4);

-- e. Esborrar el llibre de títol 'manual mysql' (segurament no existeix)
DELETE FROM llibre WHERE titol = 'manual mysql';

-- f. Actualitzar el valor de telefon a 1 en tots els socis que no tinguin telèfon
UPDATE soci
SET telefon = '1'
WHERE telefon IS NULL;

-- g. Esborrar el contingut de la taula llibre (no es pot esborrar perquè hi ha referències a aquesta taula des de prestec)
-- Aquesta acció fallaria si no es fa amb les opcions correctes de referència
-- Podem fer un TRUNCATE per esborrar totes les dades, però només si les restriccions permeten la seva eliminació.
-- De totes maneres, no es pot esborrar la taula llibre si hi ha dades referenciades des de préstec
DELETE FROM llibre;  -- Això pot fallar si hi ha restriccions de clau forana.
-- o
TRUNCATE TABLE llibre; -- No es pot fer perquè la taula està sent referenciada per la taula préstec.

-- h. Crear una vista anomenada SocisAmbPrestec amb l'email dels socis que tinguin préstecs per retornar
CREATE VIEW socisAmbPrestec AS
SELECT DISTINCT email
FROM soci, prestec
WHERE soci.idsoci = prestec.idsoci AND prestec.dataret IS NULL;


/* Explicació dels passos:
Creació de les taules: Primer es crea la base de dades prestecLlibres i les taules soci, llibre, i prestec amb les restriccions que es demanen, com les clau primàries, les claus foranes i les 
condicions de validació (per exemple, el nom en majúscules o la penalització no menor que 0).
Eliminació i afegit de columnes: Es realitza l'eliminació de la columna telefon i la seva posterior reincorporació a la taula soci.
Inserir dades: Inserim dades d'exemple a les taules soci, llibre i prestec en l'ordre adequat per respectar les relacions de clau forana.
Esborrar registre específic: Intentem esborrar un registre de la taula llibre que no existeix (per exemple, un llibre amb títol "manual mysql").
Actualització de dades: Actualitzem la columna telefon amb el valor "1" per aquells socis que no tenen telèfon assignat.
Esborrar contingut de la taula llibre: No es pot esborrar el contingut de la taula llibre perquè està referenciada per la taula prestec, la qual cosa genera una restricció d'integritat.
Creació de la vista: Finalment, creem una vista SocisAmbPrestec que retorna els correus electrònics dels socis amb préstecs oberts (on dataret és NULL). */