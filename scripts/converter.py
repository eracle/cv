import yaml
import json
from toon import encode

def main():
    # Convert YAML to TOON
    with open('../cv/resume.yaml', 'r') as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)

    toon_data = encode(yaml_data)

    with open('../resume.toon', 'w') as toon_file:
        toon_file.write(toon_data)

if __name__ == '__main__':
    main()