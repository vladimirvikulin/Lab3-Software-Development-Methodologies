from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {
        'student': 'Vikulin Volodymyr',
        'City': 'Kyiv',
        'University': 'KPI',
        'Faculty': 'FIOT',
        'group': 'IM-11',
        'Birthday': '15.04.2004'
    }
