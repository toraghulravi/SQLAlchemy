import sys
from pathlib import Path

path = str(Path(__file__).parent.parent.parent.parent.resolve())
sys.path.insert(0, path)

from databases.bridge.bridge import ShipmentUtils as BridgeShipment

class TestBridge:
    ENGINE_TYPE: str = "POSTGRES"
    def test_create_table(self):
        bridge_shipment = BridgeShipment(engine_type=TestBridge.ENGINE_TYPE)
        assert bridge_shipment.is_table_exists() is False

        bridge_shipment.create_shipment_table()
        assert bridge_shipment.is_table_exists() is True

    def test_drop_table(self):
        bridge_shipment = BridgeShipment(engine_type=TestBridge.ENGINE_TYPE)
        assert bridge_shipment.is_table_exists() == True

        bridge_shipment.drop_table()
        assert bridge_shipment.is_table_exists() == False
