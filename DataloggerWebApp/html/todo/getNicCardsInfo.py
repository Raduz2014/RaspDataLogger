#!/usr/bin/python
import subprocess, os, string, json
import StringIO
import netifaces

class Result:
    def __init__(self):
        self.exit_code = None
        self.stdout = None
        self.stderr = None
        self.command = None

def shellcmd(cmd = '', debug = None):
    result = Result()
    p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    (stdout, stderr) = p.communicate()
    result.exit_code = p.returncode
    result.stdout = stdout
    result.stderr = stderr
    result.command = cmd

    if p.returncode != 0:
        if debug == True:
            print 'Error exec cmd [%s]' % cmd
            print 'stderr: [%s]' % stderr
            print 'stdout: [%s]' % stdout
    
    return result

def checkWifiIface():
    res = shellcmd(cmd = "iwconfig", debug = None)
    out = StringIO.StringIO(res.stdout)
    c = out.getvalue()
    if len(c) > 0:
        wiface = c.split()[0]
        return wiface
    else:
        return None

def filterEth(x):
    if x.find('en', 0, 2) > -1:
        return True
    else:
        return False 
        
import re

def getNicCardsInfo(iface_type="eth"):
    ifaceNames = netifaces.interfaces()
    #aa = filter(filterEth, ifaceNames)
    myNetIfaces = []
    wifiiface = []
    for ii in ifaceNames:
        if iface_type == "eth":
            mm = re.match("(eth)|(en)", ii, re.M|re.I)
            if mm:
                myNetIfaces.append(ii)
        elif iface_type == "wlan":
            mm = re.match("(wl)", ii, re.M|re.I)
            if mm:
                myNetIfaces.append(ii)
    
    ifacesInfo = {}
    for iface in myNetIfaces:
        aa = netifaces.ifaddresses(iface.decode('utf-8'))
        ifacesInfo[iface] = {
            'ip': aa[netifaces.AF_INET],
            'mac':aa[netifaces.AF_LINK]
        }

    return ifacesInfo

def main():
    ips = getNicCardsInfo(iface_type = "eth")
    if len(ips) > 0:
        print ips
    else:
        print "No interfaces"
    #print checkWifiIface()
    

if __name__ == '__main__':
    main()