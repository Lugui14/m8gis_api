from .default_service import DefaultService
from repositories.endereco_repository import EnderecoRepository

class EnderecoService(DefaultService):
  def __init__(self):
    super().__init__(EnderecoRepository)

  def get_municipios(self):
    entities = []
    for entity in self.repository.get_municipios():
      entities.append(self._serialize(entity))
    
    return entities