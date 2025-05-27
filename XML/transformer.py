from lxml import etree

def transform_xml(input_xml_path, xslt_path, output_xml_path):
    try:
        # Parse the input XML and XSLT files
        xml_tree = etree.parse(input_xml_path)
        #print(etree.tostring(xml_tree))
        xslt_tree = etree.parse(xslt_path)
        #print(etree.tostring(xslt_tree))
        
        # Create an XSLT transformer
        transformer = etree.XSLT(xslt_tree)
        
        # Apply the transformation
        transformed_tree = transformer(xml_tree)
        
        # Save the transformed XML to the output file
        with open(output_xml_path, 'wb') as output_file:
            output_file.write(etree.tostring(transformed_tree, pretty_print=True, xml_declaration=True, encoding='UTF-8'))
        
        print(f"Transformation complete. Output saved to {output_xml_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Paths to your files
#input_xml_path = '.\xml_files\student.xml'  # Path to the input XML file
input_xml_path = '.\\xml_files\\cdcatalog\\cdcatalog.xml'  # Path to the input XML file
xslt_path = '.\\xml_files\\cdcatalog\\cdcatalog_key.xsl'  # Path to the XSLT file
output_xml_path = '.\\xml_files\\cdcatalog\\cdcatalog_out.xml'  # Path to save the transformed XML file

# Call the function
transform_xml(input_xml_path, xslt_path, output_xml_path)