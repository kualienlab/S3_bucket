import shutil
from fastapi import FastAPI,File,UploadFile
import os

app = FastAPI()
dest='/'

@app.post("/insertfile")
def upload(file:UploadFile,des='/home/aroooon/Documents/fastapi/static'):
    fullpath = os.path.join(des,file.filename)
  
    with open(fullpath,"wb+") as file_c:
        shutil.copyfileobj(file.file,file_c)

    return f"file {file.filename} saved at location {fullpath}"




