from sqlmodel import select
from fastapi_mcp import FastApiMCP
from fastapi.responses import JSONResponse
from models  import Project, CreateProject
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from db import creat_all_table , connection

# Instanciamos el objeto de FastAPI
app = FastAPI(lifespan=creat_all_table)

# Definimos los endpoints con operation_id
@app.get("/get_all_projects", tags=["mcp"], operation_id="get_all_projects")
async def get_projects(db:connection):
    """Obten información de todos los proyectos registrados
    
    Devuelve
    - Lista de todos los proyectos con su informcacio id,name y description
    """
    query = select(Project)
    return db.exec(query).all()

@app.get("/get_projects_by_id", tags=["mcp"], operation_id="get_project_by_id")
async def get_projects(db:connection,id: int):
    """Obtén un proyecto específico en base a su id 
    Devuelve
    - id
    - name
    - description
    """
    
    if not id:
        raise HTTPException(status_code=404, detail="No se digitó un id válido")
    
    query = select(Project).where(Project.id == id)
    result = db.exec(query).first()
    
    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron proyectos con ese id")
    
    return result 

@app.post("/create_project")
async def create_project(db:connection, project: CreateProject):
    """ Crear nuevos proyectos 
    
    Parametros:
    - json con name, description
    """
    try: 
        new_project = Project(
            name=project.name,
            description=project.description
        )
        
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        
        return JSONResponse(content={
            "Message":f"Proyecto: {project.name} creado con exito"
        }, status_code=201)
        
    except SQLAlchemyError as e:
        db.rollback()  # Hacemos rollback si falla commit
        raise HTTPException(
            status_code=500,
            detail=f"Error al crear el proyecto: {str(e)}"
        )

    except Exception as e:
        # Captura cualquier otro error no previsto
        raise HTTPException(
            status_code=500,
            detail=f"Error inesperado: {str(e)}"
        )
        
# Creamos el servidor MCP
mcp_server = FastApiMCP(
    app,
    name="Mi API MCP",
    description="Servidor MCP para mi API",
)

# Montamos el servidor MCP en la ruta '/mcp'
mcp_server.mount()
