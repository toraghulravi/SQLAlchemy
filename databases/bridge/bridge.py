import ConfigParser

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

BASE = declarative_base()


class Shipment(BASE):
	__tablename__ = 'shipment'
    
	id = Column(Integer, primary_key=True)
    order_number = Column(String)
    ship_service = Column(String)
    requested_warehouse_code = Column(String)
    order_status = Column(String)

	def __repr__(self):
        return f"<shipment(id='{self.id}', order_number='{self.order_number}', ship_service={self.ship_service}, requested_warehouse_code={self.requested_warehouse_code}, order_status={self.order_status}>"

	class ShipmentUtils:
		pass

