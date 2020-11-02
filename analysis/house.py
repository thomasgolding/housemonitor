from datetime import datetime
import os
from typing import Optional
from google.cloud.firestore import Client


def get_client():
    client = Client()
    return client


class House:
    collection_name = "measurement"
    def __init__(self, client: Optional[Client]=None):
        if client:
            self.client=client
        else:
            self.client=get_client()
        


    def get_data(self, start: datetime=datetime(2020,1,1), end: datetime=datetime.now(), collection_name: Optional[str]=None):
        rstart = start.timestamp()
        rend = end.timestamp()
        coll = self.collection_name
        if collection_name:
            coll = collection_name
        collection = self.client.collection(coll)
        q = collection.where("time", ">=", rstart).where("time", "<=", rend)
        docsnaps = q.get()
        docs = [el.to_dict() for el in docsnaps]

        return docs




