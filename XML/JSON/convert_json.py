import xmltodict
import json
import json as json_std
from jsonschema import validate

json_schema = {
    "type": "object",
    "properties": {
        "employees": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "employee_id": {"type": "integer"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "email": {"type": "string"},
                    "phone_number": {"type": "string"},
                    "hire_date": {"type": "string"},
                    "job_id": {"type": "string"},
                    "salary": {"type": "number"},
                    "manager_id": {"type": "integer"},
                    "department_id": {"type": "integer"}
                },
                "required": ["employee_id", "first_name", "last_name", "email"]
            }
        }
    },
    "required": ["employees"]
}

with open("XML/JSON/gimnas.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()

dict_data = xmltodict.parse(xml_data)

validate(instance=dict_data, schema=json_schema)

with open("XML/JSON/gimnasio.json", "w", encoding="utf-8") as json_file:
    json.dump(dict_data, json_file, indent=4, ensure_ascii=False)

print("JSON guardado correctamente en 'gimnasio.json'")
