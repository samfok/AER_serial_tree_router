COSIM := cosim.pl
SPICE_ACT := $(sort $(shell find * -name '*.act'))
SPICE_DIR := $(SPICE_ACT:%spice.act=%)

all : spice

spice : $(SPICE_DIR:%=%hsim.fsdb) 

%hsim.fsdb : %cosim.xml %spice.act 
	@cd $(subst hsim.fsdb,,$@) && $(COSIM) -C cosim.xml -P $(ACT_HOME) \
		| tee cosim_log.txt
	@cd $(subst hsim.fsdb,,$@) && \
		csh -c 'tlint -C /ufs/cad/lib/lint/st28soi.conf hsim' > tlint.txt

.PHONY : touch

touch :
	@touch $(SPICE_ACT)
