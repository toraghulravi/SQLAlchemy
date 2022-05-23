from sqlalchemy import Column, Integer, String, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

from databases.common import transcation_isolation
from databases.runner import Engine

BASE = declarative_base()


class Shipment(BASE):
	__tablename__ = 'shipment'
    
	id = Column(Integer, primary_key=True)
	order_number = Column(String)
	ship_service = Column(String)
	requested_warehouse_code = Column(String)
	order_status = Column(String)

class ShipmentUtils(Engine):
	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)

	def _inspect(self):
		return inspect(self.engine)

	@transcation_isolation
	def create_shipment_table(self, session: Session) -> None:
		BASE.metadata.create_all(self.engine)

	@transcation_isolation
	def insert_shipment(self, session: Session) -> None:
		shipment = Shipment(
			id=1,
			order_number="1",
			ship_service="air",
			requested_warehouse_code="1",
			order_status="success"
		)
		session.add(shipment)
	
	@transcation_isolation
	def get_shipment_count(self, session: Session) -> int:
		return session.query(Shipment).count()

	@transcation_isolation
	def is_table_exists(self, session: Session) -> bool:
		inspector = self._inspect()
		return inspector.has_table(Shipment.__tablename__)
	
	@transcation_isolation
	def drop_table(self, session: Session) -> None:
		Shipment.__table__.drop(self.engine)
