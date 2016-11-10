"""
    This module implement read info from iOS 10 backup files.
    :copyright: (c) 2016 by yiwangwuqian.
"""

import os
import sqlite3
import hashlib

def get_files_info(backup_base_path,iterator_callback=None):
    sql = "SELECT * FROM Files"
    db_path = os.path.join(backup_base_path, 'Manifest.db')
    connect = sqlite3.connect(db_path)
    info_list = []
    for row in connect.execute(sql):
        domain = row[1]
        relativePath = row[2]
        flags = row[3]
        info = {}
        info['fileID'] = hashlib.sha1(domain +'-'+ relativePath).hexdigest()
        info['domain'] = domain
        info['filename'] = relativePath
        if flags == 1:
            info['type'] = 'f' #file
        elif flags ==2:
            info['type'] = 'd' #dir
        else:
            info['type'] = '?' #unknown
        info_list.append(info)

    return info_list

def extern_run(backup_path, iterator_callback):
    if iterator_callback == None:
        return
    info_list = get_files_info(backup_path)
    for i in range(0,len(info_list)):
        iterator_callback(info_list[i])

# if __name__ == '__main__':
#     get_files_info("")