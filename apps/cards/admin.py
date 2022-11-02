from django.contrib import admin

from .models import Card


@admin.action(description='Mark selected cards as visible')
def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)


@admin.action(description='Mark selected cards as invisible')
def make_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)


class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'visible')
    actions = [make_visible, make_invisible]


admin.site.register(Card, CardAdmin)
