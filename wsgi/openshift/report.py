#!/usr/bin/python

import xmlrpclib

class rhui_reporter(object):
	def __init__(self):
		pass

	def get_deltasum(self, server, uuid):
		sql = 'SELECT uuid, time, uptime, hostname, cpus, is_virt, entitlement_virt, entitlement_cluster, entitlement_lvs, entitlement_resilientstorage, entitlement_scalablefs, entitlement_hpn, entitlement_eus, virt_guests, sum(uptime) FROM rhuibilling.test_data WHERE uuid=\"' + str(uuid) + '\";'
	#	sql = 'SELECT sum(uptime) FROM rhuibilling.test_data WHERE uuid="' + str(uuid) + '";'
		sum = server.db_query(sql)
	#	return sum[0][0]
	#	print sum
		return sum[0]

	def get_billing_report(self, server, reporter):
		# server = xmlrpclib.Server('http://192.168.122.10:8888')
		# reporter = rhui_reporter()
		uuid_list = server.db_query('SELECT DISTINCT uuid FROM rhuibilling.test_data;')
		return uuid_list
		#for uuid in uuid_list:
  		#  result = reporter.get_deltasum(server, uuid[0]) #server.db_query(sql)
  		#  print 'Server: ' + str(result[0][0]) + ' | Unidades: ' + str(result[0][1])

	#def __str__(self, server, reporter):
	#	for uuid in reporter.get_billing_report(server, reporter):
	#	  print uuid
	#	  result = reporter.get_deltasum(server, uuid[0])
	#	  return 'Server: ' + str(result[0][0]) + ' | Unidades: ' + str(result[0][1])

#EOF
