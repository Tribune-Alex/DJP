from django.contrib import admin
from .models import Category, Product,ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    # optional: show image preview in admin
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="height:100px;" />'
        return ""
    image_preview.allow_tags = True
    image_preview.short_description = "Preview"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('name','price','quantity')
    list_display_links = ('name',)
    list_editable = ('price',)
    search_fields = ('name',)

admin.site.register(Category)