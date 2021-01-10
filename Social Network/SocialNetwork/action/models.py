from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Action(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='action', db_index=True)
    verb = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    target_ct = models.ForeignKey(
        ContentType, 
        related_name='target', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True
    )
    target_id = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    target = GenericForeignKey(ct_field='target_ct', fk_field='target_id')
    class Meta:
        ordering = ('-created',)