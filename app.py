import os
from typing import List
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="OmniTask AI Engine")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskMilestone(BaseModel):
    milestone_name: str = Field(description="High-level category, phase, or course module")
    task_title: str = Field(description="Specific, micro-actionable task item")
    priority: str = Field(description="High, Medium, or Low assignment based on context")
    estimated_hours: int = Field(description="Reasonable estimated time window to complete")

class ExtractionResponse(BaseModel):
    success: bool
    project_summary: str
    action_items: List[TaskMilestone]

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "OmniTask AI Processing Engine"}

@app.post("/process-document", response_model=ExtractionResponse)
async def process_document(file: UploadFile = File(...)):
    if not file.filename.endswith(('.txt', '.md', '.pdf')):
        raise HTTPException(
            status_code=400, 
            detail="Unsupported format. Please upload standard .txt, .md, or .pdf files."
        )
    
    try:
        content = await file.read()
        raw_text = content.decode("utf-8", errors="ignore")
        
        if not raw_text.strip():
            raise HTTPException(status_code=400, detail="The uploaded document is entirely empty.")
            
        return {
            "success": True,
            "project_summary": f"Successfully ingested raw document: {file.filename}",
            "action_items": [
                {
                    "milestone_name": "Project Initialization",
                    "task_title": "Set up environment profiles and load local backend blueprints",
                    "priority": "High",
                    "estimated_hours": 2
                }
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Robust validation engine caught unhandled exception: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
