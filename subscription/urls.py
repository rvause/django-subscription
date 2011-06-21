from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required

import views

urlpatterns = patterns('',
    (
        r'^$',
        permission_required('subscription.can_view')(views.subscription_list),
        {},
        'subscription_list'
    ),
    (
        r'^(?P<object_id>\d+)/$',
        permission_required('subscription.can_view')(views.subscription_detail),
        {},
        'subscription_detail'
    ),
    (
        r'^(?P<object_id>\d+)/(?P<payment_method>(standard|pro))$',
        permission_required('subscription.can_view')(views.subscription_detail),
        {},
        'subscription_detail'
    ),
)

urlpatterns += patterns('',
    (r'^paypal/', include('paypal.standard.ipn.urls')),
    (r'^done/', 'django.views.generic.simple.direct_to_template', dict(template='subscription/subscription_done.html'), 'subscription_done'),
    (r'^change-done/', 'django.views.generic.simple.direct_to_template', dict(template='subscription/subscription_change_done.html', extra_context=dict(cancel_url=views.cancel_url)), 'subscription_change_done'),
    (r'^cancel/', 'django.views.generic.simple.direct_to_template', dict(template='subscription/subscription_cancel.html'), 'subscription_cancel'),
    )
