from pathlib import Path

from loaders.loader_factory import LoaderFactory

file = Path(
    "data/uploads/example.pdf"
)

loader = LoaderFactory.create(file)

document = loader.load(file)

print(document.id)

print(document.source)

print(len(document.text))