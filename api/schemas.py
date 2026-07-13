from pydantic import BaseModel


class ChatRequest(BaseModel):

    question: str


class SourceResponse(BaseModel):

    source: str

    page: int | None

    score: float

    retriever: str


class ChatResponse(BaseModel):

    answer: str

    sources: list[SourceResponse]


class HealthResponse(BaseModel):

    status: str


class RetrieveRequest(BaseModel):

    question: str

    top_k: int = 5


class RetrievalResult(BaseModel):

    chunk_id: str

    text: str

    source: str

    page: int | None

    score: float

    retriever: str


class RetrieveResponse(BaseModel):

    results: list[RetrievalResult]


class IndexResponse(BaseModel):

    success: bool

    filename: str

    chunks: int

    message: str
