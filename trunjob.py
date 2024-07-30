"Manages complex Job systems which need to execute one Job after another."
import json
def convert(node):
    component_id = ""
    process=""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROCESS":
            process = child.attrib['value']
    component_name = node.attrib.get("componentName")

    return f"""    # RUN JOB {component_id} 
    session.call("{process}")
"""