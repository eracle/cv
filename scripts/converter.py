import yaml
import json
from toon import encode

def main():
    # Convert YAML to JSON
    with open('resume.yaml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    with open('resume.json', 'w') as json_file:
        json.dump(yaml_data, json_file, indent=2)

    # Convert JSON to TOON
    with open('resume.json', 'r') as json_file:
        json_data = json.load(json_file)

    toon_data = encode(json_data)

    with open('resume.toon', 'w') as toon_file:
        toon_file.write(toon_data)

if __name__ == '__main__':
    main()