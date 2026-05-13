# Integrated .NET Core Library in Python

We have created a `SpreadsheetEditor` utility with the following functionalities:

* Open (Import)
* Save (Export)

## Open (Import)

You can provide an Excel file (XLS, XLSX) as a stream which will be converted to Workbook format using the XlsIO library. The `Open` method processes the uploaded file and returns the workbook data as a JSON string for use with the Spreadsheet component.

## Save (Export)

You can export Spreadsheet data to various file formats including Excel (XLS, XLSX), PDF, and CSV. The `Save` method processes the JSON data from the Spreadsheet component and returns the file stream in the requested format.

## Steps to run the Web-service

### 1. Install the required Python dependencies

Open a terminal in the `Python` folder and run the following commands:

```bash
python -m pip install flask
python -m pip install flask-cors
python -m pip install pythonnet
```

### 2. Build and publish the .NET Standard Wrapper Library

The Python web service loads the compiled `SpreadsheetLibrary` assemblies (and their dependencies) from the `publish` output folder via `pythonnet`. Build and publish the included .NET Standard solution before starting the Python app.

Replace `<Your Folder Structure>` with the absolute path on your machine:

```bash
dotnet build "<Your Folder Structure>\Python\.NET Standard Wrapper Library\SpreadsheetLibrary\SpreadsheetLibrary.sln" -c Release

dotnet publish "<Your Folder Structure>\Python\.NET Standard Wrapper Library\SpreadsheetLibrary\SpreadsheetLibrary.sln" -c Release
```

After publishing, the required DLLs will be available under:

```
.NET Standard Wrapper Library\SpreadsheetLibrary\bin\Release\netstandard2.0\publish\
```

which is the path referenced by `app.py` when loading the assemblies through `clr.AddReference`.

### 3. Start the Python Web API

From the `Python` folder (the folder that contains `app.py`), run:

```bash
python app.py
```

or

```bash
py app.py
```

The service will start on `http://127.0.0.1:5000/` by default and exposes the following endpoints:

* `POST /Open` – Imports an Excel file and returns the workbook as JSON.
* `POST /Save` – Exports the Spreadsheet JSON data to XLS, XLSX, PDF, or CSV.

### 4. Client-side configuration

On the client, update the `openUrl` and `saveUrl` of the Spreadsheet component to point to the hosted Python Web API:

```jsx
<SpreadsheetComponent
    openUrl='http://127.0.0.1:5000/Open'
    saveUrl='http://127.0.0.1:5000/Save'>
</SpreadsheetComponent>
```

> **Note:** If you host the service on a different host or port, update both URLs to match your deployment.