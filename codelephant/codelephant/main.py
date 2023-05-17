import os
import sys
import re
import json
from collections import Counter
from dir_helpers import get_all_files

KNOWN_EXTENSIONS = {
    "py": "python",
    "js": "js",
    "Makefile": "make"
}

def process_directory(directory: str) -> str:
    result = {
        "summary": {},
        "results": []
    }
    extensions = []
    try:
        for file in get_all_files(directory):
            extension = re.split("\\.|/", file)[-1]
            if extension in KNOWN_EXTENSIONS:
                extensions.append(extension)
                result["results"].append({
                    "path": file,
                    "language": KNOWN_EXTENSIONS[extension]
                })
    except ValueError as e:
        print(e)
        sys.exit(1)


    counter =  Counter(extensions)
    for extension, count in counter.items():
        result["summary"][KNOWN_EXTENSIONS[extension]] = round(count / sum(counter.values()), 6)
    return json.dumps(result, indent=4)
    


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please provide a directory path as an argument.")
        sys.exit(1)

    directory = sys.argv[1]
    print(process_directory(directory))