NETGEN := netgen -l -p'TOP<>' -B
CREATE_CDL := ./create_cdl.csh
POSTPROCESS := ./postprocess_netlist.csh
ACT_PATH := $(subst alex_,,$(ACT_PATH))
ROULETTE_PATH := samfok@roulette.stanford.edu:~/Code/layout_brainstorm/CDB/NETLIST/

ACT_FILE := $(shell find * -name 'BraindropAERArray_RCX_*.act')
SPI_TGT := $(ACT_FILE:%act=%spi)
NETGEN_CONF := netgen.conf

all: $(SPI_TGT)

$(NETGEN_CONF):
	@cp ${ACT_HOME}/scripts/sim/netgen_for_celltk.conf $(NETGEN_CONF)
	@sed -i "s/FOLDP/27/g" $(NETGEN_CONF)
	@sed -i "s/FOLDN/18/g" $(NETGEN_CONF)

%.spi: %.act ${ACT_PATH}/aer/aer/layout/BraindropAERArray_RCX_8x8/BraindropAERArray_RCX_8x8.act ${ACT_PATH}/aer/aer/aer.act ${ACT_PATH}/aer/aext/aext.act ${ACT_PATH}/aer/aerv/aerv.act ${ACT_PATH}/aer/interface/interface.act ${NETGEN_CONF} ${POSTPROCESS}
	$(NETGEN) -o$@ -C$(NETGEN_CONF) $< || (rm $@; exit 1)
	$(CREATE_CDL) $@ || (rm $@; exit 1)
	$(POSTPROCESS) $@  || (rm $@; exit 1)
	scp ${@:spi=cdl} $(ROULETTE_PATH)
	scp $@ $(ROULETTE_PATH)

clean:
	@rm $(SPI_TGT)

.PHONY: clean
