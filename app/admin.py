from django.contrib import admin

# Register your models here.


from .models import Men
from .models import Portfolio
from .models import Blog


class MenAdmin(admin.ModelAdmin):
    list_display = ['ism_sharif','telefon','email']
    list_per_page = 10
    search_fields = ['ism_sharif','phone', 'email']
    class Meta:
        model = Men
admin.site.register(Men,MenAdmin)



class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['nom', 'malumot']
    list_per_page = 10
    search_fields = ['nom', 'malumot']
    class Meta:
        model = Portfolio
admin.site.register(Portfolio,PortfolioAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['rasm', 'mavzu', 'malumot']
    list_per_page = 10
    search_fields = ['rasm', 'mavzu', 'malumot']
    class Meta:
        model = Blog
admin.site.register(Blog,BlogAdmin)