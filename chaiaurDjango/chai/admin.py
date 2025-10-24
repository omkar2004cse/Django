from django.contrib import admin
from .models import chaiVarity, chai_review, store, cetificate


# register your models here
class chai_review_inline(admin.TabularInline):
    model=chai_review
    extra=1


class chaiVarityAdmin(admin.ModelAdmin):
    list_display=('name','type', 'date_added')
    inlines=[chai_review_inline]

class storeAdmin(admin.ModelAdmin):
    list_display=("names","location")
    filter_horizontal=('chai_varieties',)

class chai_certificate(admin.ModelAdmin):
    list_display=("chai_n","certificate_number")

admin.site.register(chaiVarity,chaiVarityAdmin)
admin.site.register(store,storeAdmin)
admin.site.register(cetificate,chai_certificate)

# admin.site.register(chaiVarity)
# @admin.register(chaiVarity)
# class chaiVarityAdmin(admin.ModelAdmin):
#     list_display = ('name', 'type', 'description')