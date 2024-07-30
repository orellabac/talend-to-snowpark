
"Opens a connection to Snowflake that can then be reused by other Snowflake components."
import json
def convert(node):
    component_id = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROPERTIES":
            props = json.loads(child.attrib['value'])
    component_name = node.attrib.get("componentName")

    return f"""    # Snowflake Connection {component_id}
    session = Session.builder.app_name("").getOrCreate()
"""