import numpy as np
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

@router.get('/matrix_mult')
def matrix() -> dict:
    matrix_a = np.random.rand(10, 10).tolist()
    matrix_b = np.random.rand(10, 10).tolist()
    product = np.dot(matrix_a, matrix_b).tolist()
    result = {"matrix_a": matrix_a, "matrix_b": matrix_b, "product": product}
    return result