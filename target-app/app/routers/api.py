from fastapi import APIRouter
from app import state
from fastapi import HTTPException

api_router = APIRouter()

@api_router.get("/api/data")
async def get_data():
       if state.chaos_mode:
            raise HTTPException(status_code=500, detail="error")
       else:
             return {"status": "all good"}

