from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.routes import router


app = FastAPI(
    title="RAGForge API",
    description="Production-ready RAG Framework API",
    version="0.13.0",
)

app.include_router(router)


@app.get("/", include_in_schema=False)
def root():

    return RedirectResponse(url="/docs")
