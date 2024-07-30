"Extends the functionalities of a Job using custom Java commands."
import json
def convert(node):
    component_id = ""
    code_import = ""
    code   = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "CODE":            
            code = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "IMPORT":            
            code_import = child.attrib['value']
    component_name = node.attrib.get("componentName")

    return f"""    # JAVA {component_id}
    session.sql(\"\"\"
    with JAVA_SNIPPET as procedure () 
    returns string 
    LANGUAGE JAVA
    RUNTIME_VERSION = '11'
    PACKAGES = ('com.snowflake:snowpark:latest')
    handler='SnippetClass.run' as $$
    import java.sql.*;
    import net.snowflake.client.jdbc.*;

    class SnippetClass {{
    public String run(com.snowflake.snowpark.Session session) throws Exception {{
        Connection connection = session.jdbcConnection();
        {code_import}
        {code}
        return "Success";
    }}
    }}
    $$ CALL JAVA_SNIPPET();\"\"\").show()
"""