# Python Web Service for Spreadsheet Operations

This repository provides a Python-based web service that enables open (import) and save (export) operations for spreadsheet files by leveraging a .NET class library. The service acts as a bridge between client-side Spreadsheet components and .NET DLLs, allowing seamless file processing.

## About the Service

A .NET class named `SpreadsheetEditor.cs` was created to handle open and save processes. After building and publishing this class, the resulting DLL files from the `bin` folder are referenced in the Python application (`app.py`), which acts as a wrapper web service.

### Workflow

- The Python web service routes open and save requests.
- When a user imports or exports a file, the request is processed through the Python service.
- The service internally calls the .NET class methods to handle file operations.
- The Python application runs as a web service, and its URL is used for the `openUrl` and `saveUrl` of the Spreadsheet component.

This approach allows you to run a Python-based web service that leverages .NET DLLs, similar to the method used for the DOCX editor component.

## Steps to Run the Web Service

1. **Install required Python dependencies:**
	```bash
	python -m pip install flask
	python -m pip install flask-cors
	python -m pip install pythonnet
	```
2. **Start the Python Web API:**
	```bash
	python app.py
	```
3. **Client-side Configuration:**
	Update the `openUrl` and `saveUrl` properties of your Spreadsheet component to point to the hosted URL:
	```jsx
	<SpreadsheetComponent openUrl="http://127.0.0.1:5000/Open" saveUrl="http://127.0.0.1:5000/Save" />
	```

## .NET Dependencies (Optional)

If you wish to build or modify the .NET class library, follow these steps:

1. **Navigate to the .NET project folder:**
	Change your directory to where the `SpreadsheetLibrary.sln` file is located.
	```bash
	cd path/to/SpreadsheetLibrary
	```
2. **Build the .NET project:**
	```bash
	dotnet build SpreadsheetLibrary.sln -c Release
	```
3. **Publish the .NET project:**
	```bash
	dotnet publish SpreadsheetLibrary.sln -c Release
	```

After publishing, reference the generated DLLs in your Python application as needed.