# Python PDF Editor

This Python application, built using the Tkinter library, provides a user-friendly interface for splitting and merging PDF files. It uses the PyPDF2 library for handling PDF file operations.
<br/><br/>

## Features

##### Merge PDF

- Select a PDF file using the file dialog.

- Specify page ranges to extract and create a new PDF file.

- Supports comma-separated page ranges (e.g., 1-3, 5, 8-10).

##### Merge PDF

- Choose multiple PDF files to merge into a single PDF.

- Arrange the order of files in the merge list.

- Save the merged PDF file with a specified name.
<br/>

## Getting Started

1. Ensure you have Python 3.x installed on your machine with Tkinter.

2. Install the required libraries using the following command: `pip install -r requirements.txt`

3. Run the Python script `python python-pdf-editor.py` to launch the application.
<br/>

## Usage Instructions

##### Split Tab

1. Click the "+" button to select a PDF file.

2. Enter page ranges in the format (e.g., 1-3, 5, 8-10).

3. Click the "Split" button.

4. Choose a location to save the new PDF file.

##### Merge Tab

1. Click the "+" button to add PDF files to the merge list.

2. Arrange the order of files using the Treeview.

3. Click the "Merge" button.

4. Choose a location to save the merged PDF file.