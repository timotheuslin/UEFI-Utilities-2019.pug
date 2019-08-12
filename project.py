# Project configuration file for PUG.
#
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name, line-too-long
#
# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.
#

import os


#DEFAULT_EDK2_TAG = 'edk2-stable201903'
DEFAULT_EDK2_TAG = 'edk2-stable201905'

CODETREE = {
    # edk2-libc is a new edk2 repo since edk2-stable201905. StdLib resides in this repo.
    'edk2-libc'    : {
        'path'          : os.path.join(os.path.expanduser('~'), '.cache', 'pug', 'edk2-libc'),
        'source'        : {
            'url'       : 'https://github.com/tianocore/edk2-libc.git',
            'signature' : '6168716',   # 61687168fe02ac4d933a36c9145fdd242ac424d1 @ Apr/25/2019
        },
        'multiworkspace': True,
    },
    'UEFI-Utilities-2019'    : {
        'path'          : os.path.join(os.getcwd(), 'UEFI-Utilities-2019'),
        'source'        : {
            'url'       : 'https://github.com/fpmurphy/UEFI-Utilities-2019.git',
            'signature' : '',
        },
        'multiworkspace': True,
    }
}


###################################################################################################


if __name__ == '__main__':
    import sys
    sys.dont_write_bytecode = True      # To inhibit the creation of .pyc file

    PKG_DSC = 'MyApps/MyApps.dsc'
    IPUG_CMD = 'ipug -p {0} {1}'.format(PKG_DSC, ' '.join(sys.argv[1:]))
    print(IPUG_CMD)
    os.system(IPUG_CMD)
