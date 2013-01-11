import urllib2
import xmlrpclib
import subprocess
from random import randint
import sys
import os
import glob


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

class test_data(object):
	def gen_uuid(self):
		print "Generating UUID..."
		uuid = subprocess.Popen(['uuidgen'], stdout=subprocess.PIPE).stdout.read().strip()
		return uuid

	def gen_hostname(self):
		envs = ['PROD', 'TEST', 'DEV', 'LAB']
		role = ['DB', 'APP', 'WEB', 'DMZ', 'FILESRV']
		hostname = envs[randint(0, len(envs) - 1)] + "-" + role[randint(0, len(role) - 1)] + "-" + str(randint(0, 3)) + str(randint(0, 6)) + str(randint(1, 9))
		return hostname

	def gen_boolean(self):
		boolean = randint(0,1)
		return boolean

if len(sys.argv) != 2:
	print "Error:", sys.argv[0], "takes exactly 1 argument (positive integer)."
	raise SystemExit

transport = HTTPProxyTransport({'http':'http://172.16.111.10:3128',})
#transport = HTTPProxyTransport({'http':'http://127.0.0.1:3128',})

try:
	server = xmlrpclib.Server('http://rhuidev-lvecchio.rhcloud.com/rhui_xmlrpc_server/', transport = transport)
except:
	print "Could not set up connection."

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
		dmidecode_uuid = subprocess.Popen(['dmidecode', '-s', 'system-uuid'], stdout = subprocess.PIPE)
		uuid = dmidecode_uuid.stdout.read().strip()
		return uuid
	
	def get_hostname(self):
		dmidecode_hostname = subprocess.Popen(['hostname'], stdout = subprocess.PIPE)
		hostname = dmidecode_hostname.stdout.read().strip()
		return hostname
	
	def get_is_virtual(self):
		vm_list = ['VMware, Inc.', 'QEMU']
		dmidecode_is_virtual = subprocess.Popen(['dmidecode', '-s', 'system-manufacturer'], stdout = subprocess.PIPE)
		is_virtual = dmidecode_is_virtual.stdout.read().strip()
		if is_virtual in vm_list:
			return 1
		else:
			return 0
	
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


def rhui_report():
	client = rhui_data_collector()
	uuid_val = client.get_uuid()
	hostname_val = client.get_hostname() 
	cpus_val = client.get_cpus()
        is_virtual_val = client.get_is_virtual()
        ent_virtual_val = client.find_rpm('libvirt')
        ent_cluster_val = client.find_rpm('cman')
        ent_lvs_val = client.find_rpm('piranha')
        ent_resilient_val = client.find_rpm('lvm2-cluster')
        ent_scalable_val = client.find_rpm('xfsdump')
        ent_hpn_val = client.find_rpm('rdma')
	ent_eus_val = client.find_rpm('rdma')
        virtual_guests_val = client.get_virtual_guest_count()
	try:
                print uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val
                server.commit_data(uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val)
                print "Insertion succesful"
        except:
                print "Could not insert data"

rhui_report()
