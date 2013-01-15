# RHUI CCP Tool  

## Prerequisites  

### RHEL 5.x
python >= 2.4.3  
dmidecode  

### RHEL 6.x  
python >= 2.6.5  
dmidecode  

### Proxy Server  
Unless you are planning on giving every one of your servers free range access to the interwebz, then you will need to have a proxy server through which the client can connect to the server.  
Any combination of type / ip address / port _should_ work (but might not!). This client has been tested exclusively against `squid`, making it the preferred choice.  

### IPTables  
If you are installing `squid` on the RHUA server, then chances are that you have completely forgotten that it has `iptables` enabled (don't worry, long hours of debugging were put in before we remembered it!).  
In order to allow connections to the proxy server, simply add the rule in `/etc/sysconfig/iptables`:  
    # /etc/sysconfig/iptables
    ...
    -A INPUT -p tcp --dport 3128 -j ACCEPT
    ...

Or, issue it via command line, save and restart:  

    # iptables -I INPUT -p tcp --dport 3128 -j ACCEPT
    # service iptables save
    # service iptables restart

## Installation  
Recommended destination is `/etc/cron.hourly`, so that the script runs on the hour, every hour.  

## Configuration  
The script now supports a configuration file at `/etc/rhui/rhui_xmlrpc_client.conf`.  
This configuration file consists of various sections with a predefined set of parameters.  
Please note that any parameters added to this file will be intentionally ignored.  

    [server]
    address = http://rhuidev-lvecchio.rhcloud.com/rhui_xmlrpc_server/
    
    [proxy]
    address = http://172.16.111.10:3128
    
    [partner]
    name = Red Hat
    contact = vecchioli@redhat.com
    
    [end-user]
    name = Mariano Vecchioli
    country = Argentina
    postal_code = 1066
    contact = vecchioli@redhat.com

## Running  
The script can be run from anywhere by invoking it via `/usr/bin/python /path/to/rhui_xmlrpc_client_proxy.py`.  

## Troubleshooting  
Whatever-the-name-of-this-is now comes with a log!  
Well, kinda. Head over to `/var/log/rhui_xmlrpc_client.log` and check it out.  
There are `INFO`, `WARNING` and `ERROR` levels.  

## Questions ?  
Send an email to vecchioli@redhat.com and allow for up to 48 hours for a
response!  

