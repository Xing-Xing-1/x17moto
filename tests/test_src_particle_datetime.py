from x17moto.moto.particle.date_time import date_time
from datetime import datetime
import pytest

def test_class():
	assert date_time.TIME_ZONE == "Australia/Sydney"
	assert date_time.DATE_FORMAT == "%Y-%m-%d"
	assert date_time.TIME_FORMAT == "%H:%M:%S"
	assert date_time.DATE_TIME_FORMAT == "%Y-%m-%d %H:%M:%S"

def test_class_set_timezone():
	date_time.set_timezone("Australia/Melbourne")
	assert date_time.TIME_ZONE == "Australia/Melbourne"

def test_class_set_time_format():
	date_time.set_time_format("%H:%M")
	assert date_time.TIME_FORMAT == "%H:%M"

def test_class_set_date_format():
	date_time.set_date_format("%d-%m-%Y")
	assert date_time.DATE_FORMAT == "%d-%m-%Y"

def test_class_set_date_time_format():
	date_time.set_date_time_format("%d-%m-%Y %H:%M")
	assert date_time.DATE_TIME_FORMAT == "%d-%m-%Y %H:%M"

def test_class_from_str():
	date_time_str = "2021-01-01 00:00:00"
	date_time_obj = date_time.from_str(date_time_str)
	assert date_time_obj == datetime.strptime(date_time_str, date_time.DATE_TIME_FORMAT)

def test_class_from_timestamp():
	timestamp = 1609459200
	date_time_obj = date_time.from_timestamp(timestamp)
	assert date_time_obj == datetime.fromtimestamp(timestamp, date_time.TIME_ZONE)




