from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database
from .auth import get_current_user

router = APIRouter(
    prefix="/missions",
    tags=["missions"]
)

@router.post("/", response_model=schemas.MissionOut)
def create_mission(
    mission: schemas.MissionCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_mission = models.Mission(**mission.dict(), owner_id=current_user.id)
    db.add(new_mission)
    db.commit()
    db.refresh(new_mission)
    return new_mission

@router.get("/", response_model=List[schemas.MissionOut])
def read_missions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    missions = db.query(models.Mission).offset(skip).limit(limit).all()
    return missions

@router.get("/{mission_id}", response_model=schemas.MissionOut)
def read_mission(
    mission_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    mission = db.query(models.Mission).filter(models.Mission.id == mission_id).first()
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    return mission

@router.patch("/{mission_id}/status", response_model=schemas.MissionOut)
def update_mission_status(
    mission_id: int,
    status_update: schemas.MissionUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    mission = db.query(models.Mission).filter(models.Mission.id == mission_id).first()
    if mission is None:
        raise HTTPException(status_code=404, detail="Mission not found")
    
    mission.status = status_update.status
    db.commit()
    db.refresh(mission)
    return mission
