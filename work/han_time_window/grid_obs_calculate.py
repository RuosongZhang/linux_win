# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 10:46:24 2012

@author: han
"""
__author__='Xuhui Han'
__version__ ='$Revision: 1.1 $'
import sys, stat
import math
import subprocess as subp
## {{{ http://code.activestate.com/recipes/52224/ (r1)
from os.path import exists, join
import os.path
from os import pathsep
import string
import os
import datetime
from datetime import timedelta
import numpy as np
#import matplotlib.pyplot as plt
import time
import re
from jdcal import gcal2jd
from jdcal import jd2gcal
from jdcal import MJD_0
import shutil
import subprocess    
import glob
#from mpl_toolkits.basemap import Basemap
import numpy as np
#import matplotlib.pyplot as plt
import MySQLdb
import pandas as pd
from pandas import DataFrame, read_csv
from coords import gal2eq
from angular_distance import angular_distance
from optparse import OptionParser
#from GWAC_obs_calculate_plot import GWAC_obs_calculate_plot
import ephem
try:
  sys.path.append("./astronomical_cal_code/")
  import dt2jd
  import jd2dt
except:
  print "please install sidereal code "
  sys.exit()

t0 = datetime.datetime.now()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main(): 
	""" main method """
	usage = "Example: python grid_obs_calculate.py -g G0008 " 
	parser = OptionParser( usage,version = __version__ ) #"test")# __version__ )                                                                                                           
	parser.add_option( "-g", "--gridid", dest = "gridid" , type = "string", \
	                  help = "Grid ID,  default=G0001",default="G0001")
	opts, args = parser.parse_args()

	if len(sys.argv) == 1:
	    print "please use -h to see help"
	    print usage
	    sys.exit()

	GridID = opts.gridid

	homedir = os.getcwd()
	configuration_file = './configuration.dat'
	configuration_file_dev = open(configuration_file,'rU')

	lines1=configuration_file_dev.read().splitlines()
	configuration_file_dev.close()

	for line1 in lines1:
	    word=line1.split()
	    if word[0] == 'griduser':
	        griduser = word[2]
	    elif word[0] == 'gridip':
	        gridip = word[2]
	    elif word[0] == 'gridmypassword':
	        gridmypassword = word[2]
	    elif word[0] == 'gridmydb':
	        gridmydb = word[2]

	conf_obs_parameters_sys = './conf_obs_parameters_sys.dat'
	conf_obs_parameters_sys_dev = open(conf_obs_parameters_sys,'rU')

	lines2=conf_obs_parameters_sys_dev.read().splitlines()
	conf_obs_parameters_sys_dev.close()

	for line2 in lines2:
		word=line2.split()
		if word[0] == 'observatory_lat':
		    observatory_lat = word[2]
		elif word[0] == 'observatory_lon':
		    observatory_lon = word[2]
		elif word[0] == 'observatory_elevation':
		    observatory_elevation = float(word[2])
		elif word[0] == 'zenith_sun_min':
		    zenith_sun_min = float(word[2])	        
		elif word[0] == 'zenith_min':
		    zenith_min = float(word[2])
		elif word[0] == 'gal_min':
		    gal_min = float(word[2])
		elif word[0] == 'moon_dis_min_para':
			moon_dis_min_str = word[2]
			moon_dis_para_str = moon_dis_min_str.split('|')
			moon_dis_phase_data = [[]]
			for moon_dis_para in moon_dis_para_str:
				moon_dis_para_phase_min = float(moon_dis_para.split(':')[0].split('-')[0])
				moon_dis_para_phase_max = float(moon_dis_para.split(':')[0].split('-')[1])
				moon_dis_para_dis = float(moon_dis_para.split(':')[1])
				moon_dis_phase_data.append([moon_dis_para_phase_min,moon_dis_para_phase_max,moon_dis_para_dis])
			moon_dis_phase_data = filter(None,moon_dis_phase_data)

	conn_gwacoc_grid = MySQLdb.connect(host = gridip,
	                user = griduser,
	                passwd = gridmypassword,
	                db =  gridmydb) 
	cursor_gwacoc_grid = conn_gwacoc_grid.cursor ()  

	grid_cmd = "select * from Grid_table where GridID = '" + GridID + "'"
	#print grid_cmd
	cursor_gwacoc_grid.execute(grid_cmd)
	extract_grid_result = cursor_gwacoc_grid.fetchall()     
	print   extract_grid_result  
	cursor_gwacoc_grid.close()

	# define grid date frame ----------------------------------------
	gridframe = pd.DataFrame()
	if len(extract_grid_result) > 0:
		gridframe['obs_date'] = 0
		gridframe['Grid_ID'] = zip(*extract_grid_result)[1]
		gridframe['field_ID']  = zip(*extract_grid_result)[2]
		gridframe['ra_center'] = zip(*extract_grid_result)[3]
		gridframe['dec_center'] = zip(*extract_grid_result)[4]
		gridframe['radeg_h1'] = zip(*extract_grid_result)[5]
		gridframe['decdeg_h1'] = zip(*extract_grid_result)[6]
		gridframe['radeg_h2'] = zip(*extract_grid_result)[7]
		gridframe['decdeg_h2'] = zip(*extract_grid_result)[8]
		gridframe['radeg_l1'] = zip(*extract_grid_result)[9]
		gridframe['decdeg_l1'] = zip(*extract_grid_result)[10]
		gridframe['radeg_l2'] = zip(*extract_grid_result)[11]
		gridframe['decdeg_l2'] = zip(*extract_grid_result)[12]	
		gridframe['mjd_begin'] = 0
		gridframe['mjd_end'] = 0
		gridframe['local_time_begin'] = 0
		gridframe['local_time_end'] = 0
		gridframe['lst_begin'] = 0
		gridframe['lst_end'] = 0
		gridframe['solar_alt_begin'] = 0
		gridframe['solar_alt_end'] = 0
		gridframe['lunar_ra_begin'] = 0
		gridframe['lunar_dec_begin'] = 0
		gridframe['lunar_phase_begin'] = 0
		gridframe['lunar_ra_end'] = 0
		gridframe['lunar_dec_end'] = 0
		gridframe['lunar_phase_end'] = 0

	#path = '/Users/han/tmp_pool/gwac_dispatch/obs_skymap/'

	# set observation day ------------------------------------------------
	current_utc_datetime = datetime.datetime.utcnow()
	Op_time = current_utc_datetime.strftime( '%Y-%m-%d' )  
	Op_time = time.strptime( Op_time, "%Y-%m-%d") 
	gcal_y = Op_time.tm_year
	gcal_m = Op_time.tm_mon
	gcal_d = Op_time.tm_mday 
	MJD_newyear = gcal2jd(gcal_y,gcal_m,gcal_d)[1] 
	MJD_current = MJD_newyear
	date_current = jd2gcal(2400000.5, MJD_current)
	calendar_d_lable = "%d_%d_%d" % (date_current[0],date_current[1],date_current[2])
	calendar_d = "%d-%d-%d" % (date_current[0],date_current[1],date_current[2])

	# start calculate observation sequence
	# time_interval = 40.0 # 2 munitues
	# night_number = 36 # every 2 munitues, 720 in total.		
	time_interval = 5.0 # 2 munitues
	night_number = 288 # every 2 munitues, 720 in total.

	# set observatory parameters ----------------------------------------
	observatory = ephem.Observer()
	observatory.lat = observatory_lat
	observatory.lon = observatory_lon
	observatory.elevation = observatory_elevation
	lat_dd = float(str(observatory.lat).split(":")[0])+\
	float(str(observatory.lat).split(":")[1])/60.0+\
	float(str(observatory.lat).split(":")[2])/3600.0

	# define obs date frame ----------------------------------------
	obsframe = pd.DataFrame()

	for k in range(len(gridframe['Grid_ID'])):
		#print 'field coor: ',gridframe['ra_center'][k],gridframe['dec_center'][k]
		mjd = []
		local_time = []
		lst = []
		solar_alt = []
		lunar_ra = []
		lunar_dec = []
		lunar_phase = []	 
		gridframe.loc[k,'obs_date'] = calendar_d
		# calculate galactic coordinate of field center and all vertexes
		coor_equ_cen = ephem.Equatorial(gridframe['ra_center'][k],gridframe['dec_center'][k], epoch='2000')
		g_cen = ephem.Galactic(coor_equ_cen)
		g_cen_lat_dd = float(str(g_cen.lat).split(":")[0])+\
			float(str(g_cen.lat).split(":")[1])/60.0+\
			float(str(g_cen.lat).split(":")[2])/3600.0
		coor_equ_h1 = ephem.Equatorial(gridframe['radeg_h1'][k],gridframe['decdeg_h1'][k], epoch='2000')
		g_h1 = ephem.Galactic(coor_equ_h1)
		g_h1_lat_dd = float(str(g_h1.lat).split(":")[0])+\
			float(str(g_h1.lat).split(":")[1])/60.0+\
			float(str(g_h1.lat).split(":")[2])/3600.0
		coor_equ_h2 = ephem.Equatorial(gridframe['radeg_h2'][k],gridframe['decdeg_h2'][k], epoch='2000')
		g_h2 = ephem.Galactic(coor_equ_h2)
		g_h2_lat_dd = float(str(g_h2.lat).split(":")[0])+\
			float(str(g_h2.lat).split(":")[1])/60.0+\
			float(str(g_h2.lat).split(":")[2])/3600.0
		coor_equ_l1 = ephem.Equatorial(gridframe['radeg_l1'][k],gridframe['decdeg_l1'][k], epoch='2000')
		g_l1 = ephem.Galactic(coor_equ_l1)
		g_l1_lat_dd = float(str(g_l1.lat).split(":")[0])+\
			float(str(g_l1.lat).split(":")[1])/60.0+\
			float(str(g_l1.lat).split(":")[2])/3600.0
		coor_equ_l2 = ephem.Equatorial(gridframe['radeg_l2'][k],gridframe['decdeg_l2'][k], epoch='2000')
		g_l2 = ephem.Galactic(coor_equ_l2)
		g_l2_lat_dd = float(str(g_l2.lat).split(":")[0])+\
			float(str(g_l2.lat).split(":")[1])/60.0+\
			float(str(g_l2.lat).split(":")[2])/3600.0

		galactic_lat_min = min([abs(g_cen_lat_dd),abs(g_h1_lat_dd),abs(g_h2_lat_dd),abs(g_l1_lat_dd),abs(g_l2_lat_dd)])

		for n in range(night_number):	
			# set mjd time ----------------------------------------
			MJD_time = MJD_current + (n*time_interval/60.0/24.0)
			nighttime_current = jd2gcal(2400000.5, MJD_time)
			hh = int(nighttime_current[3] * 24.0 )
			mm = int((nighttime_current[3] * 24.0 - hh)*60.0)
			ss = (((nighttime_current[3] * 24.0 - hh)*60.0) - mm)*60.0
			hms = "%02d:%02d:%02d" % (hh,mm,ss)
			nighttime_current_cal = ('%s/%s/%s %s' % (nighttime_current[0],nighttime_current[1],nighttime_current[2],hms))
			nighttime_current_str = ('%s/%s/%sT%s' % (nighttime_current[0],nighttime_current[1],nighttime_current[2],hms))
			observatory.date = nighttime_current_cal

			# set local time ----------------------------------------
			local_nighttime_current = ephem.localtime(observatory.date)
			local_nighttime_current_str = str(local_nighttime_current).replace(' ','T')[0:22]
			

			# calculate local sidereal time  ----------------------------------------
			lst_dd = float(str(observatory.sidereal_time()).split(":")[0])* 15.0+\
			float(str(observatory.sidereal_time()).split(":")[1])/60.0* 15.0+\
			float(str(observatory.sidereal_time()).split(":")[2])/3600.0* 15.0
			

			# calculate altitude angle or zenith angular distance of the sun   ---------------------------------
			solar = ephem.Sun(observatory)
			solar_alt_dd = 90 - float(str(solar.alt).split(":")[0])+float(str(solar.alt).split(":")[1])/60.0+float(str(solar.alt).split(":")[2])/3600.0
			#print('solar  %s' % (solar_alt_dd))
			

			lunar = ephem.Moon(observatory)
			lunar_ra_dd = float(str(lunar.ra).split(":")[0])* 15.0+float(str(lunar.ra).split(":")[1])/60.0* 15.0+float(str(lunar.ra).split(":")[2])/3600.0* 15.0
			lunar_dec_dd = float(str(lunar.dec).split(":")[0])+float(str(lunar.dec).split(":")[1])/60.0+float(str(lunar.dec).split(":")[2])/3600.0
			#print('lunar %s %s %s' % (lunar_ra_dd, lunar_dec_dd, lunar.moon_phase))

			# calculate zenith angular distance of field center and all vertexes
			zenith_ang_dis_cen_dd = angular_distance(gridframe['ra_center'][k], gridframe['dec_center'][k],lst_dd,lat_dd)
			


			# calculate angular distance between field center and all vertexes and moon
			moon_ang_dis_cen_dd = angular_distance(gridframe['ra_center'][k], gridframe['dec_center'][k],lunar_ra_dd,lunar_dec_dd)
			moon_ang_dis_h1_dd = angular_distance(gridframe['radeg_h1'][k], gridframe['decdeg_h1'][k],lunar_ra_dd,lunar_dec_dd)
			moon_ang_dis_h2_dd = angular_distance(gridframe['radeg_h2'][k], gridframe['decdeg_h2'][k],lunar_ra_dd,lunar_dec_dd)
			moon_ang_dis_l1_dd = angular_distance(gridframe['radeg_l1'][k], gridframe['decdeg_l1'][k],lunar_ra_dd,lunar_dec_dd)
			moon_ang_dis_l2_dd = angular_distance(gridframe['radeg_l2'][k], gridframe['decdeg_l2'][k],lunar_ra_dd,lunar_dec_dd)
			moon_ang_dis_min = min([moon_ang_dis_cen_dd,moon_ang_dis_h1_dd,moon_ang_dis_h2_dd,moon_ang_dis_l1_dd,moon_ang_dis_l2_dd])

			# set mini distance from the moon
			for mm in range(len(moon_dis_phase_data)):
				if (lunar.moon_phase >= moon_dis_phase_data[mm][0] and lunar.moon_phase < moon_dis_phase_data[mm][1]):
					moon_dis_min = moon_dis_phase_data[mm][2]
					break
			#print lunar.moon_phase,moon_dis_min

			#print k,gridframe.loc[k,'field_ID'],zenith_ang_dis_cen_dd , zenith_min , galactic_lat_min , gal_min , moon_ang_dis_min , moon_dis_min
			if ( solar_alt_dd > zenith_sun_min ) and ( zenith_ang_dis_cen_dd < zenith_min ): # and galactic_lat_min > gal_min and moon_ang_dis_min > moon_dis_min ):
				# print 'mjd: ',MJD_current,MJD_time,nighttime_current
				# print 'zenith: ',gridframe['ra_center'][k], gridframe['dec_center'][k],lst_dd,lat_dd,solar_alt_dd,zenith_ang_dis_cen_dd,zenith_min
				mjd.append(MJD_time)
				local_time.append(local_nighttime_current_str)
				lst.append(lst_dd)
				solar_alt.append(solar_alt_dd)
				lunar_ra.append(lunar_ra_dd)
				lunar_dec.append(lunar_dec_dd)
				lunar_phase.append(lunar.moon_phase)
				#print gridframe['field_ID'],MJD_time
		# del mjd[0]
		# del local_time[0]
		# del lst[0]
		# del solar_alt[0]
		# del lunar_ra[0]
		# del lunar_dec[0]
		# del lunar_phase[0]

		# mjd = filter(None,mjd)
		# local_time = filter(None,local_time)
		# lst = filter(None,lst)	
		# solar_alt = filter(None,solar_alt)
		# lunar_ra = filter(None,lunar_ra)
		# lunar_dec = filter(None,lunar_dec)
		# lunar_phase = filter(None,lunar_phase)


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

			gridframe.loc[k,'mjd_begin'] = mjd[obs_mjd_begin_index]
			gridframe.loc[k,'mjd_end'] = mjd[obs_mjd_end_index]
			gridframe.loc[k,'local_time_begin'] = local_time[obs_mjd_begin_index]
			gridframe.loc[k,'local_time_end'] = local_time[obs_mjd_end_index]
			gridframe.loc[k,'lst_begin'] = lst[obs_mjd_begin_index]
			gridframe.loc[k,'lst_end'] = lst[obs_mjd_end_index]
			gridframe.loc[k,'solar_alt_begin'] = solar_alt[obs_mjd_begin_index]
			gridframe.loc[k,'solar_alt_end'] = solar_alt[obs_mjd_end_index]
			gridframe.loc[k,'lunar_ra_begin'] = lunar_ra[obs_mjd_begin_index]
			gridframe.loc[k,'lunar_dec_begin'] = lunar_dec[obs_mjd_end_index]
			gridframe.loc[k,'lunar_phase_begin'] = lunar_phase[obs_mjd_begin_index]
			gridframe.loc[k,'lunar_ra_end'] = lunar_ra[obs_mjd_end_index]
			gridframe.loc[k,'lunar_dec_end'] = lunar_dec[obs_mjd_begin_index]
			gridframe.loc[k,'lunar_phase_end'] = lunar_phase[obs_mjd_end_index]

	for k in range(len(gridframe['obs_date'])):   
		CurrentTable = "grid_observable_timetable" 
		if gridframe.loc[k,'mjd_begin'] > 0:  
			insert_cmd = "insert into " + CurrentTable + " values ( DEFAULT , " + \
			"'" + gridframe.loc[k,'obs_date']  + "' , " + \
			"'" + gridframe.loc[k,'Grid_ID'] + "' , " + \
			"'" + gridframe.loc[k,'field_ID'] + "' , " + \
			" " + str(gridframe.loc[k,'ra_center']) + " , " + \
			" " + str(gridframe.loc[k,'dec_center']) + " , " + \
			" " + str(gridframe.loc[k,'radeg_h1']) + " , " + \
			" " + str(gridframe.loc[k,'decdeg_h1']) + " , " + \
			" " + str(gridframe.loc[k,'radeg_h2']) + " , " + \
			" " + str(gridframe.loc[k,'decdeg_h2']) + " , " + \
			" " + str(gridframe.loc[k,'radeg_l1']) + " , " + \
			" " + str(gridframe.loc[k,'decdeg_l1']) + " , " + \
			" " + str(gridframe.loc[k,'radeg_l2']) + " , " + \
			" " + str(gridframe.loc[k,'decdeg_l2']) + " , " + \
			" " + str(gridframe.loc[k,'mjd_begin']) + " , " + \
			" " + str(gridframe.loc[k,'mjd_end']) + " , " + \
			"'" + str(gridframe.loc[k,'local_time_begin']) + "' , " + \
			"'" + str(gridframe.loc[k,'local_time_end']) + "' , " + \
			" " + str(gridframe.loc[k,'lst_begin']) + " , " + \
			" " + str(gridframe.loc[k,'lst_end']) + " , " + \
			" " + str(gridframe.loc[k,'solar_alt_begin']) + " , " + \
			" " + str(gridframe.loc[k,'solar_alt_end']) + " , " + \
			" " + str(gridframe.loc[k,'lunar_ra_begin']) + " , " + \
			" " + str(gridframe.loc[k,'lunar_dec_begin']) + " , " + \
			" " + str(gridframe.loc[k,'lunar_phase_begin']) + " , " + \
			" " + str(gridframe.loc[k,'lunar_ra_end']) + " , " + \
			" " + str(gridframe.loc[k,'lunar_dec_end']) + " , " + \
			" " + str(gridframe.loc[k,'lunar_phase_end']) + " " + \
			" " + ")"			
			print insert_cmd
			cursor = conn_gwacoc_grid.cursor()
			cursor.execute(insert_cmd)
			conn_gwacoc_grid.commit() 
			cursor.close ()                                                                                                                         

	
	conn_gwacoc_grid.close()

if __name__ == "__main__":

	main()

	# set observation day ------------------------------------------------
	current_utc_datetime = datetime.datetime.utcnow()
	Op_time = current_utc_datetime.strftime( '%Y-%m-%d' )  
	Op_time = time.strptime( Op_time, "%Y-%m-%d") 
	gcal_y = Op_time.tm_year
	gcal_m = Op_time.tm_mon
	gcal_d = Op_time.tm_mday 
	MJD_newyear = gcal2jd(gcal_y,gcal_m,gcal_d)[1] 
	MJD_current = MJD_newyear
	date_current = jd2gcal(2400000.5, MJD_current)
	calendar_d_lable = "%d_%d_%d" % (date_current[0],date_current[1],date_current[2])
	calendar_d = "%d-%d-%d" % (date_current[0],date_current[1],date_current[2])
	Op_type = 'test'
	GridID = 'G0008'
	Group_ID = 'GWAC_XL1'
	# start calculate observation sequence
	time_interval = 5.0 # 2 munitues
	night_number = 288 # every 2 munitues, 720 in total.

	for n in range(night_number):	
		# set utc time ----------------------------------------
		MJD_time = MJD_current + (n*time_interval/60.0/24.0)
		# GWAC_obs_calculate_plot(Op_type,GridID,Group_ID,calendar_d,MJD_time)

