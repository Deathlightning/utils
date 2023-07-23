from typing import List
from fastapi import FastAPI, Request, File, UploadFile
from pathlib import Path
import uvicorn
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def server():
    html_file = open("upload.html", 'r',encoding="UTF-8").read()
    return html_file

@app.post("/file")
async def file_upload(files: List[UploadFile] = File(...)):
    for file in files:
        with open(f"C:/Users/wzh/Downloads/{file.filename}", 'wb') as f:
            for i in iter(lambda: file.file.read(1024 * 1024 * 10), b''):
                f.write(i)
        f.close()
    return {"file_name": [file.filename for file in files]}

if __name__ == "__main__":
    uvicorn.run(app, host="", port=8080)
