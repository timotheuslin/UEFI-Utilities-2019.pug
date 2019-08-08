# Makefile of the front-end for building Finnbarr P. Murphy's UEFI-Utilities-2019

# (c) 2019 Timothy Lin <timothy.gh.lin@gmail.com>, BSD 3-Clause License.

PYTHON_COMMAND  =   python
PACKAGE_DSC		= 	MyApps/MyApps.dsc
PUG_CMD			=	$(PYTHON_COMMAND) pug.py -p $(PACKAGE_DSC)

all: python_v
	$(PUG_CMD)

clean: python_v
	$(PUG_CMD) clean

cleanall: python_v
	$(PUG_CMD) cleanall

python_v:
	$(PYTHON_COMMAND) --version
