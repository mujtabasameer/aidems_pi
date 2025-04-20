from fastapi import APIRouter, HTTPException
from database.influx import get_latest_sensor_data, get_historical_sensor_data 

router = APIRouter()

@router.get("/air-quality")
def get_quality_columns() :
    try:
        columns = get_latest_sensor_data()  
        if not columns:
            raise HTTPException(status_code=404, detail="No readings found")
        return columns
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/historical-data")
def get_historical_columns() :
    try:
        columns = get_historical_sensor_data()
        if not columns:
            raise HTTPException(status_code=404, detail="No reading found")
        return columns
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


