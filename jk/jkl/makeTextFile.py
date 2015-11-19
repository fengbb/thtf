__author__ = 'DN'
'makeTextFile.py --create text file'
import os
ls = os.linesep
print (ls)
fname = 'testp'
##get file
while True:
    if os.path.exists(fname):
        print("ERROR:'%s' already exists" % fname)
        break
    else:
        break
#get file content (text) lines
all = []
print ("\n Enter lines ('.' by itself to quit).\n")
## loop until user terminates input
while True:
    entry = input('>')
    if entry == '.':
        break
    else:
        all.append(entry)
## write lines to file with proper line_ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print ('DONE')
