# -*- coding: utf-8 -*-
"""
Created on June 05 10:46:24 2017

@author: han
"""
import sys, stat
import math
import subprocess as subp
## {{{ http://code.activestate.com/recipes/52224/ (r1)
from os.path import exists, join
import os.path
from os import pathsep
import string
import os
import time
from numpy import array
import numpy as np
import collections
from collections import defaultdict
# import matplotlib.pyplot as plt
from optparse import OptionParser
# from mpl_toolkits.basemap import Basemap
from angular_distance import angular_distance
from define_limit import define_limit
from GWAC_field_load import GWAC_field_load
from func_gwac_too_fieldmatch_file import func_gwac_too_fieldmatch_file


def Too_grid_select(ID_grid,trigger_ra_center,trigger_dec_center,trigger_localisation_error):

    grid_data_array = GWAC_field_load(ID_grid)
    file_grid_id_arr = []
    file_field_id_arr = []
    file_fov_sizex_arr = [] 
    file_fov_sizey_arr = []
    file_ra_center_arr = []
    file_dec_center_arr = []
    file_decdeg_h1_arr = []
    file_decdeg_l1_arr = []
    for n in range(len(grid_data_array[0])):
        file_grid_id_arr.append(grid_data_array[1][n])
        file_field_id_arr.append(grid_data_array[2][n])
        file_fov_sizex_arr.append(float(grid_data_array[3][n]))
        file_fov_sizey_arr.append(float(grid_data_array[4][n]))
        file_ra_center_arr.append(float(grid_data_array[5][n]))
        file_dec_center_arr.append(float(grid_data_array[6][n]))
        file_decdeg_h1_arr.append(float(grid_data_array[8][n]))
        file_decdeg_l1_arr.append(float(grid_data_array[12][n]))    

    grid_id_arr = []
    field_id_arr = []
    fov_sizex_arr = [] 
    fov_sizey_arr = []    
    ra_center_arr = []
    dec_center_arr = []
    for n in range(len(coor_data[0])):
        data = func_gwac_too_fieldmatch_file(trigger_ra_center,trigger_dec_center,trigger_localisation_error,file_grid_id_arr,file_field_id_arr,file_fov_sizex_arr,file_fov_sizey_arr,file_ra_center_arr,file_dec_center_arr,file_decdeg_h1_arr,file_decdeg_l1_arr)
        if len(data[0]) > 0:
            grid_id_arr.append(data[1][0])
            field_id_arr.append(data[2][0])
            fov_sizex_arr.append(data[3][0])
            fov_sizey_arr.append(data[4][0])
            ra_center_arr.append(data[5][0])
            dec_center_arr.append(data[6][0])

    # probability sum
    grid_id_nparr = np.array(grid_id_arr)
    field_id_nparr = np.array(field_id_arr)
    fov_sizex_nparr = np.array(fov_sizex_arr)
    fov_sizey_nparr = np.array(fov_sizey_arr)
    ra_center_nparr = np.array(ra_center_arr)
    dec_center_nparr = np.array(dec_center_arr)
    probability_nparr = np.array(probability_arr)


    match_region = []
    grid_id_arr = []
    field_id_arr = []
    fov_sizex_arr = [] 
    fov_sizey_arr = []
    ra_center_arr = []
    dec_center_arr = []
    # radeg_h1_arr = []
    decdeg_h1_arr = []
    # radeg_h2_arr = []
    # decdeg_h2_arr = []
    # radeg_l1_arr = []
    decdeg_l1_arr = []
    # radeg_l2_arr = []
    # decdeg_l2_arr = []
    for n in range(len(file_field_id_arr)):
        field_id=file_field_id_arr[n]
        fov_sizex=(file_fov_sizex_arr[n])
        fov_sizey=(file_fov_sizey_arr[n])
        ra_center=(file_ra_center_arr[n])
        dec_center=(file_dec_center_arr[n])
        decdeg_h1=(file_decdeg_h1_arr[n])
        decdeg_l1=(file_decdeg_l1_arr[n])

        # fov_sizey = decdeg_h1 - decdeg_l1
        # fov_sizex = angular_distance(radeg_l1,decdeg_l1,radeg_l2,decdeg_l1)
        ang_dis_obj_cen = angular_distance(ra_center,decdeg,radeg,decdeg)

        # field_boundary_arr = define_limit(ra_center,dec_center,fov_sizex,fov_sizey,2)
        # ang_dis_obj_boundary_arr = []
        # for field_boundary_n in range(len(field_boundary_arr[0])):
        #     ra_boundary = field_boundary_arr[0][field_boundary_n]
        #     dec_boundary = field_boundary_arr[1][field_boundary_n]
        #     ang_dis_obj_boundary_arr.append(angular_distance(radeg,decdeg,ra_boundary,dec_boundary))
        # ang_dis_obj_boundary_min = min(ang_dis_obj_boundary_arr)
        match_mark = 0
        if ang_dis_obj_cen < (fov_sizex/2.) and decdeg >= decdeg_l1 and decdeg <= decdeg_h1:
                match_region.append('center')
                grid_id_arr.append(grid_id)
                field_id_arr.append(field_id)
                fov_sizex_arr.append(fov_sizex)
                fov_sizey_arr.append(fov_sizey)
                ra_center_arr.append(ra_center)
                dec_center_arr.append(dec_center)
                match_mark = 1   
        # if ang_dis_obj_boundary_min < radius and match_mark == 0:
        #         match_region.append('circle')
        #         grid_id_arr.append(grid_id)
        #         field_id_arr.append(field_id)
        #         fov_sizex_arr.append(fov_sizex)
        #         fov_sizey_arr.append(fov_sizey)
        #         ra_center_arr.append(ra_center)
        #         dec_center_arr.append(dec_center)

    return [match_region,grid_id_arr,field_id_arr,fov_sizex_arr,fov_sizey_arr,\
    ra_center_arr,dec_center_arr]


# if __name__ == "__main__":
#     usage = "Example: python GWAC_ToO_fieldmatch_file.py 59.6420 -13.8590 0.4000 G0007 (G0007 for MiniGWAC, G0008 for GWAC)"  
# if not sys.argv[1:]:
#     # print usage
#     sys.argv += ["47.5", "24.26","5.1","G0013"]

# radeg = float(sys.argv[1])
# decdeg = float(sys.argv[2])
# radius = float(sys.argv[3])
# grid_id = sys.argv[4]

# match_plot = "./GWAC_ToO_match.png"

# data = func_gwac_too_fieldmatch_file(radeg,decdeg,radius,grid_id)
# print data
# # func_gwac_too_fieldmatch_plot(radeg,decdeg,radius,data,match_plot)

