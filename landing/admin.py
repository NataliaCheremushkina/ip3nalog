from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Block


@admin.register(Block)
class BlockAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('block_title', 'sorting', 'title', 'status', 'menu_status')
    list_filter = ('status', 'menu_status')
    search_fields = ('block_title', 'title', 'content')
    ordering = ('sorting',)
