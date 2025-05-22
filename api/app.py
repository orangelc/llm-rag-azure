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

REQUIRED_ENV_VARS = [
    "OPENAI_API_KEY",
    "PINECONE_API_KEY",
    "PINECONE_ENVIRONMENT",
    "PINECONE_INDEX_NAME"
]

def check_env_vars():
    missing = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    if missing:
        raise HTTPException(
            status_code=401,
            detail=f"Faltan variables de entorno: {', '.join(missing)}"
        )


config = load_env()
qa_chain = get_qa_chain(config)

@app.get("/ask")
def ask(q: str = Query(..., description="Pregunta para el LLM")):
    try:
        check_env_vars()
        logger.info(f"Consulta recibida: {q}")
        result = qa_chain.invoke(q)

        return {
            "respuesta": result
        }

    except Exception as e:
        logger.error(f"Error procesando la consulta: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")