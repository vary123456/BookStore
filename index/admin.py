from django.contrib import admin
from index.models import *  #这个需要我们自己导入相应的模型类（数据表）
admin.site.register([Author, UserInfo, Pub])


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'retail_price', 'public1']

    # sortable_by = []
    # sorted('price')

    def public1(self, obj):
        return '出版社：' + obj.public.name
    public1.short_description = '出出出'
    public1.admin_order_field = 'public'

    # search_fields = ['title']
    # list_filter = ['title', 'price']
    # raw_id_fields = ['public']
    # list_display_links = ['title', 'public']
    # list_editable = ['price']
    fields = ('title', 'price',)
    # exclude = ('retail_price',)

# admin.site.register(Book, Book_Manager)


