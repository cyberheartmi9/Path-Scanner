import urllib


import  signal
import sys

print """
        ##################################################
        ##                                              ##
        ##          Author @intx0x80                    ##
        ##                                              ##
        ##            Path  Scanner                     ##
        ##                                              ##
        ##                                              ##
        ##                                              ##
        ##################################################

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
