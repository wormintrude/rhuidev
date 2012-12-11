import xmlrpclib
import subprocess
from random import randint
import sys

# Connection to server
server = xmlrpclib.ServerProxy("http://rhuidev-lvecchio.rhcloud.com/rhui_xmlrpc_server/")
#server = xmlrpclib.ServerProxy("http://localhost:8000/rhui_xmlrpc_server/")

# Check that sysargv[1] exists and is an integer
if len(sys.argv) != 2:
	print "Error:", sys.argv[0], "takes exactly 1 argument (positive integer)."
	raise SystemExit

# UUID generation
def gen_uuid():
	print "Generating UUID..."
	return subprocess.Popen(['uuidgen'], stdout=subprocess.PIPE).stdout.read().strip()


# Random hostname generation.
def gen_hostname():
	envs = ['PROD', 'TEST', 'DEV', 'LAB']
	role = ['DB', 'APP', 'WEB', 'DMZ', 'FILESRV']
	return envs[randint(0, len(envs) - 1)] + "-" + role[randint(0, len(role) - 1)] + "-" + str(randint(0, 3)) + str(randint(0, 6)) + str(randint(1, 9))

# Random boolean generator (ok, ok, it's just for the sake of putting it into a function)
def gen_boolean():
	boolean = randint(0,1)
	return boolean

# Insertion of UUIDs into database alongside 'random' values for all other fields.
for i in xrange(int(sys.argv[1])):
	uuid_val = gen_uuid()
	hostname_val = gen_hostname()
	cpus_val = randint(0,1)
	is_virtual_val = gen_boolean()
	ent_virtual_val = gen_boolean()
	ent_cluster_val = gen_boolean()
	ent_lvs_val = gen_boolean()
	ent_resilient_val = gen_boolean()
	ent_scalable_val = gen_boolean()
	ent_hpn_val = gen_boolean()
	ent_eus_val = gen_boolean()
	virtual_guests_val = randint(1, 30)
	try:
		print uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val
		server.commit_data(uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val)
		print "Insertion succesful"
	except:
		print "Could not insert data"
