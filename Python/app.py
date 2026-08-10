from flask import Flask, json, request, Response, send_file
from flask_cors import CORS #import CORS from flask_cors

import clr #import clr from pythonnet
import os
from io import BytesIO

app = Flask(__name__)
CORS(app) #enable CORS on the app

app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024 # 500 MB
app.config['MAX_FORM_MEMORY_SIZE'] = 500 * 1024 * 1024 # 500 MB

# get the current working directory
current_working_directory = os.getcwd()

# Load explicit DLLs from the publish folder (direct AddReference calls)
publish_base = current_working_directory + "/.NET Standard Wrapper Library/SpreadsheetLibrary/bin/Release/netstandard2.0/publish/"

clr.AddReference(publish_base + "Syncfusion.EJ2.Spreadsheet.dll")
clr.AddReference(publish_base + "BitMiracle.LibTiff.NET.dll")
clr.AddReference(publish_base + "HarfBuzzSharp.dll")
clr.AddReference(publish_base + "Microsoft.Bcl.AsyncInterfaces.dll")
clr.AddReference(publish_base + "Newtonsoft.Json.dll")
clr.AddReference(publish_base + "SkiaSharp.dll")
clr.AddReference(publish_base + "SkiaSharp.HarfBuzz.dll")
clr.AddReference(publish_base + "SpreadsheetLibrary.dll")
clr.AddReference(publish_base + "Syncfusion.Compression.Portable.dll")
clr.AddReference(publish_base + "Syncfusion.EJ2.dll")
clr.AddReference(publish_base + "Syncfusion.Licensing.dll")
clr.AddReference(publish_base + "Syncfusion.MetafileRenderer.Portable.dll")
clr.AddReference(publish_base + "Syncfusion.Pdf.Imaging.Portable.dll")
clr.AddReference(publish_base + "Syncfusion.Pdf.Portable.dll")
clr.AddReference(publish_base + "Syncfusion.SkiaSharpHelper.Portable.dll")
clr.AddReference(publish_base + "Syncfusion.XlsIO.Portable.dll")
clr.AddReference(publish_base + "Syncfusion.XlsIORenderer.Portable.dll")
clr.AddReference(publish_base + "System.Buffers.dll")
clr.AddReference(publish_base + "System.Memory.dll")
clr.AddReference(publish_base + "System.Numerics.Vectors.dll")
clr.AddReference(publish_base + "System.Runtime.CompilerServices.Unsafe.dll")
clr.AddReference(publish_base + "System.Text.Encoding.CodePages.dll")
clr.AddReference(publish_base + "System.Text.Encodings.Web.dll")
clr.AddReference(publish_base + "System.Text.Json.dll")
clr.AddReference(publish_base + "System.Threading.Tasks.Extensions.dll")
clr.AddReference(publish_base + "Microsoft.AspNetCore.Mvc.Core.dll")
clr.AddReference(publish_base + "Microsoft.AspNetCore.Mvc.Abstractions.dll")
clr.AddReference(publish_base + "Microsoft.AspNetCore.Razor.dll")

#import our SpreadsheetEditor class from our C# namespace SpreadsheetLibrary
from SpreadsheetLibrary import SpreadsheetEditor
from Syncfusion.EJ2.Spreadsheet import SaveSettings, SaveType
from Syncfusion.Licensing import SyncfusionLicenseProvider
from System import Enum
from System.IO import SeekOrigin

# Register Syncfusion license
SyncfusionLicenseProvider.RegisterLicense("Your License key")

spreadEditor = SpreadsheetEditor() #create our SpreadsheetEditor object

@app.route('/Open', methods=['POST'])
def openExcel():
    if 'file' in request.files:
        files = request.files['file']
        # Get the stream data
        stream_data = files.stream.read()
        # Calling our Open method from our SpreadsheetEditor class which will return the Workbook JSON string
        return spreadEditor.Open(stream_data)
    else:
        return ""

@app.route('/Save', methods=['POST'])
def saveExcel():
    try:
        # Extract parameters from form data
        json_data = request.form.get('JSONData', '')
        save_type = request.form.get('saveType', 'Xlsx')  # Default to Xlsx
        file_name = request.form.get('fileName', 'Sample')
        
        # Extract PDF layout settings if provided
        pdf_layout_settings = request.form.get('pdfLayoutSettings', '{}')
        
        # Create SaveSettings object
        save_settings = SaveSettings()
        save_settings.JSONData = json_data
        # Convert string to SaveType enum
        save_settings.SaveType = Enum.Parse(SaveType, save_type)
        save_settings.FileName = file_name
        save_settings.PdfLayoutSettings = pdf_layout_settings
        
        # Call the Save method from SpreadsheetEditor class
        file_stream = spreadEditor.Save(save_settings)
        
        # Convert .NET MemoryStream to bytes
        file_stream.Seek(0, SeekOrigin.Begin)  # Seek to beginning
        stream_bytes = file_stream.ToArray()  # Convert to byte array
        file_stream.Dispose()  # Clean up the stream
        
        # Convert bytes to BytesIO for Flask
        output = BytesIO(stream_bytes)
        output.seek(0)
        
        extension = f".{save_type.lower()}"
        # Get the mime type based on the save type.
        mime_type = {
            "xls":  "application/vnd.ms-excel",
            "xlsx": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "pdf": "application/pdf",
            "csv": "text/csv"
        }.get(save_type.lower(), "application/octet-stream")

        return send_file(
            output,
            as_attachment=True,
            download_name=f"{file_name}{extension}",
            mimetype=mime_type
        )

    except Exception as e:
        import traceback
        error_msg = f"Error saving file: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return error_msg, 500



@app.route("/")
def home():
    return "Flask Web API for SpreadsheetEditor!"

if __name__ == "__main__":
    app.run(debug=True) # http://localhost:5000/
    # app.run(host='', port=5001, debug=True) # http://localhost:5001/
