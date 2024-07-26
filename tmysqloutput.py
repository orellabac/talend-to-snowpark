"Writes, updates, makes changes or suppresses entries in a database."
import json
def convert(node):
    component_id = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROPERTIES":
            props = json.loads(child.attrib['value'])
    component_name = node.attrib.get("componentName")

    return ""