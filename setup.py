#!/usr/bin/python
#
# Dell Recovery Media install script
# Copyright (C) 2008-2009, Dell Inc.
#  Author: Mario Limonciello <Mario_Limonciello@Dell.com>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from distutils.core import setup
from DistUtilsExtra.command import (build_extra, 
                                   build_i18n, 
                                   build_help,
                                   build_icons,
                                   clean_i18n)

import glob, os.path

I18NFILES = []
for filepath in glob.glob("po/mo/*/LC_MESSAGES/*.mo"):
    lang = filepath[len("po/mo/"):]
    targetpath = os.path.dirname(os.path.join("share/locale",lang))
    I18NFILES.append((targetpath, [filepath]))

setup(
    name="dell-recovery",
    author="Mario Limonciello",
    author_email="Mario_Limoncielo@Dell.com",
    maintainer="Mario Limonciello",
    maintainer_email="Mario_Limonciello@Dell.com",
    url="http://linux.dell.com/",
    license="gpl",
    description="Creates a piece of recovery media for a Dell Factory image",
    packages=["Dell"],
    data_files=[("share/dell", glob.glob("gtk/*.ui")),
                ('share/dell/bin', ['bto-autobuilder/dell-bto-autobuilder']),
                ('share/pixmaps', glob.glob("gtk/*.svg")),
                ('share/dell/bin', ['backend/recovery-media-backend']),
                ('share/dell/casper/scripts', glob.glob('casper/scripts/*')),
                ('share/dell/casper/hooks', glob.glob('casper/hooks/*')),
                ('share/dell/casper/seeds', glob.glob('casper/seeds/*')),
                ('share/dell/scripts', glob.glob('late/scripts/*')),
                ('share/dell/oie', glob.glob('oie/*')),
                ('share/dell/scripts/non-negotiable', glob.glob('late/chroot_scripts/*')),
                ('/etc/dbus-1/system.d/', glob.glob('backend/*.conf')),
                ('share/dell/grub', glob.glob('grub/*')),
                ('share/dell/grub/theme', glob.glob('bootloader_theme/*')),
                ('share/dbus-1/system-services', glob.glob('backend/*.service')),
                ('/lib/udev/rules.d', glob.glob('udev/*')),
                ('lib/ubiquity/plugins', glob.glob('ubiquity/*.py')),
                ('share/ubiquity/gtk', glob.glob('ubiquity/*.ui')),
                ('share/ubiquity', ['ubiquity/dell-bootstrap'])]+I18NFILES,
    scripts=["dell-recovery"],

    cmdclass = { 'build': build_extra.build_extra,
                 'build_i18n': build_i18n.build_i18n,
                 "build_help" : build_help.build_help,
                 'build_icons': build_icons.build_icons,
                 'clean': clean_i18n.clean_i18n,
               }
)

