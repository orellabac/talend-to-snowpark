
"Triggers a task required for the execution of a Job"

def convert(node):
    component_id = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
    component_name = node.attrib.get("componentName")

    return ""