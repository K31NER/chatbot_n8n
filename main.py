import os
import httpx
from dotenv import load_dotenv
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI,Request, Form

# Cargamos las varibales de entorno
load_dotenv()

# Obtenmos la url de n8n
URL_N8N = os.getenv("N8N_URL")

# Creamos el objeto de Fastapi
app = FastAPI()

# Cargamos los templates
template = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def arancar():
    print("Servidor iniciado con exito")
    
@app.get("/",response_class=HTMLResponse)
async def index(request:Request):
    return template.TemplateResponse("index.html",{"request":request})

# Endpoint para el chatbot
@app.post("/chatbot")
async def chatbot(pregunta: str = Form()):
    data = {"pregunta": pregunta}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url=URL_N8N, json=data)
            response.raise_for_status()
            
            # Si N8N responde con datos, intentar extraer la respuesta
            try:
                response_data = response.json() if response.content else {}
            except:
                response_data = {}
            
    except httpx.HTTPError as e:
        print(f"Error al enviar datos a N8N: {e}")
        # Si N8N no está disponible, generar respuesta local
        respuesta_local = "No se logro conectar con el servidor"
        return {
            "status": "Respuesta generada localmente (N8N no disponible)", 
            "n8n_status": "offline",
            "pregunta": pregunta,
            "respuesta": respuesta_local
        }
    
    return {
        "status": "Datos enviados correctamente", 
        "n8n_status": response.status_code,
        "pregunta": pregunta,
        "Respuesta": response_data.get("Respuesta","Sin respuesta generada")
    }
