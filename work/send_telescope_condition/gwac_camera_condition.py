from get_gwac_camera import *
def gwac_camera_condition():
    usable_camera = 0
    camera_list = ['ccd_3_21', 'ccd_3_22','ccd_3_23', 'ccd_3_24', 'ccd_3_25', 'ccd_3_31', 'ccd_3_32', 'ccd_3_33', 'ccd_3_34','ccd_3_35', 'ccd_3_41', 'ccd_3_42', 'ccd_3_43', 'ccd_3_44', 'ccd_3_45']
    for camera in camera_list:
        usable_camera = usable_camera + check_camagent(camera)
    return usable_camera
    print(usable_camera)




