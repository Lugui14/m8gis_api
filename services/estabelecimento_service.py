from typing import List, Dict
from .default_service import DefaultService
from repositories.estabelecimento_repository import EstabelecimentoRepository
from services.empresa_service import EmpresaService

empresa_service = EmpresaService()


class EstabelecimentoService(DefaultService):
  def __init__(self):
    super().__init__(EstabelecimentoRepository)
    
  def get_estab_by_id_with_empresa(self, id: int) -> Dict:
    estabelecimento = self.repository.get_by_id(id)  # Supondo que este método retorna um único estabelecimento
    if not estabelecimento:
        return None  # Ou manipule de acordo com a necessidade, talvez levantando uma exceção
    
    filters = {
      'cnae': estabelecimento.empresa.cnae_principal_id,
    }

    empresas_relacionadas = empresa_service.get_filtered(filters)
    for empresa in empresas_relacionadas:
      if empresa.get('id') == estabelecimento.empresa.id:
        empresas_relacionadas.remove(empresa)

    # Serializar o estabelecimento incluindo os detalhes da empresa relacionada
    return self._serialize(estabelecimento, empresas_relacionadas, include_empresa=True, include_socios=True, include_address=True, include_relacionadas=True)



  def get_all(self, page: int) -> List[Dict]:
    estabelecimentos = self.repository.get_all(page)
    return [self._serialize_simple(estabelecimento) for estabelecimento in estabelecimentos]

  def get_by_id(self, id: int) -> Dict:
    estabelecimento = self.repository.get_by_id(id)
    return self._serialize(estabelecimento) 
  
  def get_by_cnpj(self, cnpj: int) -> List[Dict]:
    estabelecimentos = self.repository.get_by_cnae(cnpj)
    return [self._serialize(estabelecimento) for estabelecimento in estabelecimentos]
  
  def get_filtered(self, filters: Dict) -> List[Dict]:
    estabelecimentos = self.repository.get_filtered(filters)
    return [self._serialize_simple(estabelecimento) for estabelecimento in estabelecimentos]
  
  def _serialize_empresa(self,empresa_relacionada):
    return {
        'id': empresa_relacionada.get('id'),
        'cnpj_basico': empresa_relacionada.get('cnpj_basico'),
        'porte': empresa_relacionada.get('porte'),
        'razao_social': empresa_relacionada.get('razao_social'),
        'natureza_juridica_id': empresa_relacionada.get('natureza_juridica_id'),
        'capital_social': empresa_relacionada.get('capital_social'),
        'cnae_principal_id': empresa_relacionada.get('cnae_principal_id'),
    }
  
  def _serialize_socio(self,socio_empresa):
    return {
        'id': socio_empresa.socio.id,
        'cpf_cnpj': socio_empresa.socio.cpf_cnpj,
        'nome_socio': socio_empresa.socio.nome_socio,
        'representante_legal': socio_empresa.socio.representante_legal,
        'nome_representante_legal': socio_empresa.socio.nome_representante_legal,
        # ... outros campos do sócio
    }

  def _serialize(self, estabelecimento, empresas_relacionadas, include_address:bool=False, include_empresa: bool = False, include_socios:bool = False, include_relacionadas:bool = False) -> Dict:
    # Esta função assume que sua entidade `Estabelecimento` é um modelo SQLAlchemy
    # e converte para um dicionário. Você pode precisar ajustar isso
    # para se adequar à estrutura exata de sua entidade `Estabelecimento`.
    serialized_data = {
    	'id': estabelecimento.id,
      'cnae': estabelecimento.empresa.cnae.descricao,
      'cnpj_basico': estabelecimento.cnpj_basico,
      'cnpj_ordem': estabelecimento.cnpj_ordem,
      'identificador_matriz_filial': estabelecimento.identificador_matriz_filial,
      'nome_fantasia': estabelecimento.nome_fantasia,
      'data_inicio_atividade': estabelecimento.data_inicio_atividade,
      'endereco_id': estabelecimento.endereco_id,
      'situacao_cadastral': estabelecimento.situacao_cadastral,
      'nome_fantasia':estabelecimento.nome_fantasia,
    }
    if include_empresa and estabelecimento.empresa:
        empresa_data = {
            'id': estabelecimento.empresa.id,
            'razao_social': estabelecimento.empresa.razao_social,
            'capital_social': str(estabelecimento.empresa.capital_social),
            'porte': estabelecimento.empresa.porte,
            'natureza_juridica_descricao': estabelecimento.empresa.natureza_juridica.descricao if estabelecimento.empresa.natureza_juridica else None,
            'cnae_descricao': estabelecimento.empresa.cnae.descricao if estabelecimento.empresa.cnae else None,
        }
            # Aqui você pode adicionar mais campos conforme necessário
        if include_socios:
            empresa_data['socios'] = [
                self._serialize_socio(socio) for socio in estabelecimento.empresa.socio_empresas[:10]
            ]

        if include_relacionadas:
          empresa_data['empresas_relacionadas'] = [
              self._serialize_empresa(empresa) for empresa in empresas_relacionadas[:5]
          ]

    serialized_data['empresa'] = empresa_data
      
    if include_address and estabelecimento.endereco:
      serialized_data['endereco'] = {
        'logradouro': estabelecimento.endereco.logradouro,
        'numero': estabelecimento.endereco.numero,
        'bairro': estabelecimento.endereco.bairro,
        'cidade':estabelecimento.endereco.municipio.descricao if estabelecimento.endereco.municipio else '',
        'cep':estabelecimento.endereco.cep,
        'municipio': estabelecimento.endereco.municipio.descricao if estabelecimento.endereco.municipio else ''
        # ... outros campos do endereço
      }
    return serialized_data
  
  def _serialize_simple(self, estabelecimento) -> Dict:
    return {
        'id': estabelecimento.id,
        'cnpj_basico': estabelecimento.cnpj_basico,
        'nome_fantasia': estabelecimento.nome_fantasia,
        'cnae_id': estabelecimento.empresa.cnae.id if estabelecimento.empresa and estabelecimento.empresa.cnae else None,
        'cnae':estabelecimento.empresa.cnae.descricao if estabelecimento.empresa and estabelecimento.empresa.cnae else None,
        'razao_social': estabelecimento.empresa.razao_social if estabelecimento.empresa else None,
        'cidade': estabelecimento.endereco.municipio.descricao if estabelecimento.endereco and estabelecimento.endereco.municipio else None,
        'situacao_cadastral': estabelecimento.situacao_cadastral,
        'porte': estabelecimento.empresa.porte if estabelecimento.empresa else None
    }
