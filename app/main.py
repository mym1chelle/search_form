from fastapi import FastAPI, Request, Response, status, Depends
from tinydb import TinyDB
from urllib import parse
from .engine import get_type, get_templates
from constants import TEMPLATES_MAIN

app = FastAPI()


def get_db():
    try:
        db = TinyDB('main_db.json')
        if not db.all():
            for string in TEMPLATES_MAIN:
                db.insert(string)
        yield db
    finally:
        db.close()


@app.post("/get_form")
async def get_template(
        request: Request,
        response: Response,
        db=Depends(get_db)):
    body = await request.body()
    request_body = dict(parse.parse_qsl(body.decode()))
    request_all = parse.parse_qsl(body.decode())
    if request_body == {}:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return []
    if len(request_body) != len(request_all):
        response.status_code = status.HTTP_409_CONFLICT
        return []
    fields = set([get_type(item) for item in request_all])
    return get_templates(fields, db.all())
