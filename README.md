# EJ2-Spreadsheet-WebServices
EJ2 Spreadsheet component web services

## 📘 Example Repository – Hosting Open and Save Services

This repository demonstrates how to host and integrate Open and Save services for the EJ2 Spreadsheet component using ASP.NET Core. These examples are intended for developers building secure, scalable, and production-ready spreadsheet applications without relying on demo endpoints.

## 🚀 Overview

The EJ2 Spreadsheet allows users to view, edit, and manage Excel-like data directly in the browser. While demo endpoints (`openUrl` and `saveUrl`) are useful for showcasing features, they are not suitable for production due to limitations in security, scalability, and customization.

This repository offers a self-hosted solution using ASP.NET Core Web API, giving developers full control over file handling, data privacy, and performance.

## 🔧 How It Works

The Open and Save services are powered by the `Syncfusion XlsIO` library on the server side:

- **Open Service**: Accepts an uploaded Excel file, reads it on the server, and converts it into a JSON workbook format that the Spreadsheet component can render on the client.
- **Save Service**: Receives the modified JSON workbook from the client, converts it back into an Excel file, and returns it for download.

All operations are performed in memory during the request lifecycle, ensuring no data is persisted on the server.

## 📦 Features

- Host your own Open and Save services using ASP.NET Core.
- Full control over data flow and file processing.
- Enhanced security and privacy for enterprise applications.
- Compatible with the Spreadsheet’s `openUrl` and `saveUrl` configuration.

## 🛠️ Setup Instructions

1. Clone this repository.
2. Navigate to the `WebAPI` folder and configure the ASP.NET Core project.
3. Run the project locally.
4. Update the Spreadsheet component’s `openUrl` and `saveUrl` to point to your hosted endpoints.

## 📄 Reference

For a detailed guide, refer to the official blog post:  
[Host Open and Save Services for JavaScript Spreadsheet with ASP.NET Core](https://www.syncfusion.com/blogs/post/host-spreadsheet-open-and-save-services)
