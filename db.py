fake_db = [
    {
        "id": 1,
        "name": "Análisis de datos",
        "description": "Proyecto de análisis de datos tipo EDA"
    },
    {
        "id": 2,
        "name": "Desarrollo Web",
        "description": "Creación de una plataforma e-commerce con React y Node.js"
    },
    {
        "id": 3,
        "name": "Aplicación Móvil",
        "description": "Desarrollo de una app móvil para seguimiento de fitness"
    },
    {
        "id": 4,
        "name": "Sistema de Gestión",
        "description": "Implementación de un sistema de gestión de inventarios para pequeñas empresas"
    },
    {
        "id": 5,
        "name": "Machine Learning",
        "description": "Modelo de predicción de ventas utilizando algoritmos de machine learning"
    },
    {
        "id": 6,
        "name": "Automatización de Procesos",
        "description": "Automatización de procesos internos utilizando Python y RPA"
    },
    {
        "id": 7,
        "name": "Ciberseguridad",
        "description": "Evaluación y mejora de la seguridad de la red para una empresa financiera"
    },
    {
        "id": 8,
        "name": "Realidad Virtual",
        "description": "Desarrollo de una experiencia de realidad virtual para entrenamiento médico"
    },
    {
        "id": 9,
        "name": "Blockchain",
        "description": "Creación de una solución basada en blockchain para la trazabilidad de productos"
    },
    {
        "id": 10,
        "name": "Internet de las Cosas (IoT)",
        "description": "Proyecto de IoT para monitoreo y control de dispositivos en el hogar"
    }
]



def search_project(id:int)-> dict:
    """ Busca en toda la base de datos el proyecto con el nombre indicado"""
    for proyecto in fake_db:
        if proyecto["id"] == id:
            return proyecto["description"]
    return "No se encontratron proyectos con ese id"
    
