from django.contrib import admin

# Register your models here.

from .models import Product, About, Slider, Media


class AboutAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 1:
      return False
    else:
      return True

admin.site.register(About, AboutAdmin)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title']

class SliderAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    num_objects = self.model.objects.count()
    if num_objects >= 3:
      return False
    else:
      return True

admin.site.register(Slider, SliderAdmin)

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['title']
