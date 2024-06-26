from typing import TypeVar
from extensions import db

T = TypeVar('T', bound=db.Model)

class DefaultRepository():

  def __init__(self, entity: T) -> None:
    self.entity = entity
  
  def get_all(self, page: int = 0, per_page: int = 20):
    return self.entity.query.limit(per_page).offset(page * per_page).all()
  
  def get_by_id(self, id: int):
    return self.entity.query.get(id)
  
  def create(self, entity):
    created = self.entity()
    for key in entity:
      setattr(created, key, entity[key])

    db.session.add(created)
    db.session.commit()
    return entity
  
  def update(self, entity):
    updated = self.get_by_id(entity.id)

    for key in entity:
      setattr(updated, key, entity[key])
      
    db.session.commit()
    return entity
  
  def delete(self, id: int):
    entity = self.get_by_id(id)
    db.session.delete(entity)
    db.session.commit()

