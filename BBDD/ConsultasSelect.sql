/*Ejercicio 1
Lista los nombres de los clientes que tienen representantes de ventas cuyo trabajo es
"Sales Rep" y que están ubicados en países donde el nombre del país comienza 
con la letra "C". Ordena los resultados alfabéticamente por el nombre del cliente.*/

use CustProd;
SELECT 
    c.customerName, c.salesRepEmployeeNumber, e.jobTitle, o.city
FROM
    customers c
        JOIN
    employees e ON e.employeeNumber = c.salesRepEmployeeNumber
        JOIN
    offices o ON o.officeCode = e.officeCode
WHERE
    e.jobTitle = 'Sales Rep'
        AND o.city = 'C*'
GROUP BY c.customerName asc;

/* Errores principales son el AND o.city = 'C*' que seria AND o.city Like 'C%' y en el "grup by" que es 
"order by" */

use CustProd;
SELECT 
    c.customerName, c.salesRepEmployeeNumber, e.jobTitle, o.city
FROM
    customers c
        JOIN
    employees e ON e.employeeNumber = c.salesRepEmployeeNumber
        JOIN
    offices o ON o.officeCode = e.officeCode
WHERE
    e.jobTitle = 'Sales Rep'
        AND o.city Like 'C%'
order by c.customerName asc


/* Ejercicio 2:
Muestra el nombre de los clientes, el número total de pedidos realizados por cada 
cliente y la cantidad total de productos pedidos. 
Ordena los resultados de mayor a menor por la cantidad total de productos pedidos.

Pistas:

Usa las tablas customers, orders, y orderdetails.
Necesitarás hacer un JOIN para relacionar las tablas.
Agrupa los resultados por cliente para obtener el número total de pedidos y productos. */

use custprod;
SELECT 
    c.customerName, o.orderNumber, od.quantityOrdered
FROM
    customers c
        JOIN
    orders o ON o.customerNumber = c.CustomerNumber
        JOIN
    orderdetails od ON od.orderNumber = o.orderNumber
GROUP BY o.orderNumber
ORDER BY od.quantityOrdered

/* Uso incorrecto de GROUP BY 
GROUP BY debería agrupar por el cliente (c.customerName) en este caso,
 porque estás calculando el total de pedidos y productos por cliente. 
 Actualmente está agrupando por o.orderNumber, lo cual no es lo que pedimos.

 Falta de agregación para contar pedidos y sumar productos:
Cuando usas GROUP BY, debes aplicar funciones de agregación como COUNT() y SUM() 
para obtener totales, ya que od.quantityOrdered no puede aparecer directamente sin 
una función de agregación.

Orden incorrecto en ORDER BY:
Debemos ordenar por la suma total de productos pedidos (SUM(od.quantityOrdered)) en lugar 
de od.quantityOrdered
*/
SELECT 
    c.customerName, 
    COUNT(o.orderNumber) AS total_orders, 
    SUM(od.quantityOrdered) AS total_products
FROM
    customers c
        JOIN
    orders o ON o.customerNumber = c.customerNumber
        JOIN
    orderdetails od ON od.orderNumber = o.orderNumber
GROUP BY c.customerName
ORDER BY total_products DESC;

/* Ejercicio 3:
Muestra los nombres de los productos que han sido comprados por clientes en Germany, 
junto con la cantidad total ordenada de cada producto. Ordena los resultados de mayor
a menor según la cantidad total ordenada.

Pistas:

Usa las tablas customers, orders, orderdetails y products.
Necesitarás hacer varios JOINs para conectar las tablas.
Usa SUM() para calcular la cantidad total ordenada por producto.
Agrupa por el nombre del producto. */

use custprod;
SELECT 
    p.productName, od.quantityOrdered
FROM
    products p
        JOIN
    orderdetails od ON od.productCode = p.productCode
        JOIN
    orders o ON o.orderNumber = od.orderNumber
        JOIN
    customers c ON o.customerNumber = c.customerNumber
WHERE
    c.city = 'Germany'
ORDER BY od.quantityOrdered DESC

/* Errores en la consulta:
Condición incorrecta en WHERE:

c.city = 'Germany' está mal, porque "Germany" no es una ciudad, sino un país.
Debes usar c.country = 'Germany'.
Falta de agregación para sumar productos:

od.quantityOrdered debe ser sumado con SUM(od.quantityOrdered) porque queremos la cantidad 
total de productos vendidos por producto.
Si no agregas una función de agregación cuando usas GROUP BY, MySQL dará un error.
Falta de GROUP BY:

Debemos agrupar por p.productName para obtener la cantidad total ordenada por cada producto.
 */

SELECT 
    p.productName, 
    SUM(od.quantityOrdered) AS total_quantity
FROM
    products p
        JOIN
    orderdetails od ON od.productCode = p.productCode
        JOIN
    orders o ON o.orderNumber = od.orderNumber
        JOIN
    customers c ON o.customerNumber = c.customerNumber
WHERE
    c.country = 'Germany'
GROUP BY p.productName
ORDER BY total_quantity DESC;


/* Ejercicio 4:
Muestra los nombres de los empleados, junto con la cantidad total de clientes que tienen
asignados como representantes de ventas.
Ordena los resultados de mayor a menor según la cantidad total de clientes.

Pistas:

Usa las tablas employees y customers.
Relaciónalas usando salesRepEmployeeNumber.
Usa COUNT() para contar la cantidad de clientes por empleado.
Agrupa los resultados por el nombre del empleado.
 */

use custprod;
SELECT 
    e.firstName, COUNT(c.customerName) as totalClients
FROM
    employees e
        JOIN
    customers c ON c.salesRepEmployeeNumber = e.employeeNumber 
    group by e.firstName
    order by totalClients desc


/* Si dos empleados tienen el mismo firstName, tu consulta los combinará como si fueran
la misma persona. Para evitar esto, agrupa por e.employeeNumber en lugar de e.firstName,
pero aún mostrando el nombre: */

SELECT 
    e.firstName, e.lastName, COUNT(c.customerNumber) AS totalClients
FROM
    employees e
        JOIN
    customers c ON c.salesRepEmployeeNumber = e.employeeNumber 
GROUP BY e.employeeNumber
ORDER BY totalClients DESC;



/* Ejercicio 5:
Obtén los nombres de los clientes, el número total de productos diferentes que han pedido y
el total de unidades pedidas por cada cliente.
Ordena los resultados por el total de unidades pedidas en orden descendente.

Pistas:

Usa las tablas customers, orders, orderdetails y products.
Relaciona las tablas usando las claves customerNumber, orderNumber y productCode.
Usa COUNT(DISTINCT) para obtener el número de productos diferentes pedidos.
Usa SUM() para calcular el total de unidades pedidas.
Agrupa por el nombre del cliente.
 */

SELECT 
    c.customerName, 
    COUNT(DISTINCT p.productCode) AS total_different_products, 
    SUM(od.quantityOrdered) AS total_units_ordered
FROM
    customers c
        JOIN
    orders o ON c.customerNumber = o.customerNumber
        JOIN
    orderdetails od ON o.orderNumber = od.orderNumber
        JOIN
    products p ON od.productCode = p.productCode
GROUP BY 
    c.customerName
ORDER BY 
    total_units_ordered DESC;