from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import json
import io

app = FastAPI()

def convert_json_to_csv(json_data):
    df = pd.json_normalize(json_data)
    # Convert DataFrame to CSV in-memory
    csv_content = df.to_csv(index=False)

    return csv_content

@app.post("/json_to_csv")
async def json_to_csv(file: UploadFile = File(...)):
    try:
        json_data = json.loads(file.file.read().decode("utf-8-sig"))

        csv_content = convert_json_to_csv(json_data)

        # Send the CSV content as a response
        return StreamingResponse(io.StringIO(csv_content), media_type="text/csv", headers={"Content-Disposition": "attachment; filename=output.csv"})
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error during conversion: {str(e)}"
        )
