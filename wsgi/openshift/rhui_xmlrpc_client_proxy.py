#!/usr/bin/python

import urllib2
import xmlrpclib
import subprocess
from random import randint
import sys
import os
import glob
from ConfigParser import SafeConfigParser
import logging

# First things first, set up logging
rhui_logger = logging.getLogger('rhui_xmlrpc_client')
rhui_log_handler = logging.FileHandler('/var/log/rhui_xmlrpc_client.log')
rhui_log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
rhui_log_handler.setFormatter(rhui_log_formatter)
rhui_logger.addHandler(rhui_log_handler)
rhui_logger.setLevel(logging.INFO)

# 
class Urllib2Transport(xmlrpclib.Transport):
    def __init__(self, opener=None, https=False, use_datetime=0):
	if hasattr(xmlrpclib.Transport, '__init__'):
        	xmlrpclib.Transport.__init__(self, use_datetime)
        self.opener = opener or urllib2.build_opener()
        self.https = https
    
    def request(self, host, handler, request_body, verbose=0):
        proto = ('http', 'https')[bool(self.https)]
        req = urllib2.Request('%s://%s%s' % (proto, host, handler), request_body)
        req.add_header('User-agent', self.user_agent)
        self.verbose = verbose
        return self.parse_response(self.opener.open(req))


class HTTPProxyTransport(Urllib2Transport):
    def __init__(self, proxies, use_datetime=0):
        opener = urllib2.build_opener(urllib2.ProxyHandler(proxies))
        Urllib2Transport.__init__(self, opener, use_datetime)


# Data Collector
class rhui_data_collector(object):
	rpm_list = []

	def __init__(self):
		import rpm
		t_set = rpm.TransactionSet()
		db_match = t_set.dbMatch()
		for rpm in db_match:
			self.rpm_list.append(rpm['name'])
	
	def get_rpm_list(self):
		for rpm in self.rpm_list:
			print rpm
	
	def find_rpm(self, rpm):
		if rpm in self.rpm_list:
			return 1
		else:
			return 0
	
	def get_uuid(self):
		dmidecode_uuid = subprocess.Popen(['/usr/sbin/dmidecode', '-s', 'system-uuid'], stdout = subprocess.PIPE)
		uuid = dmidecode_uuid.stdout.read().strip()
		return uuid
	
	def get_hostname(self):
		dmidecode_hostname = subprocess.Popen(['/bin/hostname'], stdout = subprocess.PIPE)
		hostname = dmidecode_hostname.stdout.read().strip()
		return hostname
	
	def get_sys_info(self):
		dmidecode_sys_info = subprocess.Popen(['/usr/sbin/dmidecode', '-s', 'system-manufacturer'], stdout = subprocess.PIPE)
		sys_info = dmidecode_sys_info.stdout.read().strip()
		return sys_info
	
	def get_cpus(self):
		cpus = os.sysconf("SC_NPROCESSORS_ONLN")
		return cpus
	
	def get_virtual_guest_count(self):
		vms_list = []
		vms_path = '/etc/libvirt/qemu/'

		if os.path.exists(vms_path):
			for file in glob.glob(vms_path + '*.xml'):
				vms_list.append(file)
			vm_count = len(vms_list)
			return vm_count
		else:
			vm_count = 0
			return vm_count




# Configuration file parsing
config_parser = SafeConfigParser()
config_file = '/etc/rhui/rhui_xmlrpc_client.conf'

# Read config_file
try:
	config_parser.read(config_file)
except:
	rhui_logger.error('There is no configuration file')
	sys.exit(0)

# Set values from config_file
rhui_server_url = config_parser.get('server', 'address')
proxy_address = config_parser.get('proxy', 'address')
partner_name = config_parser.get('partner', 'name')
partner_contact = config_parser.get('partner', 'contact')
end_user_name = config_parser.get('end-user', 'name')
end_user_country = config_parser.get('end-user', 'country')
end_user_postal_code = config_parser.get('end-user', 'postal_code')
end_user_contact = config_parser.get('end-user', 'contact')


# Report function is declared _after_ config parsing because we are going to need some details from that
def rhui_report():
	client = rhui_data_collector()
	uuid_val = client.get_uuid()
	hostname_val = client.get_hostname() 
	cpus_val = client.get_cpus()
        sys_info_val = client.get_sys_info()
        ent_virtual_val = client.find_rpm('libvirt')
        ent_cluster_val = client.find_rpm('cman')
        ent_lvs_val = client.find_rpm('piranha')
        ent_resilient_val = client.find_rpm('lvm2-cluster')
        ent_scalable_val = client.find_rpm('xfsdump')
        ent_hpn_val = client.find_rpm('rdma')
        virtual_guests_val = client.get_virtual_guest_count()
	try:
                print 'Uploading data to server:', partner_name, partner_contact, end_user_name, end_user_country, end_user_postal_code, end_user_contact, uuid_val, hostname_val, cpus_val, sys_info_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, virtual_guests_val
                server.commit_data(partner_name, partner_contact, end_user_name, end_user_country, end_user_postal_code, end_user_contact, uuid_val, hostname_val, cpus_val, sys_info_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, virtual_guests_val)
                rhui_logger.info('Succesfully uploaded data to server')
        except:
                rhui_logger.error('Could not insert data')
		sys.exit(0) 


# Set the transport - also need config parsing for this
transport = HTTPProxyTransport({'http':proxy_address,}) # FIXME - Possible breakage if there is no proxy defined

# Establish connection to server or die trying
try:
	server = xmlrpclib.Server(rhui_server_url, transport = transport)
	rhui_logger.info('Connected to server')
except:
	rhui_logger.error('Could not set up connection to server.')
	sys.exit(0) 

# Upload the report to the rhui server on openshift
rhui_report()
