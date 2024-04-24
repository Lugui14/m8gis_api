from .default_service import DefaultService
from repositories.endereco_repository import EnderecoRepository

class EnderecoService(DefaultService):
  def __init__(self):
    super().__init__(EnderecoRepository)

  def fill_lat_long(self): 
    enderecos = self.repository.get_all_lat_long_null()  
    for endereco in enderecos:
      street = endereco.Endereco.numero + ' ' + endereco.Endereco.logradouro
      city = endereco.descricao
      county = endereco.Endereco.bairro
    
      # Consulta api colocando os paramentros street=Rua+numero, city=cidade, county=bairro (delcarados acima)
      # e retorna um json com a latitude e longitude
      # atribui para objeto endereco.Endereco.latitude e endereco.Endereco.longitude
      # salva o endereco.Endereco pelo self.repository.save(endereco.Endereco)
      # retorna resultados