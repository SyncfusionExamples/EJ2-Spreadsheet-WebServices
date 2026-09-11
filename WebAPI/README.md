# Spreadsheet WebAPI - Implementation

## Overview

We have implemented the Open and Save (server-side) functionality in ASP.NET Core using the Syncfusion XLSIO library. This library handles file operations on the server. When you open a file, the XLSIO library reads and converts it to a spreadsheet-compatible workbook in JSON format. Similarly, when you save the spreadsheet, we process the workbook JSON into an Excel model using the XLSIO library. 

**Security Notice:** Your data is not stored on our server during these actions, ensuring it remains safe and secure.

## How to Run the WebAPI

Follow these steps to launch and run the local service:

### 1. Prerequisites
- .NET Core SDK installed
- Visual Studio or Visual Studio Code with C# support

### 2. Setup Instructions

1. **Download and Extract**
   - Download and unzip the WebAPI project.

2. **Open the Solution**
   - Open the `WebAPI.sln` file in Visual Studio.

3. **Install Syncfusion Packages**
   - Right-click on the **Dependencies** folder in the WebAPI project.
   - Click **Manage NuGet Packages**.
   - In the **Browse** tab, search for `Syncfusion.EJ2.Spreadsheet.AspNet.Core`.
   - Install the latest package version.

4. **Update Existing Packages (if needed)**
   - If the package already exists, remove it first, then re-install it to ensure all dependent packages are downloaded.

5. **Build the Solution**
   - Build the solution using **Build > Build Solution** or press `Ctrl+Shift+B`.

6. **Run the Service**
   - Press `F5` or click **Run** to start the WebAPI service.
   - The service will be hosted on `https://localhost:{port-number}`.

## API Endpoints

The WebAPI exposes the following endpoints for spreadsheet operations:

### Open Endpoint
```
POST /api/spreadsheet/open
```

Accepts a file upload and converts it to JSON format.

**Code Implementation:**
```csharp
[HttpPost]
[Route("Open")]
public IActionResult Open([FromForm]IFormCollection openRequest)
{
    OpenRequest open = new OpenRequest();
    open.File = openRequest.Files[0];
    return Content(Workbook.Open(open));
}
```

### Save Endpoint
```
POST /api/spreadsheet/save
```

Accepts workbook data in JSON format and returns the Excel file.

**Code Implementation:**
```csharp
[HttpPost]
[Route("Save")]
public IActionResult Save([FromForm]SaveSettings saveSettings)
{
    return Workbook.Save(saveSettings);
}
```

## Configuring Client-Side URLs

After launching the local service, update the Open and Save URLs in your client-side sample:

### Example Configuration

```javascript
openUrl: 'https://localhost:{port-number}/api/spreadsheet/open'
saveUrl: 'https://localhost:{port-number}/api/spreadsheet/save'
```

### Specific Example

If your service runs on port 44354:

```javascript
openUrl: 'https://localhost:44354/api/spreadsheet/open'
saveUrl: 'https://localhost:44354/api/spreadsheet/save'
```

## Finding Your Port Number

The port number is displayed in the console output when you run the WebAPI service. Look for output similar to:
```
Now listening on: https://localhost:44354
```

## Important Notes

**Ensure the WebAPI service is running before executing the client-side sample.** The client-side application will not be able to open or save spreadsheets if the service is not accessible.

## Troubleshooting

- **Service not starting:** Ensure all NuGet packages are correctly installed.
- **Connection refused:** Verify the correct port number and that the service is running.
- **Package conflicts:** Clear the NuGet cache and reinstall all packages.
