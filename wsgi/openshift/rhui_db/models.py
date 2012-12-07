from django.db import models
from datetime import datetime

class usage_data(models.Model):
	uuid = models.CharField(max_length=50)
	time_stamp = models.DateTimeField(editable=False)
	hostname = models.CharField(max_length=100)
	cpus = models.PositiveIntegerField()
	is_virtual = models.BooleanField()
	entitlement_virt = models.BooleanField()
	entitlement_cluster = models.BooleanField()
	entitlement_lvs = models.BooleanField()
	entitlement_resilientstorage = models.BooleanField()
	entitlement_scalablefs = models.BooleanField()
	entitlement_hpn = models.BooleanField()
	entitlement_eus = models.BooleanField()
	virtual_guests = models.PositiveIntegerField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.time_stamp = datetime.now()
		super(usage_data, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.uuid
