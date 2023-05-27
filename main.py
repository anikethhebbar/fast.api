from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/call_program")
def call_program():
    try:
        # Call the external program using subprocess
        subprocess.run(["python", "an.py"])
        return {"message": "Program called successfully"}
    except Exception as e:
        return {"message": f"Error calling program: {str(e)}"}