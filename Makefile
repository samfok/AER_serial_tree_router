.PHONY: default all clean

SUBDIRS=$(shell find * -mindepth 1 -type d -name test)

default: all

$(SUBDIRS)::
	$(MAKE) -C $@ $(MAKECMDGOALS)

all clean : $(SUBDIRS)
