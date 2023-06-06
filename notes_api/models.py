from django.db import models

import uuid

class NoteModel(models.Model):
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	title=models.CharField(max_length=255,unique=True)
	content=models.TextField()
	category=models.CharField(max_length=100, null=True,blank=True)
	createdAt=models.DateTimeField(auto_now_add=True)
	uploadedAt=models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table='notes'
		ordering=['-createdAt']

		def __str__(self):
			return self.title