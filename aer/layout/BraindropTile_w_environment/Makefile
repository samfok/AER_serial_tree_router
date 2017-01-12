NETGEN := netgen -l -p'TOP<>' -B
ACT_PATH := $(subst alex_,,$(ACT_PATH))
ROULETTE_PATH := samfok@roulette.stanford.edu:~/netlist/

ACT_FILE := $(shell find * -name 'BraindropTile*.act')
SPI_TGT := $(ACT_FILE:%act=%spi)
NETGEN_CONF := netgen.conf

all: $(SPI_TGT)

$(NETGEN_CONF):
	@cp ${ACT_HOME}/scripts/sim/netgen_for_celltk.conf $(NETGEN_CONF)
	@sed -i "s/FOLDP/27/g" $(NETGEN_CONF)
	@sed -i "s/FOLDN/18/g" $(NETGEN_CONF)

%.spi: %.act ${ACT_PATH}/aer/aer/aer.act ${ACT_PATH}/aer/aext/aext.act ${ACT_PATH}/aer/aerv/aerv.act ${ACT_PATH}/aer/interface/interface.act ${NETGEN_CONF}
	$(NETGEN) -o$@ -C$(NETGEN_CONF) $< || (rm $@; exit 1)
	sed -i 's/^M/xM/' $@
	sed -i '1s/^/*defines a testbench for the BraindropTile\n\n/' $@
	sed -i 's/aer_brain_aer_TILE_NRN_MEM/BraindropTileNeuronsMemory/' $@
	scp $@ $(ROULETTE_PATH)

clean:
	@rm $(SPI_TGT)

.PHONY: clean
