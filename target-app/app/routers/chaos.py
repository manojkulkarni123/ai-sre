from fastapi import APIRouter
from app import state

chaos_router = APIRouter()

@chaos_router.post("/chaos/start")
async def chaosON():
       state.chaos_mode = True
       return {"chaos_mode": state.chaos_mode}

@chaos_router.post("/chaos/stop")
async def chaosOFF():
      state.chaos_mode = False
      return {"chaos_mode": state.chaos_mode}