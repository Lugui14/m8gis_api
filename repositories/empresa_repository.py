from entities.empresa import Empresa
from .default_repository import DefaultRepository

class EmpresaRepository(DefaultRepository):
    def __init__(self):
        super().__init__(Empresa)