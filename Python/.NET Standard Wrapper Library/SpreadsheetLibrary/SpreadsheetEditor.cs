using Syncfusion.EJ2.Spreadsheet;
using Syncfusion.XlsIO;
using System;
using System.IO;

namespace SpreadsheetLibrary
{
    public class SpreadsheetEditor
    {
        public string Open(byte[] byteArr)
        {
            // Loading the bytes array to stream.
            MemoryStream stream = new MemoryStream(byteArr);
            //Creates a new instance for ExcelEngine
            ExcelEngine excelEngine = new ExcelEngine();

            //Initialize IApplication
            IApplication application = excelEngine.Excel;
            //Loads or open an existing workbook through Open method of IWorkbooks
            IWorkbook workbook = application.Workbooks.Open(stream);
            //OpenRequest open = new OpenRequest();
            //// Converting the stream into FormFile.
            //open.File = new FormFile(stream, 0, bytes.Length, "Sample", "Sample." + "xlsx");
            //var result = Workbook.Open(open);
            var spreadsheet = new SheetOpen();
            var result = spreadsheet.ProcessWorkBook(workbook);
            return result;
        }

        public Stream Save(SaveSettings settings)
        {
            return Workbook.Save<Stream>(settings);
        }
    }
}
