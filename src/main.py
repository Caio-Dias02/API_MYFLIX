from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.schemas import schemas
from src.infra.sqlalchemy.repositores.series import RepositorioSerie

#Create dataBase
create_db()

app = FastAPI()

@app.post('/series')
def create_serie(serie: schemas.Serie, db: Session = Depends(get_db)):
    created_serie = RepositorioSerie(db).create(serie)
    return created_serie

@app.get('/series')
def list_serie(db: Session = Depends(get_db)):
    return RepositorioSerie(db).list()

@app.get('/series/{serie_id}')
def get_serie(serie_id: int, db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).get(serie_id)    
    return serie

@app.delete('/series/{serie_id}')
def get_serie(serie_id: int, db: Session = Depends(get_db)):
    RepositorioSerie(db).remove(serie_id)    
    return {"MSG": "successfully removed"}