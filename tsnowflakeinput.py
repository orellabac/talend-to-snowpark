"Reads data from a Snowflake table into the data flow of your Job based on an SQL query."
import json
def convert(node):
    component_id = ""
    props = {}
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROPERTIES":
            props = json.loads(child.attrib['value'])
    component_name = node.attrib.get("componentName")
    query = props.get("query")
    if query is not None:
        query = query["storedValue"][1:-1]
    return f"""# Snowflake Input {component_id}
{component_id} = session.sql('''
{query}
''')
""" 