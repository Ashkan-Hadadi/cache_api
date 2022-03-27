from fastapi import APIRouter

from app.apis.v1 import activity
from app.apis.v1 import configuration
from app.apis.v1 import healthcheck
from app.apis.v1 import redirect

api_router = APIRouter()

api_router.include_router(healthcheck.router,
                          prefix='/healthcheck',
                          tags=['healthcheck'])
