using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Syncfusion.EJ2.Spreadsheet;
using Syncfusion.XlsIO;

namespace WebAPI.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class SpreadsheetController : ControllerBase
    {
        [HttpPost]
        [Route("Open")]
        public IActionResult Open([FromForm]IFormCollection openRequest)
        {
            OpenRequest open = new OpenRequest();
            open.File = openRequest.Files[0];
            return Content(Workbook.Open(open));
        }

        [HttpPost]
        [Route("Save")]
        public IActionResult Save([FromForm]SaveSettings saveSettings)
        {
            return Workbook.Save(saveSettings);
        }

        [HttpGet]
        [Route("ping")]
        public IActionResult Ping()
        {
            return Ok();
        }
    }
}