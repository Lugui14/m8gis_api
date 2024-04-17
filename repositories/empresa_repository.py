from entities.empresa import Empresa
from entities.cnae import Cnae
from .default_repository import DefaultRepository
from sqlalchemy.orm import joinedload

class EmpresaRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Empresa)

  # def get_all(self, page: int):
  #   return self.entity.query.options(joinedload(self.entity.cnae)).limit(100).offset((page - 1) * 100).all() 

  def get_filtered(self, filters):
    query = self.entity.query
    if 'cnae' in filters:
      query = query.filter(Empresa.cnae_principal_id == filters['cnae'])
    if 'porte' in filters:
      query = query.filter(Empresa.porte == filters['porte'])
    if 'razao_social' in filters:
      query = query.filter(Empresa.razao_social == filters['razao_social']) 
    if 'capital_social_min' in filters:
      query = query.filter(Empresa.capital_social >= filters['capital_social_min'])
    if 'natureza_juridica' in filters:
      query = query.filter(Empresa.natureza_juridica_id == filters['natureza_juridica'])
    # Adicione mais filtros conforme necessário
    return query.all()
 
  def get_by_cnae(self, cnae_id: int, ):
    return self.entity.query \
      								.join(self.entity.cnae) \
                      .filter(Cnae.id == cnae_id) \
                      .options(joinedload(self.entity.cnae)) \
                      .all()
  