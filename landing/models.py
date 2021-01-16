from django.db import models


class VisibleBlockManager(models.Manager):
    def get_queryset(self):
        return super(VisibleBlockManager, self).get_queryset().filter(status='visible').order_by('sorting')


class VisibleMenuManager(models.Manager):
    def get_queryset(self):
        return super(VisibleMenuManager, self).get_queryset().filter(menu_status='visible').order_by('sorting')


class Block(models.Model):
    STATUS_CHOICES = (
        ('visible', 'Visible'),
        ('invisible', 'Invisible'),
    )
    sorting = models.PositiveIntegerField(default=999)
    block_id = models.CharField(max_length=20, default='default')
    block_title = models.CharField(max_length=250)
    title = models.CharField(max_length=250, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='invisible')
    menu_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='invisible')
    objects = models.Manager()
    visible_block = VisibleBlockManager()
    visible_menu = VisibleMenuManager()
