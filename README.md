# talend-to-snowpark

This is small set of scripts to aid in the accelaration of converting Scripts from Talend to Snowpark

The general approach is that you can take your talend xml export scripts and put them on an input folder.

Then you can call the tool like:

`python main.py --input file/or_folder --output file_or_folder`

The tool will assume that for each component there is a corresponding python file that implements the conversion logic.

This is a work in progress so right now conversion capabilities are very basic. 

# How to implement an exporter

An exporter is just a python file that implements the following function:

```python
def convert(node):
    # node is a xml.etree.ElementTree.Element
```

XML nodes are usually like:

```xml
  <node componentName="t<ComponentName>" componentVersion="0.101" offsetLabelX="0" offsetLabelY="0" posX="320" posY="320">
    <elementParameter field="<fieldType>" name="<fieldName>" <some other properties> value="<property value>"/>
    <!-- and some other props ... -->
  </node>
```
To extract property values you can iterate thru the `elementParameter` nodes and check the `name` attribute.

```python
def convert(node):
    component_id = ""
    for child in node:
        if child.tag == "elementParameter" and child.attrib.get("name") == "UNIQUE_NAME":
            component_id = child.attrib['value']
        if child.tag == "elementParameter" and child.attrib.get("name") == "PROPERTIES":
            props = json.loads(child.attrib['value'])
    component_name = node.attrib.get("componentName")

    return f"""    # TMAP {component_id}
"""
```

The output should be a string with some python code.
