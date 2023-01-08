from fastapi import FastAPI, Request, Response, status, Depends
from starlette.responses import JSONResponse
from tinydb import TinyDB
from urllib import parse
from .engine import get_type, get_templates
from constants import TEMPLATES_MAIN

app = FastAPI()


def get_db():
    try:
        db = TinyDB('main_db.json')
        if not db.all():
            for template in TEMPLATES_MAIN:
                db.insert(template)
        yield db
    finally:
        db.close()


@app.post("/get_form")
async def get_template(
        request: Request,
        response: Response,
        db=Depends(get_db)) -> Response | JSONResponse | list:
    request_body = await request.body()
    body_dict = dict(parse.parse_qsl(request_body.decode()))
    body_all = parse.parse_qsl(request_body.decode())
    if body_dict == {}:
        response.status_code = status.HTTP_406_NOT_ACCEPTABLE
        return []
    if len(body_dict) != len(body_all):
        response.status_code = status.HTTP_409_CONFLICT
        return []
    form_fields = [
        {'name': key, 'value': value}
        for key, value in body_dict.items()
    ]
    dict_type_fields = dict()
    for field in form_fields:
        dict_type_fields.update(get_type(field))
    found_template = get_templates(dict_type_fields, db.all())
    if found_template:
        return Response(content=found_template, media_type="application/json")
    return JSONResponse(content=dict_type_fields)
