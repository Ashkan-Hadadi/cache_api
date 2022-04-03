from fastapi import APIRouter

router = APIRouter()


@router.get('/{key}')
def get_key(key: str):
    pass


@router.get('/')
def get_keys():
    pass


@router.put('/{key}')
def create_or_update_key(key: str):
    pass


@router.delete('/{key}')
def delete_key(key: str):
    pass


@router.delete('/')
def delete_keys():
    pass
