from get_gwac_camera import *
from gwac_camera_condition import *
from get_log import *
def obervartion_condition():
    message = dict()
    message['BeijingTime(UTC+8)'] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    obs_status = get_free_teles_from_log('XL002')
    if obs_status:
        message['obs'] = 'start'
    else:
        message['obs'] = 'stop'

    message['dome'] = 'Null'
    message['weather conditions'] = 'Null'
    message['gwac_camera(20)'] = gwac_camera_condition()
    if check_camagent('tele_w60') == 1 and check_gftservice('tele_w60') == 1:
        message['w60cm'] = 'online'
    else:
        message['w60cm'] = 'offline'

    if check_camagent('tele_e60') == 1 and check_gftservice('tele_w60') == 1:
        message['e60cm'] = 'online'
    else:
        message['e60cm'] = 'offline'

    if check_camagent('tele_30') == 1 and check_gftservice('tele_30') == 1:
        message['30cm'] = 'online'
    else:
        message['30cm'] = 'offline'

    return message

#message['gwac'] = check_camagent('ccd_3_21')
print(message)
