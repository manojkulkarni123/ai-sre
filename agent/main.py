from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List
from datetime import datetime


class Alert(BaseModel):
    status: str
    labels: dict
    annotations: dict
    startsAt: datetime
    endsAt: datetime
    generatorURL: str
    fingerprint: str


class AlertManagerPayload(BaseModel):
    receiver: str
    status: str
    alerts: List[Alert]
    groupLabels: dict
    commonLabels: dict
    commonAnnotations: dict
    externalURL: str
    version: str
    groupKey: str
    truncatedAlerts: int


app = FastAPI()


@app.post("/webhook/alert")
async def webhook_alert(payload: AlertManagerPayload, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_alert, payload)
    return {"status": "received"}


def process_alert(payload: AlertManagerPayload):
    
    pass