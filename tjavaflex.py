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

    return f"""    # JAVAFLEX {component_id}
    session.sql(\"\"\"
  create function {component_id}(/* you will need to adjust the parameters*/)
  returns table(/* you will need to adjust the outputs see https://docs.snowflake.com/en/developer-guide/udf/java/udf-java-tabular-functions*/)
  language java
  handler='JavaFlex'
  target_path='@mystage/{component_id}.jar'
  as
  $$
  {code_import}
    import java.util.stream.Stream;
    class OutputRow {{
      public String output_value; /* Add more or less fields as needed */
      public OutputRow(String outputValue) {{
        this.output_value = outputValue;
      }}
    }}
    class JavaFlex {{
      public JavaFlex()  {{
        {CODE_START}
      }}
      public static Class getOutputClass() {{
        return OutputRow.class;
      }}
      public Stream<OutputRow> process(String inputValue) {{
        {CODE_MAIN}
        // Return two rows with the same value.
        return Stream.of(new OutputRow(inputValue), new OutputRow(inputValue));
      }}
      public Stream<OutputRow> endPartition() {{
        {CODE_END}
      }}
    }}
  $$;\"\"\").show()
"""