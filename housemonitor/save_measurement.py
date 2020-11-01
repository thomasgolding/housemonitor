from datetime import datetime
from typing import Optional, Dict
import os

from google.cloud import firestore





def get_current_timestamp():
    return datetime.now().timestamp()


def prepare_document(temperature: Optional[float]=None, humidity: Optional[float]=None) -> Dict[str, float]:
    measurement = {"time": get_current_timestamp()}
    if isinstance(temperature, float):
        measurement.update({"temperature": temperature})
    if isinstance(humidity, float):
        measurement.update({"humidity": humidity})

    return measurement


def save(temperature: Optional[float]=None, humidity: Optional[float]=None) -> None:
    measurement = prepare_document(temperature=temperature, humidity=humidity)
    print(measurement)
    db = firestore.Client(project=os.environ.get("GCP_PROJECT"))
    collection = db.collection("measurement")
    doc = collection.document()
    res = doc.set(measurement)
    print(res)


    