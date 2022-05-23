from databases.bridge.bridge import ShipmentUtils

e = ShipmentUtils(engine_type="POSTGRES")
e.create_shipment_table()
