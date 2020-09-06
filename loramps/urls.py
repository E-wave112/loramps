from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework import routers
from apps.views import api

schema = get_schema_view(
    title='Users API',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


events_urls_patterns = [
    path('events', api.EventsAPI.as_view()),
]


auth_urls_patterns = [
    path('login', api.LoginAPI.as_view()),
    path('register', api.RegisterAPI.as_view()),
    path('users', api.UserAPI.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/schema', schema),
    path('api/docs', include_docs_urls(title='Ticket System API')),
    path('api/auth/', include(auth_urls_patterns)),
    path('api/', include(events_urls_patterns)),
    path('', api.index),
]
