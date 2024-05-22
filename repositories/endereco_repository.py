from entities.endereco import Endereco, Municipio
from .default_repository import DefaultRepository

class EnderecoRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Endereco)

  def get_all_lat_long_null(self):
    return self.entity.query.join(Municipio, Municipio.id == self.entity.municipio_id).filter(self.entity.latitude == None, self.entity.longitude == None).add_column(Municipio.descricao).all()
  
  def get_municipios(self):
    return Municipio.query.all()