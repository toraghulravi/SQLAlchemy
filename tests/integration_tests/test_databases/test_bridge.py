from databases.bridge.bridge import ShipmentUtils as BridgeShipment

class TestBridge:
    ENGINE_TYPE: str = "POSTGRES"
    def test_create_table(self):
        bridge_shipment = BridgeShipment(engine_type=TestBridge.ENGINE_TYPE)
        assert bridge_shipment.has_table() == False

        bridge_shipment.create_shipment_table()
        assert bridge_shipment.has_table() == True

    def test_drop_table(self):
        bridge_shipment = BridgeShipment(engine_type=TestBridge.ENGINE_TYPE)
        assert bridge_shipment.has_table() == True

        bridge_shipment.drop_table()
        assert bridge_shipment.has_table() == False
