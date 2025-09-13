from django.urls import path
from main.views import render_all_json, render_all_xml, render_by_id_json, render_by_id_xml, render_create_product, render_main, render_product_details

app_name = 'main'

urlpatterns = [
    path('', render_main, name='show_main'),
    path('xml/', render_all_xml, name='render_all_xml'),
    path('xml/<str:id>/', render_by_id_xml, name='render_by_id_xml'),
    path('json/', render_all_json, name='render_all_json'),
    path('json/<str:id>/', render_by_id_json, name='render_by_id_json'),
    path('create_product/', render_create_product, name='render_create_product'),
    path('products/<str:id>/', render_product_details, name='render_product_details'),
]
