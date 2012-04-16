__author__ = 'Dyachkov'

infile = "C:\\Temp\\tasks.txt"
outfile = "C:\\Temp\\outtasks.txt"

def dump(st):
    mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime = st
    print ('- size:', size, 'bytes')
    print ('- owner:', uid, gid)
    print ('- created:', time.ctime(ctime))
    print ('- last accessed:', time.ctime(atime))
    print ('- last modified:', time.ctime(mtime))
    print ('- mode:', oct(mode))
    print ('- inode/dev:', ino, dev)

st = os.stat(infile)
print ("Stat", infile)
dump(st)
print ("")

os.chmod(infile, stat.S_IMODE(st[stat.ST_MODE]))
print ("Stat", infile)
dump(st)
print ("")

# copy content

fi = open(infile, "rb")
fo = open(outfile, "wb")

while 1:
    s = fi.read(10000)
    if not s:
        break
    fo.write(s)

fi.close()
fo.close()

# copy mode and timestamp
st = os.stat(infile)
os.chmod(outfile, stat.S_IMODE(st[stat.ST_MODE]))
os.utime(outfile, (st[stat.ST_ATIME], st[stat.ST_MTIME]))

print ("original", "=>")
print ("mode", oct(stat.S_IMODE(st[stat.ST_MODE])))
print ("atime", time.ctime(st[stat.ST_ATIME]))
print ("mtime", time.ctime(st[stat.ST_MTIME]))

print ("copy", "=>")
st = os.stat(outfile)
print ("mode", oct(stat.S_IMODE(st[stat.ST_MODE])))
print ("atime", time.ctime(st[stat.ST_ATIME]))
print ("mtime", time.ctime(st[stat.ST_MTIME]))
  