from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shop.views import ProductListView, ProductDetailView, MainView, CategoryListView, CategoryDetailView

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', MainView.as_view(), name='index'),

    url(r'^api/product/$', ProductListView.as_view(), name='product-list'),
    url(r'^api/product/(?P<id>[0-9]+)$', ProductDetailView.as_view(), name='product-detail'),

    url(r'^api/category/$', CategoryListView.as_view(), name='category-list'),
    url(r'^api/category/(?P<id>[0-9]+)$', CategoryDetailView.as_view(), name='category-detail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += staticfiles_urlpatterns()