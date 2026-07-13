from pathlib import Path

from services.pipeline_service import (
    PipelineService,
)


qa = PipelineService().build(

    Path(
        "data/uploads/example.pdf"
    )

)

while True:

    question = input(
        "\nQuestion : "
    )

    if question.lower() == "exit":

        break

    response = qa.ask(
        question
    )

    print()

    print(
        response["answer"]
    )

    print()

    print("Sources")

    for result in response["sources"]:

        print(

            f"- {result.source.name}"

            f" | page={result.page}"

            f" | score={result.score:.3f}"

        )