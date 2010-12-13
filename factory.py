# (C) Copyright 2010 CPS-CMS community <http://cps-cms.org/>
# Authors:
# M.-A. Darche <cps@cynode.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""CPS demo portal factory."""

from Products.CPSDefault.metafactory import CPSSiteMetaConfigurator

#
# Callables for meta profiles
#

def removeCookieCrumbler(site):
    site.manage_delObjects(['cookie_authentication'])

class SiteConfigurator(CPSSiteMetaConfigurator):
     """CPS demo portal configurator"""

     meta_profiles = {
         'CPS_DEMO': {'title' : 'Common set of components',
                             'extensions': ('CPSRSS:default',
                                            'CPSSubscriptions:default',
                                            'CPSDefault:folder_advanced_display',
                                            'CPSTramline:cpsdefault-all',
                                            'CpsDemoPortal:default',
                                            ),
                          'optional' : False,
                          'parameters' : {'attributes': ('smtp_host',
                                                         'smtp_port',
                                                         'smtp_pwd',
                                                         'smtp_uid'),
                                          'class': 'Products.MailHost.'
                                                   'MailHost.MailHost',
                                          'rpath' : 'MailHost'},
                          }
         }
     metas_order = ('CPS_DEMO',
                    )
     form_heading = "Add CPS demo portal"
     post_action = 'addConfiguredCpsDemoPortal'

_cpsconfigurator = SiteConfigurator()

# GR: straight from CPSDefault.factory
# Do the following dance because bound methods don't play well with
# constructors registered for products.

def addConfiguredCpsDemoPortalForm(dispatcher):
    """Form to add a CPS Site from ZMI.
    """
    return _cpsconfigurator.addConfiguredSiteForm(dispatcher)

def addConfiguredCpsDemoPortal(dispatcher, REQUEST=None, **kw):
    """Add a CPSSite according to profile and extensions.
    """
    if REQUEST is not None:
        kw.update(REQUEST.form)
    return _cpsconfigurator.addConfiguredSite(dispatcher,
                                              REQUEST=REQUEST, **kw)
