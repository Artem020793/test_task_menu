from django.contrib import admin
from .models import Menu, Dish

admin.site.site_header = "Menu Admin"
admin.site.site_title = "Our Menu"
admin.site.index_title = "Welcom to the Menu admin area"


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'price')


class DishInline(admin.TabularInline):
    model = Dish
    extra = 1


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = [(None, {'fields': ['title']}),
                 ('Dates',
                  {'fields': ['created_at'],
                   'classes': ['collapse']})
                 ]
    inlines = [DishInline]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)
