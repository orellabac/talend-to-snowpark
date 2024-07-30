
"Opens a connection to the specified MySQL database for reuse in the subsequent subJob or subJobs."
import json
import common

def convert(node):
    component_id = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROPERTIES":
            props = json.loads(child.attrib['value'])
        if child.tag == "elementParameter" and child.attrib.get("name") == "CONNECTION":
            connection = child.attrib['value']
    component_name = node.attrib.get("componentName")
    common.components[component_id] = node
    return f"""    # MySQL connection {component_id}
"""