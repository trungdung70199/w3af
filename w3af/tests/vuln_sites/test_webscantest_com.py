"""
test_webscantest_com.py

Copyright 2014 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
"""
from w3af.tests.vuln_sites.utils.scan_vulnerable_site import TestScanVulnerableSite
from w3af.plugins.tests.helper import PluginTest


class TestScanWebScanTestCom(TestScanVulnerableSite, PluginTest):

    target_url = 'http://www.webscantest.com'
    EXPECTED_VULNS = {()}
