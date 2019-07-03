"""

   Pubsub envelope subscriber   
 
   Author: Xuhui Han
  
"""
# from version import version
# import zmq
# import sys
# from jdcal import gcal2jd
# import os
# import datetime
# import time
# import MySQLdb
# import socket
# from search_box import search_box
# from optparse import OptionParser
# from GWAC_neutrino_followup import GWAC_neutrino_followup
# from GWAC_GW_followup import GWAC_GW_followup
# from GWAC_GBM_gwacfollowup import GWAC_GBM_gwacfollowup
# from func_GRBalerts_slack import func_GRBalerts_slack
# from func_slack_message import func_slack_message
# from func_GBM_111_observable_check import func_GBM_111_observable_check

# # from func_slack_test import func_GRBalerts_slack

# tele60_followup_codepath = os.getcwd() + '/tele60_followup/'
# sys.path.insert(0, tele60_followup_codepath)
# from tele60_GRB_followup import tele60_GRB_followup
# from tele60_GBM_followup import tele60_GBM_followup

# import threading

import sys
import time
import datetime
import json
from obsplan_to_DB_v2 import Retrieve_last_trigger_params
from obsplan_to_DB_v2 import Retrieve_newer_trigger_params
from obsplan_to_DB_v2 import Retrieve_pointing_list_lal
from obsplan_to_DB_v2 import CMM_DBConnect
from obsplan_to_DB_v2 import CMM_DBClose
from obsplan_to_DB_v2 import Telescope_Obs_strategy_match
from obsplan_to_DB_v2 import Set_reception_status_pointing_list
from obsplan_to_DB_v2 import trigger_type_classification
from func_GW_obs_insert_gwac import func_GW_obs_insert_gwac


# from ToP_GW_followup_GWAC_tile_assign import ToP_GW_followup_GWAC_tile_assign
# from ToP_GW_followup_F60_F30_galaxy_assign import ToP_GW_followup_F60_F30_galaxy_assign

# # set mode before impliment
# # mode = 'observation'
# mode = 'test'
# # set location
# location = 'beijing'
# # location = 'xinglong'

if __name__ == '__main__':
#    print sys.argv  
    z=0
if not sys.argv[1:]:
    sys.argv += ["observation", "beijing", "./log/"]

mode = sys.argv[1]
location = sys.argv[2]
homedir = sys.argv[3]


# if mode == 'test':

#     currenttime_time = time.strptime('2018-03-12 19:14:57',"%Y-%m-%d %H:%M:%S")
#     channel_name = "#grbalerttest"
#     channel_name_private = "#grbalerttest"

# elif mode == 'observation':
#     currenttime_time  = time.gmtime()
#     channel_name = "#grbalerts"  
#     channel_name_private = "#grbalerttest" 

# if location == 'beijing':
#     configuration_file = homedir+'/configuration_bj.dat'
# elif location == 'xinglong':
#     configuration_file = homedir+'/configuration_xl.dat'    


# mode_para = [mode,configuration_file,channel_name,currenttime_time,channel_name_private]
# # print mode_para

""" main method """
usage = "Example: python ToO_O3_followup.py" 


