import uvicorn
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import pandas as pd
import traceback

from src.functions import generate_draw, convert_from_df_to_dict

MAX_ATTEMPTS = 100

app = FastAPI()

# Mount the static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(('.xlsx', '.xls')):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an Excel file.")
    
    try:
        df = pd.read_excel(file.file)
        
        dict_ = convert_from_df_to_dict(df)
        
        draw = generate_draw(dict_, MAX_ATTEMPTS)

        draw_df = pd.DataFrame(list(draw.items()), columns=['giver', 'receiver'])

        html_table = draw_df.to_html(
            classes='table table-striped table-bordered table-hover table-sm',
            justify='center',
            border=0,
            table_id="data-table"
        )

        # Return the processed data as HTML
        return {"filename": file.filename, "html_table": html_table}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="There was an error processing the file. " + str(traceback.format_exc()))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)