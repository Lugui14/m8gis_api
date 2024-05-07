from .default_service import DefaultService
from repositories.cnae_repository import CnaeRepository

class CnaeService(DefaultService):
  def __init__(self):
    super().__init__(CnaeRepository)

  def get_all(self, page: int = 0, per_page: int = 1000):
    entities = []
    for entity in self.repository.get_all(page, per_page):
      entities.append(self._serialize(entity))
    
    return entities