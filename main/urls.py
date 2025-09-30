from django.urls import path
from main.views import render_all_json, render_all_xml, render_by_id_json, render_by_id_xml, render_create_product, render_delete_product, render_edit_product, render_login, render_logout, render_main, render_product_details, render_register

app_name = 'main'

urlpatterns = [
    path('', render_main, name='show_main'),
    path('xml/', render_all_xml, name='render_all_xml'),
    path('xml/<str:id>/', render_by_id_xml, name='render_by_id_xml'),
    path('json/', render_all_json, name='render_all_json'),
    path('json/<str:id>/', render_by_id_json, name='render_by_id_json'),
    path('create_product/', render_create_product, name='render_create_product'),
    path('products/<str:id>/', render_product_details, name='render_product_details'),
    path('products/<str:id>/edit', render_edit_product, name='render_edit_product'),
    path('products/<str:id>/delete', render_delete_product, name='render_delete_product'),
    path('register/', render_register, name='render_register'),
    path('login/', render_login, name='render_login'),
    path('logout/', render_logout, name='render_logout')
]
