"""BantuNusantara URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from conf import api_urls
from core import views as core_views
from org import views as org_views
from org.views import RestrictedView

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('jara/', admin.site.urls),
    # home
    path('', core_views.home, name='home'),
    path(_('giver'), TemplateView.as_view(template_name="giver/info.html"), name='giver'),
    path('legal', TemplateView.as_view(template_name="footer/legal.html"), name='legal'),
    path(_('volunteer') + '/legal', TemplateView.as_view(template_name="volunteer/info.html"), name='volunteer_legal'),
    path(_('general_faq'), core_views.view_faq, name='general_faq'),
    path(_('contact_us'), TemplateView.as_view(template_name="footer/contact_us.html"), name='contact_us'),
    # help requests
    path(_('help_request'), TemplateView.as_view(template_name="help_request/info.html"), name='help_request'),
    path(_('request_form'), core_views.request_form, name="request-form"),
    path(_('request') + '/<int:id>', core_views.view_request, name='request-detail'),
    path(_('request_city') + '/<slug:city>', core_views.list_by_city, name='request-by-city'),
    path(_('request'), core_views.list_requests, name='request'),
    # donations
    path('ceder', org_views.donation_form, name="donation-form"),
    path('donar', RestrictedView.as_view()),
    path(_('donations'), org_views.list_donation, name='donations'),
    path(_('donation_by_city') + '/<slug:city>', org_views.list_donation_by_city, name='donation-by-city'),
    path(_('donations') + '/<int:id>', org_views.view_donation_center, name='donation-detail'),
    # volunteer
    path(_('volunteer'), TemplateView.as_view(template_name="volunteer/form.html"), name='volunteer'),
    # stats
    path('stats', core_views.stats, name='stats'),
    # login/logout
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += api_urls.urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
