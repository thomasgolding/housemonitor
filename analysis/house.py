from datetime import datetime
from typing import Optional

import pandas as pd
from google.cloud.firestore import Client


def get_client():
    client = Client()
    return client


class House:
    collection_name = "measurements"

    def __init__(self, client: Optional[Client] = None):
        if client:
            self.client = client
        else:
            self.client = get_client()

    def get_data(
        self,
        start: datetime = datetime(2020, 1, 1),
        end: datetime = datetime.now(),
        collection_name: Optional[str] = None,
    ):
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

    def get_nice_data(
        self,
        start: datetime = datetime(2020, 1, 1),
        end: datetime = datetime.now(),
        collection_name: Optional[str] = None,
    ):
        d = self.get_data(start=start, end=end, collection_name=collection_name)
        df = pd.DataFrame(d)
        df["time"] = df["time"].apply(datetime.fromtimestamp)
        df = df.sort_values("time")
        df.set_index("time", drop=True, inplace=True)
        return df

    def list_collections(self):
        collections = [el.id for el in self.client.collections()]
        _ = [print(el) for el in collections]

    def delete_collection(self, collection_name: str) -> None:
        collection = self.client.collection(collection_name)
        docs = [el for el in collection.list_documents()]
        ndocs = len(docs)
        _ = [el.delete() for el in docs]
        print(f"Deleted {str(ndocs)} documents for collection = {collection_name}")
