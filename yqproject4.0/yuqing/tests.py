import paramiko 
import os 
import datetime 
# 需要加上信息
hostname='' 
username='' 
password='' 
port=
local_dir='/tmp/' 
remote_dir='/tmp/test/' 
if __name__=="__main__": 
 #    try: 
        t=paramiko.Transport((hostname,port)) 
        t.connect(username=username,password=password) 
        sftp=paramiko.SFTPClient.from_transport(t) 
#        files=sftp.listdir(dir_path) 
        files=os.listdir(local_dir) 
        for f in files: 
                print '' 
                print '#########################################' 
                print 'Beginning to upload file %s ' % datetime.datetime.now() 
                print 'Uploading file:',os.path.join(local_dir,f) 
 
               # sftp.get(os.path.join(dir_path,f),os.path.join(local_path,f)) 
                sftp.put(os.path.join(local_dir,f),os.path.join(remote_dir,f)) 
 
                print 'Upload file success %s ' % datetime.datetime.now() 
                print '' 
                print '##########################################' 
 
     #except Exception: 
#       print "error!" 
        t.close() 
