import pytest
from Part_4.Section07_Project3.app_arnav.models.storage import Storage


@pytest.fixture()
def storage_values():
	return {
		'name': 'Thumbdrive',
		'manufacturer': 'Sandisk',
		'total': 10,
		'allocated': 3
	}


@pytest.mark.parametrize('capacity_gb', [64, 128, 256])
def test_valid_storage(storage_values, capacity_gb):
	assert Storage(**storage_values, capacity_GB=capacity_gb)


@pytest.mark.parametrize(
	'exception, capacity_gb', [(TypeError, '64'), (TypeError, 128.5), (TypeError, 256 + 3j),
	                           (ValueError, -64), (ValueError, 0)])
def test_invalid_storage(storage_values, exception, capacity_gb):
	with pytest.raises(exception):
		Storage(**storage_values, capacity_GB=capacity_gb)


@pytest.mark.parametrize(
	'exception, capacity_gb', [(AttributeError, 64), (AttributeError, 128), (AttributeError, 256)])
def test_readonly_capacity_GB(storage_values, exception, capacity_gb):
	s1 = Storage(**storage_values, capacity_GB=capacity_gb)
	with pytest.raises(exception):
		s1.capacity_GB = 100
