from fastapi import APIRouter, HTTPException
from app.db.models import Desk, Employee, OccupancyData
from app.services.desk_matching import find_suitable_desks
from app.services.vergesense_client import get_real_time_occupancy

router = APIRouter()

@router.get("/desks/available")
async def get_available_desks(query: str, employee_id: int = None):
    try:
        occupancy_data = await get_real_time_occupancy()
        desks = await find_suitable_desks(query, employee_id, occupancy_data)
        return {"available_desks": desks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/desks/{desk_id}")
async def get_desk_details(desk_id: int):
    desk = await Desk.get(desk_id)
    if desk is None:
        raise HTTPException(status_code=404, detail="Desk not found")
    return desk

@router.post("/desks/")
async def create_desk(desk: Desk):
    await desk.save()
    return {"message": "Desk created successfully", "desk_id": desk.id}