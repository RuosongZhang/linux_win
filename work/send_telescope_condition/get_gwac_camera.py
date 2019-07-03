#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import re
import time
import datetime
import paramiko
def get_ser_config(type):
    if type == 'ccd_3_21':
        ser_ip = '172.28.3.21'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_22':
        ser_ip = '172.28.3.22'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_23':
        ser_ip = '172.28.3.23'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_24':
        ser_ip = '172.28.3.24'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_25':
        ser_ip = '172.28.3.25'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_31':
        ser_ip = '172.28.3.31'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_32':
        ser_ip = '172.28.3.32'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_33':
        ser_ip = '172.28.3.33'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_34':
        ser_ip = '172.28.3.34'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_35':
        ser_ip = '172.28.3.35'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_41':
        ser_ip = '172.28.3.41'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_41':
        ser_ip = '172.28.3.41'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_42':
        ser_ip = '172.28.3.42'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_43':
        ser_ip = '172.28.3.43'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_44':
        ser_ip = '172.28.3.44'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'ccd_3_45':
        ser_ip = '172.28.3.45'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'tele_w60':
        ser_ip = '190.168.1.203'
        ser_un = 'w60ccd'
        ser_pw = 'x'
    if type == 'tele_e60':
        ser_ip = '190.168.1.201'
        ser_un = 'e60ccd'
        ser_pw = 'x'
    if type == 'tele_30':
        ser_ip = '190.168.1.207'
        ser_un = 'ccduser'
        ser_pw = 'x'
    ser_con_list = [ser_ip, ser_un, ser_pw]
    return ser_con_list


def con_ssh(ip, username, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(hostname=ip, port=22, username=username, password=passwd, timeout=30)
    except:
        print("\nWARNING: Connection of ssh is wrong!")
    else:
        stdin, stdout, stderr = ssh.exec_command(cmd)
        out = stdout.readlines()
        ssh.close()
        return out

def check_camagent(type):
    ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
    cmd = 'ps -ef | grep camagent | grep -v grep'
    res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
#    print(res)
    if res:
        return 1
    else:
        return 0

def check_gftservice(type):
    ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
    cmd = 'ps -ef | grep gftservice | grep -v grep'
    res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
#    print(res)
    if res:
        return 1
    else:
        return 0