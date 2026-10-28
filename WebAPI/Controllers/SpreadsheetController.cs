using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Syncfusion.EJ2.Spreadsheet;
using System.Text.Json;
using System.IO;

namespace WebAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SpreadsheetController : ControllerBase
    {
        [HttpPost]
        [Route("Open")]
        public IActionResult Open([FromForm] IFormCollection openRequest)
        {
            OpenRequest open = new OpenRequest();
            if (openRequest.Files.Count != 0)
            {
                open.File = openRequest.Files[0];
                if (openRequest.ContainsKey("IsManualCalculationEnabled") && bool.TryParse(openRequest["IsManualCalculationEnabled"].ToString(), out bool flag))
                {
                    open.IsManualCalculationEnabled = flag;
                }
            }
            open.Password = openRequest["Password"];
            if (openRequest["SheetIndex"].Count != 0)
            {
                open.SheetIndex = int.Parse(openRequest["SheetIndex"].ToString());
            }
            open.SheetPassword = openRequest["SheetPassword"];
            return Content(Workbook.Open(open));
        }

        [HttpPost]
        [Route("Save")]
        public IActionResult Save([FromForm] SaveSettings saveSettings)
        {
            return Workbook.Save(saveSettings);
        }

        [HttpPost]
        [Route("OpenFromJson")]
        public IActionResult OpenFromJson()
        {
            try
            {
                // Read workbook.json from the application root directory
                string jsonFilePath = Path.Combine(Directory.GetCurrentDirectory(), "workbook.json");

                if (!System.IO.File.Exists(jsonFilePath))
                {
                    return NotFound("workbook.json file not found in the application root directory.");
                }

                // Read JSON content from file
                string jsonContent = System.IO.File.ReadAllText(jsonFilePath);

                // Parse JSON to verify structure and extract Workbook element
                var jsonDocument = JsonDocument.Parse(jsonContent);

                // First, extract jsonObject property
                if (!jsonDocument.RootElement.TryGetProperty("jsonObject", out JsonElement jsonObjectElement))
                {
                    return BadRequest("Invalid JSON format: 'jsonObject' key not found.");
                }

                // Then, extract Workbook from jsonObject
                if (!jsonObjectElement.TryGetProperty("Workbook", out JsonElement workbookElement))
                {
                    return BadRequest("Invalid JSON format: 'Workbook' key not found in jsonObject.");
                }

                string workbookJson = workbookElement.GetRawText();

                // Create SaveSettings with the workbook JSON data
                SaveSettings saveSettings = new SaveSettings()
                {
                    SaveType = SaveType.Xlsx,
                    FileName = "Sample",
                    JSONData = workbookJson,
                    PdfLayoutSettings = "{\"fitSheetOnOnePage\":false}"
                };

                // Save the workbook to a stream
                var excelStream = Workbook.Save<Stream>(saveSettings);

                // Save the file in the application directory
                string outputFilePath = Path.Combine(Directory.GetCurrentDirectory(), "Sample.xlsx");

                using (var fileStream = new FileStream(outputFilePath, FileMode.Create, FileAccess.Write))
                {
                    excelStream.Position = 0;
                    excelStream.CopyTo(fileStream);
                }

                return Ok(new { message = "Workbook saved successfully", filePath = outputFilePath });
            }
            catch (Exception ex)
            {
                return StatusCode(500, new { error = ex.Message });
            }
        }
    }
}
