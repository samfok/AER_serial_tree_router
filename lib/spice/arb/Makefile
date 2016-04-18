COSIM := ~/bin/cosim_vpsub_vnsub.pl
SPICE_ACT := $(sort $(shell find * -name '*.act'))
SPICE_DIR := $(SPICE_ACT:%spice.act=%)

all : spice

spice : $(SPICE_DIR:%=%hsim.fsdb) 

%hsim.fsdb : %cosim.xml %spice.act $(ACT_PATH)/aer/lib/arbiter.act
	@cd $(subst hsim.fsdb,,$@) && $(COSIM) -C cosim.xml -P $(ACT_PATH) \
		| tee cosim_log.txt
