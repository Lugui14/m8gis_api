from entities.empresa import Empresa
from entities.natureza_juridica import NaturezaJuridica
from entities.cnae import Cnae
from .default_repository import DefaultRepository
from sqlalchemy.orm import joinedload

class NatjuRepository(DefaultRepository):
  def __init__(self):
    super().__init__(NaturezaJuridica)

  # def get_all(self, page: int):
  #   return self.entity.query.options(joinedload(self.entity.cnae)).limit(100).offset((page - 1) * 100).all()  

 
  