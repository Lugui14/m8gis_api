from entities.empresa import Empresa
from entities.cnae import Cnae
from .default_repository import DefaultRepository
from sqlalchemy.orm import joinedload

class EmpresaRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Empresa)

  # def get_all(self, page: int):
  #   return self.entity.query.options(joinedload(self.entity.cnae)).limit(100).offset((page - 1) * 100).all()  

  def get_by_cnae(self, cnae_id: int, ):
    return self.entity.query \
      								.join(self.entity.cnae) \
                      .filter(Cnae.id == cnae_id) \
                      .options(joinedload(self.entity.cnae)) \
                      .all()
  