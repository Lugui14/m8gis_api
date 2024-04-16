from entities.estabelecimento import Estabelecimento
from entities.cnae import Cnae
from .default_repository import DefaultRepository
from sqlalchemy.orm import joinedload

class EstabelecimentoRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Estabelecimento)

  # def get_all(self, page: int):
  #   return self.entity.query.options(joinedload(self.entity.cnae)).limit(100).offset((page - 1) * 100).all()  

  def get_by_cnpj(self, cnpj: int, ):
    return self.entity.query \
                      .filter(Estabelecimento.id == cnpj) \
                      .all()
  