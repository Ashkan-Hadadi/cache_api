import uvicorn
from apps.apis.v1 import api_router as api_router_v1
from apps.core.middlewares import ActivityLoggerMiddleWare
from apps.core.middlewares import ProcessTimeMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import settings


def get_application() -> FastAPI:
    _app = FastAPI(title=settings.PROJECT_NAME,
                   openapi_url='/openapi.json')
    _app.include_router(api_router_v1,
                        prefix='/api/v1')

    CORSMiddleware(_app, allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
                   allow_credentials=True,
                   allow_methods=['*'],
                   allow_headers=['*'])
    ProcessTimeMiddleware(_app)
    ActivityLoggerMiddleWare(_app)

    return _app


app = get_application()

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=9000)
