from apps.apis.v1 import healthcheck
from apps.apis.v1 import cache
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(healthcheck.router,
                          prefix='/healthcheck',
                          tags=['healthcheck'])
api_router.include_router(cache.router,
                          prefix='/api/v1/cache',
                          tags=['cache'])
