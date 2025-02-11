from django.urls import path, include

urlpatterns = [
    # path('employees/', include('core.modules.employees.urls')),
    path('customers/', include('drf_core.drf_modules.customers.urls')),
    path('auth/', include('drf_core.drf_modules.user.urls')),
    # path('products/', include('core.modules.products.urls')),
    # path('tasks/', include('core.modules.tasks.urls')),
]