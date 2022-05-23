from databases.bridge.bridge import ShipmentUtils

e = ShipmentUtils(engine_type="POSTGRES")
e.create_shipment_table()
# e.insert_shipment()
print(e.get_shipment_count())
