from housemonitor.save_measurement import prepare_document
from  unittest.mock import patch


def test_prepare_document():
    t = 1.
    temperature = 10.
    humidity = 42.
    doc = prepare_document(temperature=temperature, humidity=humidity)
    
    assert abs(doc["temperature"] - temperature) < 0.001
    assert abs(doc["humidity"] - humidity) < 0.001


def test_prepare_document_none():
    t = 1.
    temperature = None
    humidity = 42.
    doc = prepare_document(temperature=temperature)
    
    assert not doc.get("temperature")



def test_time():
    with patch("housemonitor.save_measurement.get_current_timestamp") as pfunc:
        pfunc.return_value = 1
        doc = prepare_document(10,10)
        assert abs(doc["time"] - 1) < 0.001

