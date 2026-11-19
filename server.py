from fastapi import FastAPI
import subprocess
import uvicorn

app = FastAPI()

def run_applescript(script):
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip()

@app.get("/")
def status():
    return {"status": "online", "jarvis": "Bereit", "zentrale": "MacBook Air M5"}

@app.get("/kalender-heute")
def kalender_heute():
    script = 'tell application "Calendar" to get summary of every event of calendar 1'
    return {"kalender": run_applescript(script)}

@app.get("/erinnerungen")
def erinnerungen():
    script = 'tell application "Reminders" to get name of every reminder of list 1 whose completed is false'
    return {"erinnerungen": run_applescript(script)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

