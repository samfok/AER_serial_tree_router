include ${ACT_PATH}/aer/standard_defs.mk

CFLAT := cflat -DLAYOUT=false -DPRSIM=true
PRSIM := prsim

TESTS := $(sort $(shell find * -name '*.act'))
PRS_OBJS := $(TESTS:%.act=prs/%.prs)
SIM_OBJS := $(TESTS:%.act=sim/%.sim)
RES_OBJS := $(TESTS:%.act=results/%.png)

all: benchmark

benchmark: $(RES_OBJS) $(SIM_OBJS) $(PRS_OBJS)

results/%.png: %.py sim/%.sim
	@mkdir -p results
	@python $<

sim/%.sim: prs/%.prs %.rc
	@mkdir -p sim
	@printf '%-30s' $(subst .prs,,$(<F))
	@cat $(word 2,$^) | ($(PRSIM) $< > $@)

prs/%.prs: %.act ${ACT_PATH}/aer/serial/serial.act
	@mkdir -p prs
	@printf 'compiling %s...\n' $(subst .act,,$(<F))
	@$(CFLAT) $< > $@ || (rm -f $@; exit 1)

clean:
	@rm -rf prs
	@rm -rf sim
	@rm -rf results
