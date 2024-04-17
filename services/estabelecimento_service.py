from typing import List, Dict
from .default_service import DefaultService
from repositories.estabelecimento_repository import EstabelecimentoRepository

class EstabelecimentoService(DefaultService):
  def __init__(self):
    super().__init__(EstabelecimentoRepository)

  def get_all(self, page: int) -> List[Dict]:
    estabelecimentos = self.repository.get_all(page)
    return [self._serialize(estabelecimento) for estabelecimento in estabelecimentos]

  def get_by_id(self, id: int) -> Dict:
    estabelecimento = self.repository.get_by_id(id)
    return self._serialize(estabelecimento)
  
  def get_by_cnpj(self, cnpj: int) -> List[Dict]:
    estabelecimentos = self.repository.get_by_cnae(cnpj)
    return [self._serialize(estabelecimento) for estabelecimento in estabelecimentos]

  def _serialize(self, estabelecimento) -> Dict:
    # Esta função assume que sua entidade `Estabelecimento` é um modelo SQLAlchemy
    # e converte para um dicionário. Você pode precisar ajustar isso
    # para se adequar à estrutura exata de sua entidade `Estabelecimento`.
    return {
    	'id': estabelecimento.id,
      'cnpj_basico': estabelecimento.cnpj_basico,
      'cnpj_ordem': estabelecimento.cnpj_ordem,
      'identificador_matriz_filial': estabelecimento.identificador_matriz_filial,
      'nome_fantasia': estabelecimento.nome_fantasia,
      'data_inicio_atividade': estabelecimento.data_inicio_atividade,
      'empresa_id': estabelecimento.empresa_id,
      'endereco_id': estabelecimento.endereco_id,
      'endereco_completo': {"cidade":estabelecimento.endereco.municipio.descricao ,"logradouro": estabelecimento.endereco.logradouro, "numero":estabelecimento.endereco.numero, "bairro":estabelecimento.endereco.bairro },
      'situacao_cadastral': estabelecimento.situacao_cadastral,      
      # Inclua outros campos conforme necessário
    }