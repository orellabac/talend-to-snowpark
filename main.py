import xml.etree.ElementTree as ET
import importlib

def convert_talend_to_python(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    output_code = ""
    for component in root.findall('.//node'):
        component_name = component.get('componentName')
        if component_name:
            python_module_name = component_name.lower()
            try:
                module = importlib.import_module(python_module_name)
                python_code = module.convert(component)
                output_code += python_code + "\n"
            except ModuleNotFoundError:
                print(f"No module found for component {component_name}")
            except AttributeError:
                print(f"Module {python_module_name} does not have a convert function")
    return output_code
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert Talend components to Python code')
    parser.add_argument('--input', required=True, help='Input file')
    parser.add_argument('--output', required=True, help='output file')
    
    args = parser.parse_args()

    xml_file = args.input
    output_code = convert_talend_to_python(xml_file)
    with open(args.output, 'w') as f:
        f.write(output_code)

