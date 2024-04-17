from typing import List, Dict
from .default_service import DefaultService
from repositories.empresa_repository import EmpresaRepository

class EmpresaService(DefaultService):
  def __init__(self):
    super().__init__(EmpresaRepository)

  def get_all(self, page: int) -> List[Dict]:
    empresas = self.repository.get_all(page)
    return [self._serialize(empresa) for empresa in empresas]

  def get_by_id(self, id: int) -> Dict:
    empresa = self.repository.get_by_id(id)
    return self._serialize(empresa)
  
  def get_by_cnae(self, cnae: int) -> List[Dict]:
    empresas = self.repository.get_by_cnae(cnae)
    return [self._serialize(empresa) for empresa in empresas]
  
  def get_filtered(self, filters: Dict) -> List[Dict]:
    empresas = self.repository.get_filtered(filters)
    return [self._serialize(empresa) for empresa in empresas]

  def _serialize(self, empresa) -> Dict:
    # Esta função assume que sua entidade `Empresa` é um modelo SQLAlchemy
    # e converte para um dicionário. Você pode precisar ajustar isso
    # para se adequar à estrutura exata de sua entidade `Empresa`.
    return {
    	'id': empresa.id,
      'cnpj_basico': empresa.cnpj_basico,
      'porte': empresa.porte,
      'razao_social': empresa.razao_social,
      'natureza_juridica_id': empresa.natureza_juridica_id,
      'capital_social': empresa.capital_social,
      'cnae_principal_id': empresa.cnae_principal_id,
      'cnae_descricao': empresa.cnae.descricao if empresa.cnae else None,
      # Inclua outros campos conforme necessário
    }