#-*-coding:utf8-*-
import itchat
itchat.auto_login(hotReload=True)

friends = itchat.get_friends()
print('friends')

itchat.send(msg='success', toUserName='wxid_kza9zg4cx47v51')

