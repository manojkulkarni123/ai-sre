from fastapi import APIRouter
from app import state

health_router = APIRouter()

@health_router.get("/health")
async def health():
        return {
        "status": "degraded" if state.chaos_mode or state.memory_leak else "healthy",
        "chaos_mode": state.chaos_mode,  
        "memory_leak": state.memory_leak, 
    }