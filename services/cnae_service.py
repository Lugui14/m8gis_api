from .default_service import DefaultService
from repositories.cnae_repository import CnaeRepository

class CnaeService(DefaultService):
  def __init__(self):
    super().__init__(CnaeRepository)