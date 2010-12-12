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
""" Init """

from Products.CMFCore.DirectoryView import registerDirectory

from Products.GenericSetup import profile_registry
from Products.GenericSetup import EXTENSION

from Products.CPSDefault.Portal import CPSDefaultSite

from Products.CPSCore.interfaces import ICPSSite

registerDirectory('skins', globals())

import factory

class CpsDemoPortal(CPSDefaultSite):
    """ Just a marker.

    I'd rather add constructors to CPSDefault. Don't know if it'd work"""
    meta_type = 'CPS Demo Portal'

def initialize(registrar):
    profile_registry.registerProfile(
        'default',
        "cps-cms.org look and feel",
        "CPS demo portal extension profile",
        'profiles/default',
        'CpsDemoPortal',
        EXTENSION,
        for_=ICPSSite)

    registrar.registerClass(CpsDemoPortal,
                            constructors=(factory.addConfiguredCpsDemoPortalForm,
                                          factory.addConfiguredCpsDemoPortal))

