import re
import paramiko
import datetime
import time
def get_ser_config(type):
    if type == 'XL001':
        ser_ip = '172.28.1.11'
        ser_un = 'gwac'
        ser_pw = 'gwac1234'
    if type == 'XL002':
        ser_ip = '190.168.1.203'
        ser_un = 'w60ccd'
        ser_pw = 'x'
    if type == 'XL003':
        ser_ip = '190.168.1.207'
        ser_un = 'ccduser'
        ser_pw = 'x'
    ser_con_list = [ser_ip, ser_un, ser_pw]
    return ser_con_list

def get_cam_config(cam_id):
    if cam_id == '1':
        cam_ip = '190.168.1.203'
        cam_un = 'w60ccd'
        cam_pw = 'x'
    if cam_id == '2':
        cam_ip = '190.168.1.201'
        cam_un = 'e60ccd'
        cam_pw = 'x'
    if cam_id == '3':
        cam_ip = '190.168.1.207'
        cam_un = 'ccduser'
        cam_pw = 'x'
    cam_con_list = [cam_ip, cam_un, cam_pw]
    return cam_con_list

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

def check_ser(type):
    if type in ['XL002','XL003']:
        ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
        cmd = 'ps -ef | grep gftservice | grep -v grep'
        res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
        if res:
            return True
        else:
            print("\nWARNING: The gftservice of %s is Error." % type)
            return False
    if type == 'XL001':
        ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
        cmd = 'ps -ef | grep gtoaes | grep -v grep'
        res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
        if res:
            return True
        else:
            print("\nWARNING: The gtoaes of %s is Error." % type)
            return False

def check_cam(cam_id):
    cam_ip, cam_un, cam_pw = get_cam_config(cam_id)[0:3]
    cmd = 'ps -ef | grep camagent | grep -v grep'
    res = con_ssh(cam_ip, cam_un, cam_pw, cmd)
    if res:
        return True
    else:
        print("\nThe camagent of %s is Error." % cam_id)
        return False

def get_free_teles_from_log(type):
    #gwac_init = ['002','004']
    gwac_frees = []
    f60_frees = []
    f30_frees = []
    cur_date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    ###group=XL001
    if type == 'XL002':
        if check_ser(type):
            ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
            cmd = 'ls /tmp/gftservice*.log'
            logs = con_ssh(ser_ip, ser_un, ser_pw, cmd)
            if logs:
                logs.reverse()
                print(logs)
                
                auto_mark = 0
                for log in logs:
                    log = log.strip()
                    for uid in ['1','2']:
                        cmd = "tac " + log + " | grep '<system id = %s> .* automatic .*' | head -1" % uid
                        print(cmd)
                        res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
                        print(res)
                        if res:
                            res = ''.join(res).strip()
                            res_time = re.search(r"^20\d\d-\d\d-\d\d \d\d:\d\d:\d\d", res).group(0)
                            res_time_utc = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(res_time, "%Y-%m-%d %H:%M:%S"))).strftime("%Y-%m-%d")
                            if res_time_utc == cur_date:
                                res_stat = re.search(r"<system id = 1> (.*?) automatic", res).group(1)
                                if res_stat == 'enter':
                                    if check_cam(uid):
                                        if uid == '1':
                                            f60_frees.append('001')
                                        if uid == '2':
                                            f60_frees.append('002')
                                        auto_mark = 1
                                    else:
                                        auto_mark = -1
                                else:
                                    auto_mark = -1
                            else:
                                auto_mark = -1
                    if auto_mark != 0:
                        break
                if auto_mark == 1:
                    return f60_frees
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    ###group=XL003
    if type == 'XL003':
        if check_ser(type):
            ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
            cmd = 'ls /tmp/gftservice*.log'
            logs = con_ssh(ser_ip, ser_un, ser_pw, cmd)
            if logs:
                logs.reverse()
                auto_mark = 0
                for log in logs:
                    log = log.strip()
                    cmd = "tac " + log + " | grep '<system id = 3> enter .* mode' | head -1"
                    res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
                    if res:
                        res = ''.join(res).strip()
                        res_time = re.search(r"^20\d\d-\d\d-\d\d \d\d:\d\d:\d\d", res).group(0)
                        res_time_utc = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(res_time, "%Y-%m-%d %H:%M:%S"))).strftime("%Y-%m-%d")
                        if res_time_utc == cur_date:
                            res_stat = re.search(r"<system id = 3> enter (.*?) mode", res).group(1)
                            if res_stat == 'automatic':
                                if check_cam('3'):
                                    f30_frees.append('001')
                                    auto_mark = 1
                                else:
                                    auto_mark = -1
                            else:
                                if check_cam('3'):
                                    print('\nWARNING: The system of XL003 is in idle mode now.')
                                auto_mark = -1
                        else:
                            auto_mark = -1
                    if auto_mark != 0:
                        break
                if auto_mark == 1:
                    return f30_frees
                else:
                    return 0
            else:
                return 0
        else:
            return 0
   



print(get_free_teles_from_log('XL002'))
