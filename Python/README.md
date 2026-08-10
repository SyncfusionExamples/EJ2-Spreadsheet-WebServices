# Python Web Service for Spreadsheet Operations

This repository provides a Python-based web service that enables open (import) and save (export) operations for spreadsheet files by leveraging a .NET class library. The service acts as a bridge between client-side Spreadsheet components and .NET DLLs, allowing seamless file processing.

## About the Service

This solution integrates a .NET Standard class library with a Python web service to enable spreadsheet file operations.

**.NET Project Structure:**
- The core logic for opening and saving spreadsheet files is implemented in C# within a .NET Standard class library (e.g., `SpreadsheetEditor.cs`).
- The project is managed using a solution file (`.sln`) and a project file (`.csproj`).
- When you build and publish the .NET project, DLL files are generated in the `bin` directory. These DLLs contain all the compiled logic required for spreadsheet processing.

**Integration with Python:**
- The Python application (`app.py`) acts as a lightweight web API wrapper.
- It uses the `pythonnet` package to load the published .NET DLLs and invoke their methods for file operations.
- The Python code is minimal and primarily responsible for routing HTTP requests and calling the appropriate .NET methods.

### Workflow

- The Python web service routes open and save requests.
- When a user imports or exports a file, the request is processed through the Python service.
- The service internally calls the .NET class methods to handle file operations.
- The Python application runs as a web service, and its URL is used for the `openUrl` and `saveUrl` of the Spreadsheet component.

This approach allows you to run a Python-based web service that leverages .NET DLLs.

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
	Update the `openUrl` and `saveUrl` properties of your Client-side Spreadsheet component to point to the hosted URL:

	| Property   | Value                                 |
	|------------|---------------------------------------|
	| openUrl    | http://127.0.0.1:5000/Open            |
	| saveUrl    | http://127.0.0.1:5000/Save            |

## .NET Dependencies (Optional)

> **Note:** This repository already includes the required Spreadsheet library DLLs. In most cases, you can use the provided DLLs without any additional setup.

If you need to update the package version or modify the .NET implementation, you can generate new DLLs by following the steps below.

1. **Navigate to the .NET project folder:**
	Change your directory to where the `SpreadsheetLibrary.sln` file is located.
	```bash
	cd path/to/SpreadsheetLibrary
	```
2. **Build the .NET project:**
	```bash
	dotnet build -c Release
	```
3. **Publish the .NET project:**
	```bash
	dotnet publish -c Release
	```

After publishing, the newly generated DLLs will be referred by the Python application.
