from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI(title="M Project", description="FastAPI Server for M Project")

app.mount("/css", StaticFiles(directory="css"), name="css")
app.mount("/js", StaticFiles(directory="js"), name="js")
app.mount("/imgs", StaticFiles(directory="imgs"), name="imgs")
app.mount("/fonts", StaticFiles(directory="fonts"), name="fonts")
app.mount("/wasm", StaticFiles(directory="wasm"), name="wasm")
app.mount("/common", StaticFiles(directory="common"), name="common")

@app.get("/")
async def root():
    return {"message": "Welcome to M Project", "status": "running"}

@app.get("/character")
async def character_page():
    return FileResponse("character.html")

@app.get("/dialog-voice.html")
async def dialog_voice_page():
    return FileResponse("dialog-voice.html")

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
