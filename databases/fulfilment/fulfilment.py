from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

from databases.common import transcation_isolation
from databases.runner import Engine

BASE = declarative_base()


class Shipment(BASE):
	__tablename__ = 'shipment'

	ShipmentId = Column(Integer, primary_key=True)
	CompanyId = Column(Integer)
	WarehouseId = Column(Integer)
	ShipmentStatusId = Column(Integer)

class ShipmentUtils(Engine):
	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)

	def __repr__(self) -> str:
		return f"<ShipmentId(id='{self.ShipmentId}', CompanyId='{self.CompanyId}', WarehouseId={self.WarehouseId}, ShipmentStatusId={self.ShipmentStatusId}>"

	@transcation_isolation
	def create_shipment_table(self, session: Session) -> None:
		BASE.metadata.create_all(self.engine)

	@transcation_isolation
	def insert_shipment(self, session: Session) -> None:
		shipment = Shipment(
			ShipmentId=1,
			CompanyId=1,
			WarehouseId=1,
			ShipmentStatusId=1
		)
		session.add(shipment)

	@transcation_isolation
	def get_shipment_count(self, session: Session) -> str:
		return session.query(Shipment).count()
