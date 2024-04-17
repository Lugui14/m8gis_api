from .default_service import DefaultService
from repositories.natju_repository import NatjuRepository

class NatjuService(DefaultService):
  def __init__(self):
    super().__init__(NatjuRepository)