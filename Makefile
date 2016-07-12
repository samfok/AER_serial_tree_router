.PHONY: default all clean

# get parent directory
PARENT_DIR := $(lastword $(subst /, ,$(shell dirname `pwd`)))

# check if we're embedded in the brainstorm repo or not
ifeq ($(PARENT_DIR), act)
	SUBDIRS=$(shell find * -mindepth 1 -type d -name test*)
else
	SUBDIRS=$(shell find * -mindepth 1 -type d -name test)
endif

default: all

$(SUBDIRS)::
	$(MAKE) -C $@ $(MAKECMDGOALS)

all clean : $(SUBDIRS)
