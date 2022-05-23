from databases.bridge.bridge import ShipmentUtils

e = ShipmentUtils(engine_type="POSTGRES")
print(e)
e.create_shipment_table()
