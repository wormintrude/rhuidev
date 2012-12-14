import urllib2
import xmlrpclib
import subprocess
from random import randint
import sys


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

for i in xrange(int(sys.argv[1])):
	server_data = test_data()
	uuid_val = server_data.gen_uuid()
	hostname_val = server_data.gen_hostname()
	cpus_val = randint(0,1)
        is_virtual_val = server_data.gen_boolean()
        ent_virtual_val = server_data.gen_boolean()
        ent_cluster_val = server_data.gen_boolean()
        ent_lvs_val = server_data.gen_boolean()
        ent_resilient_val = server_data.gen_boolean()
        ent_scalable_val = server_data.gen_boolean()
        ent_hpn_val = server_data.gen_boolean()
        ent_eus_val = server_data.gen_boolean()
        virtual_guests_val = randint(1, 30)
	try:
                print uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val
                server.commit_data(uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val)
                print "Insertion succesful"
        except:
                print "Could not insert data"

