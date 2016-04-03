COSIM := ~/bin/cosim_vpsub_vnsub.pl
SPICE_ACT := $(sort $(shell find * -name '*.act'))
SPICE_HSIM := $(SPICE_ACT:%spice.act=%hsim.fsdb)

all : hsim

hsim : $(SPICE_HSIM)

# run cosim flow to generate spi files
%hsim.fsdb : %spice.act.spi
	@cd $(subst hsim.fsdb,,$@) && ./simv +nsda+cosim.cfg

%spice.act.spi : %spice.act %cosim.xml
	@cd $(subst spice.act.spi,,$@) && $(COSIM) -C cosim.xml -P $(ACT_HOME) \
		| tee cosim_log.txt
	@./thick_oxide.csh $@
