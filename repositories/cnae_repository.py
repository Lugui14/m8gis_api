from entities.cnae import Cnae
from .default_repository import DefaultRepository

class CnaeRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Cnae)

  def get_all(self, page: int = 0, per_page: int = 20):
    return self.entity.query.distinct(Cnae.descricao).limit(per_page).offset(page * per_page).all()