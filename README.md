UEFI-Utilities-2019.pug
===
**UEFI-Utilities-2019.pug** provides a front-end solution that simplifies the build process of Finnbarr P. Murphy's [UEFI-Utilities-2019](https://github.com/fpmurphy/UEFI-Utilities-2019) using [PUG](https://github.com/timotheuslin/PugPkg).

## Prerequisites:
1. Python 2.7.10+ or Python 3.7.0+
2. git 2.17.0+

## Generic prerequisites for the UDK build:
0. Reference:
    - [Getting Started with EDK II](https://github.com/tianocore/tianocore.github.io/wiki/Getting%20Started%20with%20EDK%20II) 
    - [Xcode](https://github.com/tianocore/tianocore.github.io/wiki/Xcode)
1. nasm (2.0 or above)
2. iasl (version 2018xxxx or later)
3. MSVC(Windows) or Xcode(Mac) or GCC(Open-source Posix)
4. build-essential uuid-dev (Posix)
5. pip2 install future (Python 2.7.x)
6. motc (Xcode)

## Tool installation for any Debian-Based Linux:
 `$ sudo apt update ; sudo apt install nasm iasl build-essential uuid-dev`

## Usage: 
1. `git clone https://github.com/timotheuslin/UEFI-Utilities-2019.pug.git`
2. In the command console, change-directory to folder **UEFI-Utilities-2019.pug** .
3. (Optional) Edit `CODETREE` in `config.py` to specify where to place the downloaded source files of the UDK git repo or any other additional respos.
4. (Optional) Edit `config.py` for the settings accordingly in: `WORKSPACE`, `TARGET_TXT`.
5. To build the code, run `make` (Linux) or `nmake` (Windows) or `python pug.py -p MyApps/MyApps.dsc` <br>
    For the 1st time setup, `pug.py` would automatically try to git-clone:
    - the [UDK code tree](https://github.com/tianocore/edk2)
    - the openssl repo (a recursive submodule)
    - Finnbarr P. Murphy's [UEFI-Utilities-2019](https://github.com/fpmurphy/UEFI-Utilities-2019)
6. Browse to folder **Build/MyApps** for the build results.
7. Browse to folder **Build/Pug/Conf** for CONF_PATH setting files.
8. Run `{make, nmake, "python pug.py -p MyApps/MyApps.dsc"} {clean, cleanall}` to clean (all) the intermediate files.

## Known issues:
1. Working for Linux/GCC only. Windows/MSVC has some C99 incompatibility issues to deal with. Xcode is not tested.
2. The original UEFI-Utilities-2019 has [two trivial build issues](https://github.com/fpmurphy/UEFI-Utilities-2019/issues/3) to fix as well.


## Tech notes:
1. The full [UDK code tree](https://github.com/tianocore/edk2) is git-cloned-checked-out to:
    - %USERPROFILE%\.cache\pug\edk2 (Windows)
    - $HOME/.cache/pug/edk2 (Linux)
2. On Windows, the default MSVC tool chain tag is "vs2012x86". The following command should be run first in the command console:
    - "C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\vcvarsall.bat" x86
3. **UEFI-Utilities-2019.pug**, as the current working directory, is assigned as the "WORKSPACE" directory. **PACKAGES_PATH a.k.a. MULTIPLE-WORKSPACE** is used here to implicitly reference other standard packages outside the current working directory tree.


## Have Fun!
