# RHUI CCP Tool  

## Prerequisites  

### RHEL 5.x
python >= 2.4.3  
dmidecode  

### RHEL 6.x  
python >= 2.6.5  
dmidecode  

## Installation  
The script can be installed to anywhere in the system that `root` has access to (so, anywhere).  
Recommended destination is `/sbin`, mererly due to the fact that end-users will feel less inclined to erase it.  

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
Ideally, you would run it either via cron, from roots crontab:  

    * */1 * * * /usr/bin/python /sbin/rhui_xmlpc_client_proxy.py

Or, via `/etc/cron.hourly`.  

## Troubleshooting  
Whatever-the-name-of-this-is now comes with a log!  
Well, kinda. Head over to `/var/log/rhui_xmlrpc_client.log` and check it out.  
There are `INFO`, `WARNING` and `ERROR` levels.  

## Questions ?  
Send an email to vecchioli@redhat.com and allow for up to 48 hours for a
response!  

