# Integrated .NET Core Library in Python

We have created a SpreadsheetEditor utility with the following functionalities:

* Open (Import)
* Save (Export)

## Open (Import)

You can provide an Excel file (XLS, XLSX) as a stream which will be converted to Workbook format using the XlsIO library. The Open method processes the uploaded file and returns the workbook data as a JSON string for use with the Spreadsheet component.

## Save (Export)

You can export Spreadsheet data to various file formats including Excel (XLS, XLSX), PDF, and CSV. The Save method processes the JSON data from the Spreadsheet component and returns the file stream in the requested format.