from django.db import models
from datetime import datetime

class usage_data(models.Model):
	uuid = models.CharField(max_length=50)
	time_stamp = models.DateTimeField(editable=False)
	hostname = models.CharField(max_length=100)
	cpus = models.PositiveIntegerField()
	is_virtual = models.BooleanField()
	ent_virtual = models.BooleanField()
	ent_cluster = models.BooleanField()
	ent_lvs = models.BooleanField()
	ent_resilient = models.BooleanField()
	ent_scalable = models.BooleanField()
	ent_hpn = models.BooleanField()
	virtual_guests = models.PositiveIntegerField()

	def save(self, *args, **kwargs):
		if not self.id:
			self.time_stamp = datetime.now()
		super(usage_data, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.uuid
