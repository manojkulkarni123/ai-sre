from fastapi import FastAPI
from app.routers.health import health_router
from app.routers.api import api_router
from app.routers.chaos import chaos_router
from prometheus_fastapi_instrumentator import Instrumentator



app = FastAPI()

Instrumentator().instrument(app).expose(app)

app.include_router(health_router)
app.include_router(chaos_router)
app.include_router(api_router)

