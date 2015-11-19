# -*- coding: utf-8 -*-
import os
import shutil
import time
oldpath = 'D:\\test'
newpath = 'E:\\test'
def chageFile():
    if os.path.isdir(newpath):
        pass
    else:
        os.mkdir(newpath)
    for everyelem in os.listdir(oldpath):
        firstdir = everyelem[0]
        if '-' in everyelem:
            seconddir = everyelem.split('-')[0]
        else:
            seconddir = everyelem.split('.')[0]
        finalpath = newpath + '\\' + firstdir + '\\' + seconddir
        # print (finalpath)
        spath = oldpath + '\\' + everyelem
        if os.path.isdir(finalpath):
            filename = finalpath + '\\' + everyelem
            oldfilename = oldpath + '\\' + everyelem
            if os.path.exists(filename):
                fileinfo = os.stat(filename)
                filesize = os.path.getsize(filename)
                oldfilesize = os.path.getsize(oldfilename)
                #file_st_mtime = time.localtime(fileinfo.st_mtime)
                print ('oldfilesize' +' '+ oldfilename + 'size: %0.2fk' %(oldfilesize/1024) + ';'+'newfilesize' +' '+ filename + 'size:%0.2fk' %(filesize/1024))
                #print ('file exits in new path copy or not(y/n)')
                userinput = input('file exits in new path copy or not(\033[1;32;40m y/n\033[0m)')
                if userinput == 'y':
                    #print (userinput)
                    shutil.copy(spath, finalpath)
                else:
                    continue
            else:
                shutil.copy(spath, finalpath)
        else:
            os.makedirs(finalpath)
            shutil.copy(spath, finalpath)
def judgeIntExist():
    ln = []
    lp = []
    for i in range(1,20):
        m = "%0.3d" % i
        ln.append(m)
    #print (l)
    for everyelem in os.listdir(oldpath):
        lastname = everyelem.split('-')[1]
        intname = lastname[:3]
        #print (intname)
        if intname not in lp:
            lp.append(intname)
    #print (lp)
    ldiff = list(set(ln).difference(set(lp)))
    #print (ldiff)
if __name__ == '__main__':
    chageFile()
    judgeIntExist()
