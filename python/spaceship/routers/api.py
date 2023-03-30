from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'student': 'Vikulin Volodymyr',
        'group': 'IM-11',
        'Country': 'Ukraine',
        'City': 'Kyiv',
        'University': 'KPI'
    }
