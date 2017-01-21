.PHONY: default all clean

TILE_SUBDIRS := $(shell find * -mindepth 0 -maxdepth 0 -type d -name 'BraindropTile_*')
TILE_MAKE_FILES := $(TILE_SUBDIRS:%=%/Makefile)
AER_SUBDIRS := $(shell find * -mindepth 0 -maxdepth 0 -type d -name 'aer_to_tile_*')
AER_MAKE_FILES := $(AER_SUBDIRS:%=%/Makefile)
AER_RCX_SUBDIRS := $(shell find * -mindepth 0 -maxdepth 0 -type d -name 'BraindropAERArray_RCX_*')
AER_RCX_MAKE_FILES := $(AER_RCX_SUBDIRS:%=%/Makefile)

SUBDIRS := $(TILE_SUBDIRS) $(AER_SUBDIRS) $(AER_RCX_SUBDIRS)

default: tile_make_files aer_make_files aer_rcx_make_files all

tile_make_files: $(TILE_MAKE_FILES)
aer_make_files: $(AER_MAKE_FILES)
aer_rcx_make_files: $(AER_RCX_MAKE_FILES)

BraindropTile_%/Makefile: Makefile_BraindropTile_ref
	@cp $< $@

aer_to_tile_M%/Makefile: Makefile_aer_to_tile_ref
	@cp $< $@

BraindropAERArray_RCX_%/Makefile: Makefile_BraindropAERArray_RCX_ref
	@cp $< $@

$(SUBDIRS)::
	$(MAKE) -C $@ $(MAKECMDGOALS)

all clean : $(SUBDIRS)
