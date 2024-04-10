from entities.cnae import Cnae
from .default_repository import DefaultRepository

class CnaeRepository(DefaultRepository):
  def __init__(self):
    super().__init__(Cnae)