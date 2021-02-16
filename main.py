import random
import settings

from slugify import slugify

from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import Response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from questions import questions

templates = Jinja2Templates(directory="templates")


def get_context_data(request, question, perm=False):
    permalink = app.url_path_for("permalink", question=slugify(question))

    return {
        "question": question,
        "permalink": permalink,
        "perm": perm,
        "request": request,
    }


valid_routes = {}
for question in questions:
    slug = slugify(question)
    valid_routes[slug] = question


def permalink(request):
    slug = request.path_params["question"]
    try:
        question = valid_routes[slug]
    except KeyError:
        return Response("Not found", status_code=404)
    else:
        return templates.TemplateResponse(
            "question.html", get_context_data(request, question, perm=True),
        )


def home(request):
    question = random.choice(questions)

    return templates.TemplateResponse(
        "question.html", get_context_data(request, question)
    )


routes = [
    Route("/", home),
    Route("/{question}", permalink),
    Mount("/static", StaticFiles(directory="static")),
]

app = Starlette(debug=settings.DEBUG, routes=routes)
