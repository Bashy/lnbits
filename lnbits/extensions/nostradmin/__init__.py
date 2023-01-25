from fastapi import APIRouter
from starlette.staticfiles import StaticFiles

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_nostradmin")

nostradmin_static_files = [
    {
        "path": "/nostradmin/static",
        "app": StaticFiles(directory="lnbits/extensions/nostradmin/static"),
        "name": "nostradmin_static",
    }
]

nostradmin_ext: APIRouter = APIRouter(prefix="/nostradmin", tags=["nostradmin"])


def nostr_renderer():
    return template_renderer(["lnbits/extensions/nostradmin/templates"])


from .views import *  # noqa
from .views_api import *  # noqa
