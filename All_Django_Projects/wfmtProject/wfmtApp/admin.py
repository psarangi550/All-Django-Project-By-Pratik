from django.contrib import admin
from .models import WFMT_JOBS
# Register your models here.
class WFMT_JOBS_ADMIN(admin.ModelAdmin):
    list_display=['id','cp_number','sne_id','scheme_number','trs_area','cp_details']
admin.site.register(WFMT_JOBS,WFMT_JOBS_ADMIN)
