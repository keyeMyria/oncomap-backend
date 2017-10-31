from django.contrib import admin

from .models import Resource, Voting


class VotingAdmin(admin.ModelAdmin):
    list_display = ('resource', 'created_date', 'name', 'value', 'comment')
admin.site.register(Voting, VotingAdmin)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('created', 'rating')
admin.site.register(Resource, ResourceAdmin)
