.PHONY: default all clean

TILE_SUBDIRS := $(shell find * -mindepth 0 -maxdepth 0 -type d -name 'tile_*')
TILE_MAKE_FILES := $(TILE_SUBDIRS:%=%/Makefile)
AER_SUBDIRS := $(shell find * -mindepth 0 -maxdepth 0 -type d -name 'aer_to_tile_*')
AER_MAKE_FILES := $(AER_SUBDIRS:%=%/Makefile)
SUBDIRS := $(TILE_SUBDIRS) $(AER_SUBDIRS)

default: tile_make_files aer_make_files all
	echo $(SUBDIRS)

tile_make_files: $(TILE_MAKE_FILES)
aer_make_files: $(AER_MAKE_FILES)

tile_%/Makefile: Makefile_tile_ref
	@cp $< $@

aer_to_tile_M%/Makefile: Makefile_aer_to_tile_ref
	@cp $< $@

$(SUBDIRS)::
	$(MAKE) -C $@ $(MAKECMDGOALS)

all clean : $(SUBDIRS)
