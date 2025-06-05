# 🤖 Integración N8N + FastAPI para Chatbot Web

Este repositorio contiene la implementación completa de un chatbot interactivo que integra **N8N** como motor de procesamiento conversacional con **FastAPI** como servidor web que renderiza una interfaz moderna para la interacción del usuario.

![Workflow N8N](image/workflow.png)
*Workflow de N8N configurado como chatbot*

![Interfaz Web](image/interfaz.png)
*Formulario web responsive desarrollado con Bootstrap*

---

## 🏗️ Arquitectura del Sistema

```plaintext
┌─────────────┐    HTTP POST     ┌─────────────┐    Webhook     ┌─────────────┐
│   Usuario   │ ──────────────► │  FastAPI    │ ──────────────► │     N8N     │
│ (Frontend)  │                 │  (Backend)  │                 │ (Chatbot)   │
└─────────────┘ ◄────────────── └─────────────┘ ◄────────────── └─────────────┘
      ▲                JSON Response            HTTP Response           │
      │                                                                 │
      └─────────────────── Respuesta renderizada ──────────────────────┘
```

### Componentes principales:

1. **🎨 Frontend (HTML + Bootstrap + JavaScript)**
   - Formulario interactivo para enviar preguntas
   - Interfaz responsive y moderna
   - Manejo de estados (cargando, éxito, error)

2. **⚡ Backend (FastAPI)**
   - Servidor web que renderiza el formulario
   - Endpoint `/chatbot` que procesa las preguntas
   - Integración con N8N mediante HTTP requests

3. **🧠 N8N (Motor del Chatbot)**
   - Workflow configurado como chatbot
   - Procesamiento de lenguaje natural
   - Lógica conversacional avanzada

---

## 🔄 Flujo de Funcionamiento

### 1. **Inicialización del Usuario**
```
Usuario accede a: http://localhost:8000
```

### 2. **Renderizado del Formulario**
- FastAPI sirve la página HTML con el formulario
- El usuario ve una interfaz moderna con Bootstrap
- Campo de texto para escribir la pregunta

### 3. **Envío de Pregunta**
```javascript
// Frontend envía la pregunta
const formData = new FormData();
formData.append('pregunta', pregunta);

fetch('/chatbot', {
    method: 'POST', 
    body: formData
})
```

### 4. **Procesamiento en FastAPI**
```python
@app.post("/chatbot")
async def chatbot(pregunta: str = Form()):
    data = {"pregunta": pregunta}
    
    # Enviar a N8N
    async with httpx.AsyncClient() as client:
        response = await client.post(url=URL_N8N, json=data)
        
    # Procesar respuesta
    response_data = response.json()
    return {"Respuesta": response_data.get("Respuesta")}
```

### 5. **Procesamiento en N8N**
- N8N recibe la pregunta vía webhook
- Procesa el texto usando su motor conversacional
- Genera una respuesta inteligente
- Devuelve la respuesta a FastAPI

### 6. **Respuesta al Usuario**
- FastAPI recibe la respuesta de N8N
- La envía de vuelta al frontend como JSON
- JavaScript renderiza la respuesta en tiempo real

---

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.8+
- N8N instalado y ejecutándose
- Node.js (para N8N)

### 1. **Clonar el repositorio**
```powershell
git clone <repository-url>
cd N8N
```

### 2. **Instalar dependencias de Python**
```powershell
pip install -r requirements.txt
```

### 3. **Configurar variables de entorno**
Crear archivo `.env`:
```env
N8N_URL=http://localhost:5678/webhook-test/request
```

### 4. **Importar workflow en N8N**
- Abrir N8N en `http://localhost:5678`
- Importar el archivo `Chat_bot_fastapi.json`
- Activar el workflow

### 5. **Ejecutar FastAPI**
```powershell
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6. **Acceder a la aplicación**
```
http://localhost:8000
```

---

## 📁 Estructura del Proyecto

```
N8N/
├── 📄 main.py                 # Servidor FastAPI principal
├── 📄 requirements.txt        # Dependencias de Python
├── 📄 Chat_bot_fastapi.json   # Workflow de N8N exportado
├── 📄 .env                    # Variables de entorno
├── 📁 templates/
│   └── 📄 index.html          # Interfaz web del chatbot
└── 📁 image/
    ├── 🖼️ workflow.png        # Captura del workflow N8N
    └── 🖼️ interfaz.png        # Captura de la interfaz web
```

---

## 🔧 Endpoints de la API

### `GET /`
- **Descripción**: Renderiza la página principal con el formulario
- **Respuesta**: HTML page

### `POST /chatbot`
- **Descripción**: Procesa preguntas y las envía a N8N
- **Parámetros**: 
  - `pregunta` (form-data): Texto de la pregunta del usuario
- **Respuesta**:
```json
{
  "status": "Datos enviados correctamente",
  "n8n_status": 200,
  "pregunta": "¿Cómo estás?",
  "Resouesta": "¡Estoy muy bien, gracias por preguntar!"
}
```
