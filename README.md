# PDF Merger Tool

This is a simple Python utility to merge multiple PDF files using the [`PyPDF2`](https://pypi.org/project/PyPDF2/) library. It reads PDF files from the `inputs` folder and creates a merged output PDF in the `outputs` folder.

## Features

- Merge multiple PDFs into a single document
- Automatically creates input and output folders if they do not exist
- Easy to customize file names and merge order

## Requirements

- Python 3.11+
- Poetry for dependency management

## Installation

1. Clone this repository:

```bash
git clone <your-repo-url>
cd pdf-tool
```
# Install dependencies with Poetry:
```
poetry install
```

# Folder Structure
.
├── inputs/                 # Place your input PDFs here
│   └── Allianz_annual_2024.pdf
├── outputs/                # Merged PDFs will be saved here
│   └── merged_output.pdf
├── main.py                 # Main script
├── poetry.lock
└── pyproject.toml

# Usage
Place the PDFs you want to merge into the inputs/ folder.

Edit the main.py script to list the files you want to merge:

```
pdf_files = ["Allianz_annual_2024.pdf"]  # List more files in desired order
```

Run the script
```
poetry run python main.py
```


 
