import xmlrpclib
import subprocess
from random import randint

server = xmlrpclib.ServerProxy("http://localhost:8000/rhui_xmlrpc_server/")
#server.db_read()

# UUID list generation
def gen_uuid_list(range):
	uuid_list = []
	for i in xrange(range):
		gen_uuid = subprocess.Popen(['uuidgen'], stdout=subprocess.PIPE)
		uuid_list.append(gen_uuid.stdout.read().strip())
	return uuid_list

uuid_list = gen_uuid_list(10000)

# Random hostname generation.
def gen_hostname():
	pass

# Random boolean generator (ok, ok, it's just for the sake of putting it into a function)
def gen_boolean():
	boolean = randint(0,1)
	return boolean

# Insertion of UUIDs into database alongside 'random' values for all other fields.
for uuid in uuid_list:
	uuid_val = uuid
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
		server.commit_data(uuid_val, hostname_val, cpus_val, is_virtual_val, ent_virtual_val, ent_cluster_val, ent_lvs_val, ent_resilient_val, ent_scalable_val, ent_hpn_val, ent_eus_val, virtual_guests_val)
		return "Insertion succesful"
	except:
		return "Could not insert data"
