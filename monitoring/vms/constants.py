# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from django.conf import settings

URL_PREFIX = 'horizon:monitoring:vms:'
TEMPLATE_PREFIX = 'monitoring/vms/'

prefix = settings.STATIC_URL or ''
CRITICAL_ICON = 'fa fa-times'
WARNING_ICON = 'fa fa-exclamation-traingle'
MEDIUM_ICON = 'fa fa-exclamation'
LOW_ICON = 'fa fa-power-off'
OK_ICON = 'fa fa-check-square'
UNKNOWN_ICON = 'fa fa-hourglass-half'
NOTFOUND_ICON = 'fa fa-ban'
