import os

from google.cloud import firestore
from housemonitor.detect_platform_pi import pi_version
from housemonitor.measurement import Measurement

if pi_version():
    from housemonitor.pi_get_humtemp import get_humtemp

    collection_name = "measurements"
else:
    from housemonitor.simulate_get_humtemp import get_humtemp

    collection_name = "testcollection"


# check
def run():
    # check environment varibles
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        print("Credentials not provided. Set environment variable")
        print("GOOGLE_APPLICATION_CREDENTIALS to path of credentials jsonfile.")
        return

    fs_client = firestore.Client()
    temperature, humidity = get_humtemp()
    measurement = Measurement(
        fs_client=fs_client,
        temperature=temperature,
        humidity=humidity,
        collection_name=collection_name,
    )
    measurement.save_measurement()


if __name__ == "__main__":
    run()
