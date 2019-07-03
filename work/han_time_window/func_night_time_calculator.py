import os
import sys, stat
import math
import time
from time import gmtime, strftime,localtime
from coords import gal2eq
from coords import eq2gal
from astro_parameter_calculate import astro_parameter_calculate
import ephem
# try:
#   sys.path.append("./astronomical_cal_code/")
#   import dt2jd
#   import jd2dt
# except:
#   print("please install sidereal code ")
#   sys.exit()

try:
  sys.path.append("./jdcal/")
  from jdcal import gcal2jd
  from jdcal import jd2gcal
except:
  print("please install jdcal code ")
  sys.exit()

def func_night_time_calculator(current_date_str):

	# set observation day ------------------------------------------------
	# current_utc_datetime = time.gmtime()
	# Op_time = current_utc_datetime.strftime( '%Y-%m-%d %H:%M:%S' ) 
	# current_utc_datetime = "2017-05-23 21:29:38"
	Op_time = time.strptime(current_date_str, "%Y-%m-%d") 
	gcal_y = Op_time.tm_year
	gcal_m = Op_time.tm_mon
	gcal_d = Op_time.tm_mday 
	gcal_h = Op_time.tm_hour
	gcal_min = Op_time.tm_min
	gcal_sec = Op_time.tm_sec
	MJD_newyear = gcal2jd(gcal_y,gcal_m,gcal_d)[1] 
	MJD_current = MJD_newyear
	print(MJD_current)

	# start calculate observation sequence
	time_interval = 5.0 # 2 munitues
	night_number = 288 # every 2 munitues, 720 in total.

	mjd = []
	ut_time = []
	local_time = []
	solar_alt = []
	for n in range(night_number):	
		# set mjd time ----------------------------------------
		MJD_time = MJD_current + (n*time_interval/60.0/24.0)
		nighttime_current = jd2gcal(2400000.5, MJD_time)
		# print('night time', nighttime_current)
		hh = int(nighttime_current[3] * 24.0 )
		mm = int((nighttime_current[3] * 24.0 - hh)*60.0)
		ss = (((nighttime_current[3] * 24.0 - hh)*60.0) - mm)*60.0
		hms = "%02d:%02d:%02d" % (hh,mm,ss)
		nighttime_current_cal = ('%s/%s/%s %s' % (nighttime_current[0],nighttime_current[1],nighttime_current[2],hms))
		nighttime_current_str = ('%s/%02d/%02dT%s' % (nighttime_current[0],nighttime_current[1],nighttime_current[2],hms))

		nighttime_current_cal_datetime = time.strptime(nighttime_current_cal, '%Y/%m/%d %H:%M:%S')
		astro_parameter_night = astro_parameter_calculate(nighttime_current_cal_datetime)

		local_time_str = astro_parameter_night[1]
		solar_alt_dd = astro_parameter_night[3]
		zenith_sun_min =  astro_parameter_night[9]

		if ( solar_alt_dd > zenith_sun_min ):
			mjd.append(MJD_time)
			local_time.append(local_time_str)
			solar_alt.append(solar_alt_dd)

	if (len(mjd) > 0 ):
		obs_mjd_begin_index = 0
		for mmm in range(len(mjd)-1):
			m_gap = mjd[mmm+1] - mjd[mmm] 
			m_int = (2.0/24.0)
			if m_gap > m_int:
				obs_mjd_begin_index = mjd.index(mjd[mmm+1])
		if obs_mjd_begin_index == 0:
			obs_mjd_begin_index = mjd.index(min(mjd))
		obs_mjd_end_index = mjd.index(max(mjd))

	mjd_begin = mjd[obs_mjd_begin_index]
	mjd_end = mjd[obs_mjd_end_index]
	local_time_begin = local_time[obs_mjd_begin_index]
	local_time_end = local_time[obs_mjd_end_index]
	solar_alt_begin = solar_alt[obs_mjd_begin_index]
	solar_alt_end = solar_alt[obs_mjd_end_index]
	night_lenth = (mjd_end - mjd_begin) * 24.0

	return [str(local_time_begin),str(local_time_end),str(night_lenth),\
	str(solar_alt_begin),str(solar_alt_end)]

current_date_str = '2019-06-06'
data = func_night_time_calculator(current_date_str)
print(data)

