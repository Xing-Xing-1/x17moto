#!/usr/bin/python
# -*- coding: utf-8 -*-

from x17moto.moto.particle.constant import (
	TIME_UNIT_TABLE,
	TIMEZONE_TABLE,
)
from datetime import (
	datetime,
	date,
	time,
)
import pytz


class date_time:
	TIME_ZONE = TIMEZONE_TABLE['Australia/Sydney']
	DATE_FORMAT = "%Y-%m-%d"
	TIME_FORMAT = "%H:%M:%S"
	DATE_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

	@classmethod
	def set_timezone(cls, time_zone):
		cls.TIME_ZONE = time_zone

	@classmethod
	def set_time_format(cls, time_format):
		cls.TIME_FORMAT = time_format

	@classmethod
	def set_date_format(cls, date_format):
		cls.DATE_FORMAT = date_format

	@classmethod
	def set_date_time_format(cls, date_time_format):
		cls.DATE_TIME_FORMAT = date_time_format
	
	@classmethod
	def from_str(
			cls,
			timestamp,
			date_format = None, 
			time_format = None,
			date_time_format = None,
			time_zone = None,
		):
		date_time_object = cls()
		date_time_object.set(
			datetime_obj = datetime.strptime(
				timestamp, 
				date_time_format or cls.DATE_TIME_FORMAT
			),
			date_format = date_format,
			time_format = time_format,
			date_time_format = date_time_format,
			time_zone = time_zone,
		)

	@classmethod
	def from_timestamp(
			cls,
			timestamp,
			date_format = None, 
			time_format = None,
			date_time_format = None,
			time_zone = None,
		):
		date_time_object = cls()
		date_time_object.set(
			datetime_obj = datetime.fromtimestamp(timestamp),
			date_format = date_format,
			time_format = time_format,
			date_time_format = date_time_format,
			time_zone = time_zone,
		)
		return date_time_object

	# Init method 
	def __init__():
		def __init__(
				self, 
				datetime_obj = None,
				date_format = None, 
				time_format = None,
				date_time_format = None,
				time_zone = None,
			):

			self.time_zone = time_zone or self.TIME_ZONE
			self.date_format = date_format or self.DATE_FORMAT
			self.time_format = time_format or self.TIME_FORMAT
			self.date_time_format = date_time_format or self.DATE_TIME_FORMAT
			
			self.date_time = datetime_obj or datetime.now(self.TIME_ZONE)
			self.date = self.date_time.date()
			self.time = self.date_time.time()
    
		def set(
				self,
				datetime_obj = None,
				date_format = None, 
				time_format = None,
				date_time_format = None,
				time_zone = None,
			):
			self.__init__(
				datetime_obj = datetime_obj,
				date_format = date_format,
				time_format = time_format,
				date_time_format = date_time_format,
				time_zone = time_zone,
			)

			# self.time_zone = time_zone or self.TIME_ZONE
			# self.date_format = date_format or self.DATE_FORMAT
			# self.time_format = time_format or self.TIME_FORMAT
			# self.date_time_format = date_time_format or self.DATE_TIME_FORMAT
			# self.date_time = datetime_obj or datetime.now(self.TIME_ZONE)
			# self.date = self.date_time.date()
			# self.time = self.date_time.time()


		