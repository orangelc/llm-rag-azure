from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from utils.env_loader import load_env
from chains.qa_chain import get_qa_chain
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
logger = logging.getLogger("uvicorn.error")


config = load_env()
qa_chain = get_qa_chain(config)

@app.get("/ask")
def ask(q: str = Query(..., description="Pregunta para el LLM")):
    try:
        logger.info(f"Consulta recibida: {q}")
        result = qa_chain.invoke(q)

        return {
            "respuesta": result
        }

    except Exception as e:
        logger.error(f"Error procesando la consulta: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")