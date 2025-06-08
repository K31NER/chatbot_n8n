from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel,Session, create_engine

URL_BD =  "sqlite:///./proyect.db"

engine = create_engine(URL_BD,connect_args={"check_same_thread": False},echo=True)
    
def get_session():
    """ Obtener la conexion de la base de datos"""
    with Session(engine) as session:
        yield session
        
def creat_all_table(app:FastAPI):
    """ Crea todas ñas tablas de la base de datos """
    SQLModel.metadata.create_all(engine)
    print("Tablas creadas con exito")
    yield
    
connection = Annotated[Session,Depends(get_session)]