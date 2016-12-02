.PHONY: default all clean

SUBDIRS := $(shell find * -mindepth 0 -maxdepth 0 -type d -name 'tile_*')
TILE_MAKE_FILES := $(SUBDIRS:%=%/Makefile)

default: tile_make_files all

tile_make_files: $(TILE_MAKE_FILES)

%/Makefile: Makefile_tile_ref
	@cp $< $@

$(SUBDIRS)::
	$(MAKE) -C $@ $(MAKECMDGOALS)

all clean : $(SUBDIRS)
