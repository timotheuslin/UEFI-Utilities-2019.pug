# Project configuration file for PUG.
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

"""
TODO:
1. automate the LibraryClasses content of the existing INF using info from:
     1.1 their static_library_files.lst, and
     1.2 their $(BASE_NAME).map - 'Linker script and memory map'
2. automate the global/local (fixed) PCD settings from the -y/-Y build log.
"""

import os

DEFAULT_EDK2_TAG = 'edk2-stable201903'

CODETREE = {
    'PciUtils'    : {
        'path'          : os.path.join(os.getcwd(), 'UEFI-Utilities-2019'),
        'source'        : {
            'url'       : 'https://github.com/fpmurphy/UEFI-Utilities-2019.git',
            'signature' : '',
        },
        'multiworkspace': True,
    }
}

###################################################################################################

PKG_DSC = 'MyApps/MyApps.dsc'
MakefileContent = """
PKG_COMMAND	=   ipug -p {}

all :
	$(PKG_COMMAND)

clean :
	$(PKG_COMMAND) clean

cleanall :
	$(PKG_COMMAND) cleanall

""".format(PKG_DSC)

if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    MakefileName = "Makefile"
    if not os.path.exists(MakefileName):
        print('Creating: {}'.format(MakefileName))
        with open(MakefileName, 'w') as fout:
            fout.write(MakefileContent)
