from pathlib import Path
import shutil
from fastapi.responses import RedirectResponse

from fastapi import (
    APIRouter,
    File,
    HTTPException,
    UploadFile,
)

from api.schemas import (
    ChatRequest,
    ChatResponse,
    IndexResponse,
    RetrieveRequest,
    RetrieveResponse,
    RetrievalResult,
    SourceResponse,
)

from services.pipeline_service import PipelineService


router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

pipeline = PipelineService()

# İlk açılışta örnek dokümanı indeksle
pipeline.index(Path("data/uploads/example.pdf"))


# ---------------------------------------------------
# Health
# ---------------------------------------------------


@router.get("/")
def root():

    return RedirectResponse(url="/docs")


# ---------------------------------------------------
# Index Document
# ---------------------------------------------------


@router.post(
    "/index",
    response_model=IndexResponse,
)
def index_document(
    file: UploadFile = File(...),
):

    suffix = Path(file.filename).suffix.lower()

    if suffix not in {
        ".pdf",
        ".docx",
    }:

        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX are supported.",
        )

    destination = UPLOAD_DIR / file.filename

    with destination.open("wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer,
        )

    qa = pipeline.index(destination)

    return IndexResponse(
        success=True,
        filename=file.filename,
        chunks=len(qa.retriever.store.chunks),
        message="Document indexed successfully.",
    )


# ---------------------------------------------------
# Chat
# ---------------------------------------------------


@router.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
):

    if not pipeline.is_ready():

        raise HTTPException(
            status_code=400,
            detail="No document indexed.",
        )

    response = pipeline.chat(request.question)

    sources = [
        SourceResponse(
            source=result.source.name,
            page=result.page,
            score=result.score,
            retriever=result.retriever,
        )
        for result in response["sources"]
    ]

    return ChatResponse(
        answer=response["answer"],
        sources=sources,
    )


# ---------------------------------------------------
# Retrieve
# ---------------------------------------------------


@router.post(
    "/retrieve",
    response_model=RetrieveResponse,
)
def retrieve(
    request: RetrieveRequest,
):

    if not pipeline.is_ready():

        raise HTTPException(
            status_code=400,
            detail="No document indexed.",
        )

    results = pipeline.qa.retriever.hybrid_retrieve(
        query=request.question,
        top_k=request.top_k,
    )

    return RetrieveResponse(
        results=[
            RetrievalResult(
                chunk_id=result.chunk.id,
                text=result.chunk.text,
                source=result.source.name,
                page=result.page,
                score=result.score,
                retriever=result.retriever,
            )
            for result in results
        ]
    )
