import re
import time
import datetime
import paramiko
def get_ser_config(type):
    if type == 'ccd_3_21':
        ser_ip = '172.28.3.21'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'

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
    print(res)
    if res:
        return 1
    else:
        return 0
print(check_camagent('ccd_3_21'))

