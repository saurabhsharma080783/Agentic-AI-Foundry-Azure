from fastapi import FastAPI
from pydantic import BaseModel
from agents.requirement_analyst import RequirementAnalyst
from agents.solution_analyst import SolutionAnalyst
from agents.review_analyst import ReviewAnalyst
from document_generation.word_generator import generate_word

app = FastAPI(title="Agentic AI Solution Generator")

class RequestModel(BaseModel):
    requirements:str

@app.post("/generate")
async def generate(req:RequestModel):
    r=RequirementAnalyst()
    s=SolutionAnalyst()
    v=ReviewAnalyst()
    structured=await r.run(req.requirements)
    solution=await s.run(structured)
    review=await v.run(solution)
    path=generate_word(structured,solution,review)
    return {"document":path,"solution":solution,"review":review}
