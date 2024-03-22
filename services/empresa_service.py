from repositories.empresa_repository import EmpresaRepository
from .default_service import DefaultService

class EmpresaService(DefaultService):
    def __init__(self):
        super().__init__(EmpresaRepository)