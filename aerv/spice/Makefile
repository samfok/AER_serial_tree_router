COSIM := ~/bin/cosim_vpsub_vnsub.pl
SPICE_ACT := $(sort $(shell find * -name '*.act'))
SPICE_HSIM := $(SPICE_ACT:%spice.act=%hsim.fsdb)

all : hsim

hsim : $(SPICE_HSIM)

# run cosim flow to generate spi files
%hsim.fsdb : %spice.act %cosim.xml $(ACT_PATH)/aer_brainstorm/aerv/aerv.act
	@cd $(subst hsim.fsdb,,$@) && $(COSIM) -C cosim.xml -P $(ACT_PATH) \
		| tee cosim_log.txt
