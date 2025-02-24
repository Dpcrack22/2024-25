import oracledb
import xml.etree.ElementTree as ET
from lxml import etree

# Path to the XSD file
xsd_file = "employees.xsd"

# Set up connection parameters
username = 'hr'
password = 'oracle'
host = 'localhost'
port = '1521'
service_name = 'freepdb1' 

# Construct DSN
dsn = oracledb.makedsn(host, port, service_name=service_name)

# Establish a connection to the Oracle database
try:
    connection = oracledb.connect(user=username, password=password, dsn=dsn)
    print("Connected to Oracle Database!")
    
    # Create a cursor
    cursor = connection.cursor()

    # Query to fetch employee data
    query = """
        SELECT  employee_id, 
                first_name, last_name, email, phone_number, 
                to_char(hire_date,'yyyy-mm-dd') as hire_date, 
                job_id, salary, 
                nvl(manager_id,-1) as manager_id, 
                nvl(department_id,-1) as department_id
        FROM employees
    """
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()    

    # Get column names from cursor description
    columns = [col[0].lower() for col in cursor.description]

    # Create the root XML element
    root = ET.Element("Employees")

    # Transform data into XML structure
    for row in rows:
        employee_elem = ET.SubElement(root, "Employee")
        for i in range(len(columns)):
            child = ET.SubElement(employee_elem, columns[i])
            child.text = str(row[i]) if row[i] is not None else ""

    # Convert the XML structure to a string
    xml_data = ET.tostring(root, encoding="utf-8", xml_declaration=True)

    # Validate XML against XSD
    with open(xsd_file, "r") as xsd:
        schema_root = etree.XML(xsd.read())
        schema = etree.XMLSchema(schema_root)
        parser = etree.XMLParser(schema=schema)

        try:
            etree.fromstring(xml_data, parser)
            print("XML validation against XSD succeeded.")
        except etree.XMLSchemaError as e:
            print(f"XML validation error: {e}")

    # Write XML to a file
    with open("employees.xml", "wb") as xml_file:
        xml_file.write(xml_data)

    print("Data exported to employees.xml")

    
except oracledb.DatabaseError as e:
    error, = e.args
    print("Error connecting to Oracle Database:", error.message)

# Close the connection
finally:
    if 'connection' in locals():
        connection.close()
        print("Connection closed.")