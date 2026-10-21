from fastapi import FastAPI
from pydantic import BaseModel
from app.priority import calculate_priority
class PriorityRequest(BaseModel):
    customer_impact: str
    business_impact: str
    urgency: str
    resolution_minutes: int
    sla_target_minutes: int

from app.classifier import classify_ticket

app = FastAPI(
    title="AI Support & Product Analytics Copilot",
    version="0.1.0"
)


class TicketRequest(BaseModel):
    ticket_description: str


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "AI Support & Product Analytics Copilot API is running"
    }


@app.post("/classify")
def classify(request: TicketRequest):
    result = classify_ticket(request.ticket_description)

    return {
        "classification": result
    }
    
@app.post("/prioritize")
def prioritize(request: PriorityRequest):

    result = calculate_priority(
        customer_impact=request.customer_impact,
        business_impact=request.business_impact,
        urgency=request.urgency,
        resolution_minutes=request.resolution_minutes,
        sla_target_minutes=request.sla_target_minutes
    )

    return result    