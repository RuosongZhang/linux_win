def get_free_teles_from_log(type):
    #gwac_init = ['002','004']
    gwac_frees = []
    f60_frees = []
    f30_frees = []
    cur_date = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    ###group=XL001
    if type == 'XL001':
        if check_ser(type):
            ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
            cmd = 'ls /var/log/gtoaes/gtoaes*.log'
            logs = con_ssh(ser_ip, ser_un, ser_pw, cmd)
            if logs:
                logs.reverse()
                auto_mark1 = 0
                for id in gwac_init:
                    auto_mark2 = 0
                    for log in logs:
                        log = log.strip()
                        log_date = re.search(r"20\d\d\d\d\d\d", log).group(0)
                        log_date = time.strftime("%Y-%m-%d",time.strptime(log_date, "%Y%m%d"))
                        cmd = "tac %s | grep 'Mount<001:%s> is .*line' | head -1" % (log, id)
                        res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
                        if res:
                            res = ''.join(res).strip()
                            res_time = re.search(r"^\d\d:\d\d:\d\d", res).group(0)
                            res_time = "%s %s" % (log_date, res_time)
                            res_time_utc = datetime.datetime.utcfromtimestamp(time.mktime(time.strptime(res_time, "%Y-%m-%d %H:%M:%S"))).strftime("%Y-%m-%d")
                            if res_time_utc == cur_date:
                                res_stat = re.search(r"is (.*?)-line", res).group(1)
                                if res_stat == 'on':
                                    gwac_frees.append(id)
                                    auto_mark1 += 1
                                else:
                                    auto_mark2 = -1
                            else:
                                auto_mark2 = -1
                        if auto_mark2 != 0:
                            break
                if auto_mark1 >= 1:
                    return gwac_frees
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    ###group=XL002
    if type == 'XL002':
        if check_ser(type):
            ser_ip, ser_un, ser_pw = get_ser_config(type)[0:3]
            cmd = 'ls /tmp/gftservice*.log'
            logs = con_ssh(ser_ip, ser_un, ser_pw, cmd)
            if logs:
                logs.reverse()
                auto_mark = 0
                for log in logs:
                    log = log.strip()
                    for uid in ['1','2']:
                        cmd = "tac " + log + " | grep '<system id = %s> .* automatic .*' | head -1" % uid
                        res = con_ssh(ser_ip, ser_un, ser_pw, cmd)
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
                                    print '\nWARNING: The system of XL003 is in idle mode now.'
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