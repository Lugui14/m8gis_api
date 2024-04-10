from typing import TypeVar
from sqlalchemy import inspect
from repositories.default_repository import DefaultRepository

T = TypeVar('T', bound=DefaultRepository)

class DefaultService(): 
  def __init__(self, Repository: T) -> None:
    self.repository = Repository()

  def get_all(self, page: int = 0, per_page: int = 20):
    entities = []
    for entity in self.repository.get_all(page, per_page):
      entities.append(self._serialize(entity))
    
    return entities
  
  def get_by_id(self, id: int):
    return self.repository.get_by_id(id)
  
  def create(self, entity):
    self.before_create(entity)
    created = self.repository.create(entity)
    self.after_create(created)
    return created

  def update(self, entity):
    self.before_update(entity)
    updated = self.repository.update(entity)
    self.after_update(updated)
    return updated

  def delete(self, id: int):
    self.before_delete(id)
    self.repository.delete(id)
    self.after_delete(id)
    return { 'message': 'Deleted successfully' }

  def before_create(self, entity):
    # Override this method in the service class
    pass

  def before_update(self, entity):
    # Override this method in the service class
    pass

  def before_delete(self, id: int):
    # Override this method in the service class
    pass

  def after_create(self, entity):
    # Override this method in the service class
    pass

  def after_update(self, entity):
    # Override this method in the service class
    pass

  def after_delete(self, id: int):
    # Override this method in the service class
    pass

  def _serialize(self, entity):
    return {
        c.key: getattr(entity, c.key)
        for c in inspect(entity).mapper.column_attrs
    }