# -*- coding: utf-8 -*-
"""
    Util for backup device info.
    :copyright: (c) 2016 by yiwangwuqian.
"""
import os
import getpass
import plistlib

device_name_key = 'Device Name'

backup_path = '/Users/%s/Library/Application Support/MobileSync/Backup'%getpass.getuser()

def backup_dir_ls():
    names = []
    for dir in os.listdir(backup_path):
        if dir != ".DS_Store" and dir.find('-') <0:
            names.append(dir)
    return names

def device_ls(dir_list):
    device_names = []
    for dir_name in dir_list:
        upper_dir = os.path.join(backup_path,dir_name)
        path = os.path.join(upper_dir,'Info.plist')
#        try:
#            dict = plistlib.readPlist(path)
#            a_device_name = dict.get(device_name_key,None)
#            if a_device_name != None:
#                device_names.append(a_device_name)
#        except Exception , e:
#            print e
#            print 'path:'+path
#            continue
        dict = plistlib.readPlist(path)
        a_device_name = dict.get(device_name_key,None)
        if a_device_name != None:
            device_names.append(a_device_name)
    return device_names

def backup_dir_device_list():
    backup_dir_list = backup_dir_ls()
    device_name_list = device_ls(backup_dir_list)
    info_list = []
    if len(backup_dir_list) >0:
        for i in range(0,len(backup_dir_list)):
            info_list.append((os.path.join(backup_path,backup_dir_list[i]),device_name_list[i]))
    return info_list

def device_installed_app_list(one_backup_path):
    path = os.path.join(one_backup_path,'Info.plist')
    dict = plistlib.readPlist(path)
    bundle_ids = dict.get("Installed Applications",None)
    return bundle_ids

if __name__ == "__main__":
    print backup_dir_device_list()
