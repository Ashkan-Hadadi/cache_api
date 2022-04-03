import json
import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from apps.core.utils.logger import JSONFormatter


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request.state.time_started = time.time()
        response = await call_next(request)
        process_time = time.time() - request.state.time_started
        response.headers["X-Process-Time"] = str(process_time)

        return response


class ActivityLoggerMiddleWare(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler('cache.log')
        file_handler.setFormatter(JSONFormatter())
        self.logger.addHandler(file_handler)

    async def dispatch(self, request: Request, call_next):
        if 'activity' not in request.url.path:
            return await call_next(request)
        try:
            request.state.body = await request.json()
        except json.decoder.JSONDecodeError:
            request.state.body = {}
        response = await call_next(request)
        self.logger.info(None, extra={'request': request, 'response': response})

        return response
