from django.conf import settings
from django.utils.translation import ugettext_lazy as _

# Service group names (global across all projects):
MONITORING_SERVICES_GROUPS = [
    {'name': _('OpenStack Services'), 'groupBy': 'service'},
    {'name': _('Servers'), 'groupBy': 'hostname'},
    {'name': _('Virtual Machines'), 'groupBy': 'resource_name'}
]

# Services being monitored
MONITORING_SERVICES = getattr(
    settings,
    'MONITORING_SERVICES_GROUPS',
    MONITORING_SERVICES_GROUPS
)

#
# Per project service groups.  If in this form,
# '*' will be applied to all projects not explicitly listed.
#
# Note the above form (flat) is supported for backward compatibility.
#
# MONITORING_SERVICES_GROUPS = [
#    {'admin': [
#         {'name': _('OpenStack Services'), 'groupBy': 'service'},
#         {'name': _('Servers'), 'groupBy': 'hostname'}]},
#    {'*': [
#         {'name': _('Services'), 'groupBy': 'service'},
#         {'name': _('Instances'), 'groupBy': 'hostname'}]},
# ]

MONITORING_SERVICE_TYPE = getattr(
    settings, 'MONITORING_SERVICE_TYPE', 'monitoring'
)

# Grafana button titles/file names (global across all projects):
GRAFANA_LINKS = []
DASHBOARDS = getattr(settings, 'GRAFANA_LINKS', GRAFANA_LINKS)

#
# Horizon will link to the grafana home page when using Grafana2.
# For any Grafana version additional links to specific dashboards can be
# created in two formats.
# Flat:
# GRAFANA_LINKS = [ {'title': _('Dashboard'), 'path': 'openstack'} ]
#
# Per project: '*' will be applied to all projects not explicitly listed.
# GRAFANA_LINKS = [
#    {'admin': [
#        {'title': _('Dashboard'), 'path': 'openstack'}]},
#    {'*': [
#        {'title': _('OpenStack Dashboard'), 'path': 'project'}]}
# ]

GRAFANA_URL = getattr(settings, 'GRAFANA_URL', True)
GRAFANA_URL = {'RegionOne': "http://172.30.64.89:3000", }

ENABLE_KIBANA_BUTTON = getattr(settings, 'ENABLE_KIBANA_BUTTON', True)
KIBANA_HOST = getattr(settings, 'KIBANA_HOST', 'http://172.30.64.89:5601/')

KIBANA_URL = 'http://172.30.64.89/dashboard/monitoring/logs_proxy'

OPENSTACK_SSL_NO_VERIFY = getattr(settings, 'OPENSTACK_SSL_NO_VERIFY', False)
OPENSTACK_SSL_CACERT = getattr(settings, 'OPENSTACK_SSL_CACERT', None)
