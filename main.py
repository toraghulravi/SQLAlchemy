from databases.bridge.bridge import ShipmentUtils as BridgeShipment
from databases.fulfilment.fulfilment import ShipmentUtils as FulfilmentShipment

bridge_shipment = BridgeShipment(engine_type="POSTGRES")
bridge_shipment.create_shipment_table()
bridge_shipment.insert_shipment()
print(bridge_shipment.get_shipment_count())


# TODO M1 doesn't support SQLSERVER yet
"""
fulfilment_shipment = FulfilmentShipment(engine_type="SQLSERVER")
fulfilment_shipment.create_shipment_table()
fulfilment_shipment.insert_shipment()
print(fulfilment_shipment.get_shipment_count())
"""