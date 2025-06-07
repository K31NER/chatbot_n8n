from fastapi_mcp import FastApiMCP
from db import fake_db, search_project
from fastapi import FastAPI, HTTPException

# Instanciamos el objeto de FastAPI
app = FastAPI()

# Definimos los endpoints con operation_id
@app.get("/get_all_projects", tags=["mcp"], operation_id="get_all_projects")
async def get_projects():
    """Obten información de todos los proyectos registrados"""
    return fake_db

@app.get("/get_projects_by_id", tags=["mcp"], operation_id="get_project_by_id")
async def get_projects(id: int):
    """Obtén un proyecto específico en base a su id"""
    if not id:
        raise HTTPException(status_code=404, detail="No se digitó un id válido")
    return search_project(id)

# Creamos el servidor MCP
mcp_server = FastApiMCP(
    app,
    name="Mi API MCP",
    description="Servidor MCP para mi API",
)

# Montamos el servidor MCP en la ruta '/mcp'
mcp_server.mount()
