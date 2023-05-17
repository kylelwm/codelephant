# Codelephant
## Description
This is a command-line interface (CLI) tool written in Python. It accepts a directory as an argument and lists out all the files within the directory and subdirectories. It also provides a summary of the ratio of different files within the directory.

## Installation
### Prerequisites
Make sure you have the following prerequisites installed on your machine:

* Python 3.x

### Clone the Repository
1. Open a terminal.
2. Clone the repository using the following command:

`git clone https://github.com/kylelwm/codelephant-poc.git`

1. Navigate to the project directory:

`cd codelephant-poc`

Install Dependencies

1. Create a virtual environment (optional but recommended):

`python3 -m venv venv`

2. Activate the virtual environment:

`source venv/bin/activate`

3. Install the required dependencies:

`pip install -r requirements.txt`

## Usage
1. In the terminal, navigate to the project directory if you haven't already done so.

2. Run the CLI tool with the following command:
`sh exec.sh /path/to/directory`

Replace /path/to/directory with the actual directory path you want to process.

## Examples
Given the following directory structure:
```
/some/path
    /a.py
    /another/path
        /b.js
```

The output should be:
```
{
    "summary": {
        "python": 0.5,
        "js": 0.5
    },
    "results": [
        {
            "path": "/some/path/a.py",
            "language": "python"
        },
        {
            "path": "/some/path/another/path/b.js",
            "language": "js"
        }
    ]
}
```
