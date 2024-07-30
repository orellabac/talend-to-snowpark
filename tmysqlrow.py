"Executes the stated SQL query on the specified MySQL database."
import json
def convert(node):
    component_id = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROPERTIES":
            props = json.loads(child.attrib['value'])
        if child.tag == "elementParameter" and child.attrib.get("name") == "QUERY":
            query = child.attrib['value'][1:-1]
    component_name = node.attrib.get("componentName")

    return f"""    # MySQL query 
    session.read.format("jdbc").jdbc("mysql", "jdbc:mysql://host:port/database", "user", "password", 
\"\"\"{query}\"\"\")
"""