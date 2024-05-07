from .default_service import DefaultService
from repositories.natju_repository import NatjuRepository

class NatjuService(DefaultService):
  def __init__(self):
    super().__init__(NatjuRepository)

  def get_all(self, page: int = 0, per_page: int = 1000):
    entities = []
    for entity in self.repository.get_all(page, per_page):
      entities.append(self._serialize(entity))
    
    return entities