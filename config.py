# from pathlib import Path
from typing import List, Optional
from typing import Union

from pydantic import BaseSettings
from pydantic import validator


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Cache API'
    BACKEND_CORS_ORIGINS: Union[List[str], str] = []
    CACHE_TIMEOUT: int = 300

    APPS = (
        '',
    )

    @validator('BACKEND_CORS_ORIGINS', pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith('['):
            return [i.strip() for i in v.split(',')]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        case_sensitive = True
        env_file = '.env'


settings = Settings()
