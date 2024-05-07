from entities.estabelecimento import Estabelecimento
from entities.endereco import Endereco
from entities.endereco import Municipio
from entities.empresa import Empresa
from entities.cnae import Cnae
from entities.natureza_juridica import NaturezaJuridica
from .default_repository import DefaultRepository
from sqlalchemy import or_
from sqlalchemy.orm import joinedload

class EstabelecimentoRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Estabelecimento)

  # def get_all(self, page: int):
  #  return Estabelecimento.query.join(Endereco).add_columns(Endereco.latitude, Endereco.longitude).limit(20).offset(page * 20).all()

  def get_filtered(self, filters):
    query = Estabelecimento.query.join(Endereco).join(Municipio).join(Empresa)
    if 'id' in filters.keys():
      query = query.filter(Estabelecimento.id == filters['id'])
    if 'cnae' in filters.keys():
      conditions = [Cnae.id == cnae for cnae in filters['cnae']]
      query = query.join(Cnae).filter(or_(*conditions))
    if 'situacao' in filters.keys():
      query = query.filter(Estabelecimento.situacao_cadastral == filters['situacao'])
    if 'matriz' in filters.keys():
      query = query.filter(Estabelecimento.identificador_matriz_filial == filters['matriz'])
    if 'natju' in filters.keys():
      conditions = [NaturezaJuridica.id == natju for natju in filters['natju']]
      query = query.join(NaturezaJuridica).filter(or_(*conditions))
    if 'porte' in filters.keys():
      query = query.filter(Empresa.porte == filters['porte'])
    if 'capital_social_min' in filters.keys():
      query = query.filter(Empresa.capital_social >= filters['capital_social_min'])
    if 'data_abertura' in filters.keys():
      query = query.filter(Estabelecimento.data_inicio_atividade >= filters['data_abertura'])
    if 'cnpj' in filters.keys():
      query = query.filter(Empresa.cnpj_basico == filters['cnpj'])
    if 'razao_social' in filters.keys():
      query = query.filter(Empresa.razao_social == filters['razao_social'])
    if 'numero' in filters.keys():
      query = query.filter(Endereco.numero == filters['numero'])
    if 'logradouro' in filters.keys():
      query = query.filter(Endereco.logradouro == filters['logradouro'].upper())
    if 'cidade' in filters.keys():
      query = query.filter(Municipio.descricao == filters['cidade'].upper()).options(joinedload(Estabelecimento.endereco))

    return query.all()
  
  def get_estab_by_id_with_empresa(id):
      estabelecimento = Estabelecimento.query \
            .join(Estabelecimento.empresa) \
            .join(Empresa.natureza_juridica) \
            .join(Empresa.cnae) \
            .add_columns(
                Estabelecimento.nome_fantasia,
                Estabelecimento.data_inicio_atividade,
                Empresa.razao_social,
                Empresa.capital_social,
                Empresa.natureza_juridica.label('natureza_juridica_descricao'),  # Assume que NaturezaJuridica tem um campo 'descricao'
                Empresa.cnae.label('cnae_descricao')
                # ... outros campos que você deseja retornar
            ) \
            .filter(Estabelecimento.id == id) \
            .first()
        
      return estabelecimento
  def get_by_cnpj(self, cnpj: int, ):
    return self.entity.query \
                      .filter(Estabelecimento.id == cnpj) \
                      .all()
  