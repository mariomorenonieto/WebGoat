import re
def parse_log(text):
    pattern = r'\b(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}.\d{3}\s+([A-Z]+)\s\d{7}\s---\s\[([a-zA-Z0-9]+)\]\s([a-zA-Z0-9.]+)\s+:)\s([^\r\n]+)'
    matches = re.findall(pattern, text)
    for match in matches:
        level = match[1]
        thread = match[2]
        class_name = match[3]
        message = match[4]
        if not class_name:
            class_name = match[5]
        print(f'"{level}","{thread}","{class_name}","{message}"')
text = input()
parse_log(text)
