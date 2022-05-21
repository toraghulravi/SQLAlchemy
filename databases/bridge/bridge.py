from databases.runner import transcation_isolation

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Any

BASE = declarative_base()


class Shipment(BASE):
	__tablename__ = 'shipment'
    
	id = Column(Integer, primary_key=True)
	order_number = Column(String)
	ship_service = Column(String)
	requested_warehouse_code = Column(String)
	order_status = Column(String)

class ShipmentUtils(Shipment):
	def __init__(self, *args: Any, **kwargs: Any) -> None:
		super().__init__(*args, **kwargs)

	def __repr__(self) -> str:
		return f"<shipment(id='{self.id}', order_number='{self.order_number}', ship_service={self.ship_service}, requested_warehouse_code={self.requested_warehouse_code}, order_status={self.order_status}>"

	@transcation_isolation
	def get_shipment(self, session: Session) -> str:
		return session.query(Shipment).first()
