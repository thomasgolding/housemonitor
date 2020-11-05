from datetime import datetime
from typing import Dict, Optional

from google.cloud.firestore import Client


class Measurement:
    collection_name = "testcollection"

    def __init__(
        self,
        fs_client: Client,
        temperature: Optional[float] = None,
        humidity: Optional[float] = None,
        collection_name: Optional[str] = None,
    ):
        self.fs_client = fs_client
        self.temperature = temperature
        self.humidity = humidity
        # allow saving in other collections. Used for testing.
        if collection_name:
            self.collection_name = collection_name

    def prepare_doc(self) -> Dict[str, float]:
        measurement = {"time": self.get_current_timestamp()}
        if self.temperature:
            measurement.update({"temperature": self.temperature})
        if self.humidity:
            measurement.update({"humidity": self.humidity})
        return measurement

    def save_measurement(self) -> None:
        measurement_collection = self.fs_client.collection(self.collection_name)
        doc = measurement_collection.document()
        measurement = self.prepare_doc()
        doc.set(measurement)

    @staticmethod
    def get_current_timestamp():
        return datetime.now().timestamp()
