#  Copyright (c) 2023 Kanishk Pachauri.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.organizations_schmea import Organizations_schema
from app.models.organization_models import Organizations_db
from sqlalchemy.orm import Session
from app.db.database import get_db

router = APIRouter(
    tags=["organizations"],
    prefix="/yogdaan/apiv1/organizations"
)

@router.post("/add")
def add_organizations(organizations_schema: Organizations_schema, db: Session = Depends(get_db)):
    new_organization = Organizations_db(name = organizations_schema.name, description = organizations_schema.description, url = organizations_schema.url)
    db.add(new_organization)
    db.commit()
    db.refresh(new_organization)
    return new_organization

@router.get("/info/all")
def get_all_organizations(db: Session = Depends(get_db)):
    organizations = db.query(Organizations_db).all()
    return organizations

@router.get("/info/{id}")
def get_organizations_by_id(id: int, db: Session = Depends(get_db)):
    organizations = db.query(Organizations_db).filter(Organizations_db.id == id).first()
    if organizations:
        return organizations
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Orgs not Found")

@router.delete("/delete/{id}")
def delete_organizations_by_id(id: int, db: Session = Depends(get_db)):
    organizations = db.query(Organizations_db).filter(Organizations_db.id == id).first()
    if organizations:
        db.delete(organizations)
        db.commit()
        return {"Details": "Successfully Delete the Organization"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Organization {organizations} with this ID is not available in the Database")