while True:
    # ask the DB to find the last alert
    old_trigger_params = json.loads(Retrieve_last_trigger_params(location))

    if old_trigger_params['ID_external_trigger'] != 0: 
        old_trigger_ID = old_trigger_params['ID_external_trigger']   
        # old_trigger_ID = 1300
        # print('old_trigger_ID',old_trigger_ID)

        while True: 
        #     if mode == 'observation':
        #         currenttime_time  = time.gmtime()
        #         # currenttime_time = time.strptime('2018-06-01 19:14:57',"%Y-%m-%d %H:%M:%S")
        #         # mode_para = [mode,configuration_file,channel_name,currenttime_time,channel_name_private]

            currenttime_time  = time.gmtime()
        #     # mode_para = [mode,configuration_file,channel_name,currenttime_time,channel_name_private]
            time_mark = time.strftime("%Y-%m-%d %H:%M:%S", currenttime_time)

            new_trigger_params = json.loads(Retrieve_newer_trigger_params(location,old_trigger_ID))
            
            if 0 in new_trigger_params['ID_external_trigger']:
                print(time_mark,'can not connect to the CMM DB, retry in 10 seconds')
                time.sleep(10)
            else: 
                print(time_mark,'connection is good. the old trigger id',old_trigger_ID)
                # print('new_trigger_params',Retrieve_newer_trigger_params(location,old_trigger_ID))
                trigger_ID = new_trigger_params['ID_external_trigger']
                trigger_name = new_trigger_params['external_trigger_name']
                trigger_time = new_trigger_params['external_trigger_time']  
                trigger_ra_center = new_trigger_params['external_trigger_RA_center'] 
                trigger_dec_center = new_trigger_params['external_trigger_dec_center'] 
                trigger_localisation_error = new_trigger_params['external_trigger_localisation_error'] 
                trigger_type = new_trigger_params['ID_external_trigger_type'] 
                trigger_type_name = new_trigger_params['ID_external_trigger_type']
                ID_external_trigger_telescope = new_trigger_params['ID_external_trigger_telescope']
                alert_message_revision = new_trigger_params['alert_message_revision']        
                alert_message_type = new_trigger_params['alert_message_type']

                if len(trigger_ID) >= 1:
                    for n in range(len(trigger_ID)):
                        #----- Retrieve the pointing list sent from LAL
                        name_telescope = []
                        ID_grid = []
                        ID_field = []
                        RA_pointing = []
                        dec_pointing = []
                        grade_pointing = []

                        mark1,mark2,mark5 = trigger_type_classification(trigger_type[n],ID_external_trigger_telescope[n],alert_message_type[n])
                        mark_trigger_type = mark1+mark2
                        if mark_trigger_type < 20000:
                            markobs = 'obs'
                            pointing_list_params = json.loads(Retrieve_pointing_list_lal(location,trigger_ID[n]))
                            while pointing_list_params == {}:
                                print(time_mark,'can not connect to the CMM DB, retry in 10 seconds')
                                time.sleep(10)
                                pointing_list_params = json.loads(Retrieve_pointing_list_lal(location,trigger_ID[n]))
                            else:
                                Set_reception_status_pointing_list(location,trigger_ID[n])
                                name_telescope = pointing_list_params['name_telescope']
                                ID_grid = pointing_list_params['ID_grid']
                                ID_field = pointing_list_params['ID_field']
                                RA_pointing = pointing_list_params['RA_pointing']
                                dec_pointing = pointing_list_params['dec_pointing']
                                grade_pointing = pointing_list_params['grade_pointing']
                                # print('name_telescope',name_telescope)
                                if 'GWAC' in name_telescope:
                                    # print('tiles')
                                    mark3 = 100
                                elif 'F60' in name_telescope:
                                    # print('galaxies')
                                    mark3 = 200
                                else:
                                    # print('name_telescope',name_telescope)
                                    mark3 = 0

                        elif mark_trigger_type > 20000 and mark_trigger_type < 30000:
                            markobs = obs_filterB()
                            if markobs == 'obs':

                                # create tile list for F30
                                name_telescope = 'F30'
                                ID_grid = 'G0015'
 
                                 
                                ID_field_arr,RA_pointing_arr,dec_pointing_arr,grade_pointing_arr = func_too_fieldmatch_file(ID_grid,trigger_ra_center,trigger_dec_center,trigger_localisation_error)
                                pointing_status = 'received @ GWAC'
                                upload_pointing_list_gwac(name_telescope,ID_grid,ID_field_arr,RA_pointing_arr,dec_pointing_arr,grade_pointing_arr,pointing_status)
                                mark3 = 100

                                # create galaxy list for F60
                                name_telescope = 'F60'
                                pointing_status = 'received @ GWAC'
                                ID_field_arr,RA_pointing_arr,dec_pointing_arr,grade_pointing_arr = func_too_galaxymatch_file(name_telescope,trigger_ra_center,trigger_dec_center,trigger_localisation_error，num_galaxy)
                                upload_pointing_list_gwac(name_telescope,ID_grid,ID_field_arr,RA_pointing_arr,dec_pointing_arr,grade_pointing_arr,pointing_status)
                                mark3 = 200


                        elif mark_trigger_type > 30000 and mark_trigger_type < 40000:
                            markobs = obs_filterC()
                            if markobs == 'obs':
                                
                                # create tile list for F30
                                name_telescope = 'F60'
                                pointing_status = 'received @ GWAC'
                                upload_pointing_list_gwac(name_telescope,'','',trigger_ra_center,trigger_dec_center,'',pointing_status)
                                mark3 = 300

                        elif mark_trigger_type > 40000 and mark_trigger_type < 50000:
                            markobs = obs_filterC()
                            if markobs == 'obs':
                                
                                # create tile list for F30
                                name_telescope = 'F30'
                                pointing_status = 'received @ GWAC'
                                upload_pointing_list_gwac(name_telescope,'','',trigger_ra_center,trigger_dec_center,'',pointing_status)
                                mark3 = 300


                            utc_time  = time.gmtime()
                            utc_time_str = time.strftime('%Y/%m/%d %H:%M:%S', utc_time)
                            utc_datetime = datetime.datetime.strptime(utc_time_str, '%Y/%m/%d %H:%M:%S')
                            datet_datetime = datetime.datetime.strptime(trigger_time[n], '%Y-%m-%d %H:%M:%S')
                            timedelta = utc_datetime - datet_datetime
                            timedelta_seconds = timedelta.total_seconds()
                            timedelay_check = timedelta_seconds / 60.0

                            if timedelay_check > 3 and timedelay_check <= 30:
                                mark4 = 10
                            elif timedelay_check > 30:
                                mark4 = 20
                            elif timedelay_check <= 3:
                                mark4 = 30
                            else:
                                # print('time delay check failed')
                                mark4 = 0

                            mark = mark1 + mark2 + mark3 + mark4 + mark5
                            if mark == 11111:
                                print('it is a GW trigger: initial, tiles, early, real')
                                obs_priority_plus = 2
                            elif mark == 11121:
                                print('it is a GW trigger: initial, tiles, late, real')
                                obs_priority_plus = 0
                            elif mark == 12111:
                                print('it is a GW trigger: Update, tiles, early, real')
                                obs_priority_plus = 3
                            elif mark == 12121:
                                print('it is a GW trigger: Update, tiles, late, real')
                                obs_priority_plus = 1

                            elif mark == 11112:
                                print('it is a GW trigger: initial, tiles, early, test')
                                obs_priority_plus = 2
                            elif mark == 11122:
                                print('it is a GW trigger: initial, tiles, late, test')
                                obs_priority_plus = 0
                            elif mark == 12112:
                                print('it is a GW trigger: Update, tiles, early, test')
                                obs_priority_plus = 3
                            elif mark == 12122:
                                print('it is a GW trigger: Update, tiles, late, test')
                                obs_priority_plus = 1

                            elif mark == 11211:
                                print('it is a GW trigger: initial, galaxies, early, real')
                                obs_priority_plus = 2
                            elif mark == 11221:
                                print('it is a GW trigger: initial, galaxies, late, real')
                                obs_priority_plus = 0
                            elif mark == 12211:
                                print('it is a GW trigger: Update, galaxies, early, real')
                                obs_priority_plus = 3
                            elif mark == 12221:
                                print('it is a GW trigger: Update, galaxies, late, real')
                                obs_priority_plus = 1

                            elif mark == 11212:
                                print('it is a GW trigger: initial, galaxies, early, test')
                                obs_priority_plus = 2
                            elif mark == 11222:
                                print('it is a GW trigger: initial, galaxies, late, test')
                                obs_priority_plus = 0
                            elif mark == 12212:
                                print('it is a GW trigger: Update, galaxies, early, test')
                                obs_priority_plus = 3
                            elif mark == 12222:
                                print('it is a GW trigger: Update, galaxies, late, test')
                                obs_priority_plus = 1

                            elif mark == 11212:
                                print('it is a GW trigger: initial, galaxies, early, test')
                                obs_priority_plus = 2
                            elif mark == 11222:
                                print('it is a GW trigger: initial, galaxies, late, test')
                                obs_priority_plus = 0
                            elif mark == 12212:
                                print('it is a GW trigger: Update, galaxies, early, test')
                                obs_priority_plus = 3
                            elif mark == 12222:
                                print('it is a GW trigger: Update, galaxies, late, test')
                                obs_priority_plus = 1

                                

                            obs_type_list = json.loads(Telescope_Obs_strategy_match(mark,location))
                            task_for = 0
                            if 12 in obs_type_list['obs_type_id']:
                                task_for = task_for + 1
                            elif 13 in obs_type_list['obs_type_id']:
                                task_for = task_for + 2
                            elif 14 in obs_type_list['obs_type_id']:   
                                task_for = task_for + 5
                            else:
                                task_for = 0

                            if task_for == 1:
                                print('it is a gwac task')  
                                priority = int(obs_type_list['priority'][0][0:2]) + obs_priority_plus
                                # print(priority,obs_type_list['group_ids'],obs_type_list['unit_ids'])
                                # print(RA_pointing,dec_pointing,grade_pointing)
                                packet_type = 'GW'
                                if mark5 == 1:
                                    rolet = 'observation'
                                else:
                                    rolet = 'test'
                                print('trigger ID',trigger_ID[n],trigger_name[n],trigger_time[n],trigger_type[n],obs_type_list['group_ids'][0],obs_type_list['unit_ids'][0],alert_message_type[n],packet_type,rolet)
                                func_GW_obs_insert_gwac(trigger_name[n],obs_type_list['group_ids'][0],obs_type_list['unit_ids'][0],packet_type,alert_message_type[n],priority,rolet,ID_grid,ID_field,RA_pointing,dec_pointing,grade_pointing)           
                            elif task_for == 2:
                                print('it is a F60 task')
                                print(trigger_ID[n],trigger_name[n],trigger_time[n],trigger_type[n],trigger_type_name[n],alert_message_revision[n],alert_message_type[n])

                            #     print(obs_type_list['obs_type_id'],obs_type_list['priority'],obs_type_list['group_ids'],obs_type_list['unit_ids'])
                            #     ToP_GW_followup_F60_F30_galaxy_assign(utc_datetime,obs_type_list['group_ids'],obs_type_list['unit_ids'],\
                            #         pointing_list_params['ID_grid'],pointing_list_params['ID_field'],pointing_list_params['RA_pointing'],pointing_list_params['dec_pointing'],pointing_list_params['grade_pointing'])             
                            elif task_for == 5:
                                print('it is a F30 task')
                                print(trigger_ID[n],trigger_name[n],trigger_time[n],trigger_type[n],trigger_type_name[n],alert_message_revision[n],alert_message_type[n])

                            #     print(obs_type_list['obs_type_id'],obs_type_list['priority'],obs_type_list['group_ids'],obs_type_list['unit_ids'])
                            #     ToP_GW_followup_F60_F30_galaxy_assign(utc_datetime,obs_type_list['group_ids'],obs_type_list['unit_ids'],\
                            #         pointing_list_params['ID_grid'],pointing_list_params['ID_field'],pointing_list_params['RA_pointing'],pointing_list_params['dec_pointing'],pointing_list_params['grade_pointing'])             
                            elif task_for == 7:
                                print('it is a F60 and F30 task') 
                                print(trigger_ID[n],trigger_name[n],trigger_time[n],trigger_type[n],trigger_type_name[n],alert_message_revision[n],alert_message_type[n])

                            #     print(obs_type_list['obs_type_id'],obs_type_list['priority'],obs_type_list['group_ids'],obs_type_list['unit_ids'])
                            #     ToP_GW_followup_F60_F30_galaxy_assign(utc_datetime,obs_type_list['group_ids'],obs_type_list['unit_ids'],\
                            #         pointing_list_params['ID_grid'],pointing_list_params['ID_field'],pointing_list_params['RA_pointing'],pointing_list_params['dec_pointing'],pointing_list_params['grade_pointing'])             
                            else:
                                print('it is no designated task') 
                                print(trigger_ID[n],trigger_name[n],trigger_time[n],trigger_type[n],trigger_type_name[n],alert_message_revision[n],alert_message_type[n])


                    old_trigger_ID = trigger_ID[-1]
                time.sleep(3)
    else:
        # old_trigger_params = json.loads(Retrieve_last_trigger_params(location))
        # while old_trigger_params['ID_external_trigger'] == 0:
        currenttime_time  = time.gmtime()
        time_mark = time.strftime("%Y-%m-%d %H:%M:%S", currenttime_time)
        # old_trigger_params = json.loads(Retrieve_last_trigger_params(location))
        print(time_mark, 'can not get the old ID_external_trigger, retry in 10 seconds')
        time.sleep(10)
        # if old_trigger_params['ID_external_trigger'] != 0:
        #     old_trigger_ID = old_trigger_params['ID_external_trigger']

