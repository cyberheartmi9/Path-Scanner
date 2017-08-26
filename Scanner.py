import urllib


import  signal
import sys

print """
       
    ____        __  __       
   / __ \____ _/ /_/ /_      
  / /_/ / __ `/ __/ __ \     
 / ____/ /_/ / /_/ / / /     
/_/    \__,_/\__/_/ /_/      
                             



     _______.  ______     ___      .__   __. .__   __.  _______ .______      
    /       | /      |   /   \     |  \ |  | |  \ |  | |   ____||   _  \     
   |   (----`|  ,----'  /  ^  \    |   \|  | |   \|  | |  |__   |  |_)  |    
    \   \    |  |      /  /_\  \   |  . `  | |  . `  | |   __|  |      /     
.----)   |   |  `----./  _____  \  |  |\   | |  |\   | |  |____ |  |\  \----.
|_______/     \______/__/     \__\ |__| \__| |__| \__| |_______|| _| `._____|
                                                                             

@intx0x80

"""


def signal_handler(signal, frame):

    print "\n[-] Exiting"

    exit()

signal.signal(signal.SIGINT, signal_handler)



url=raw_input("Enter URL Address    ")






f=open('db.txt','r')

for i in f.readlines():

    ur=urllib.urlopen('http://'+url+'/'+'{}'.format(i))
    if ur.code==200:
                print '#########################################'
                print   ' [Found]------->   '+ str(ur.geturl()) +'  code is '+str(ur.code)
                print '##########################################'
                f1=open('Found.txt','a')
                f1.writelines('Found------->  '+ str(ur.geturl()) +'  code is '+str(ur.code)+'\n')
    else:
        print 'Not Found------->'+str(ur.geturl()) +'   code is '+str(ur.code)
print "\nScanning....... complete"

print "  #################  Banner #################"
print ur.headers 

print "#############################################"
#f1.writelines("Banner \n"+ur.headers)
