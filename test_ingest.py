from services.ingest_service import IngestService

service = IngestService()

count = service.ingest(
    "data/uploads/example.pdf"
)

print(count)