from unittest.mock import patch
import pytest

from housemonitor.measurement import Measurement

xtemp = 10.1
xhumidity = 80.3
small_diff = 0.001

@pytest.fixture
def measurement():
    m = Measurement(fs_client=1, temperature=xtemp, humidity=xhumidity)
    return m

def test_measurement_docprep(measurement):
    doc = measurement.prepare_doc()
    assert abs(doc["temperature"] - xtemp) < small_diff
    assert abs(doc["humidity"] - xhumidity) < small_diff


def test_prepare_document_none():
    measurement = Measurement(fs_client=1)
    doc = measurement.prepare_doc()
    assert not doc.get("temperature")
    assert not doc.get("humidity")

    
def test_measurment_time(measurement):
    testtime = 1.0
    with patch("housemonitor.measurement.Measurement.get_current_timestamp") as t_method:
        t_method.return_value = testtime
        doc = measurement.prepare_doc()
        assert abs(doc["time"] - testtime) < small_diff

