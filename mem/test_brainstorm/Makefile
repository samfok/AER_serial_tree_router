include ${ACT_PATH}/aer/standard_defs.mk

CFLAT := cflat -DLAYOUT=false -DPRSIM=true
PRSIM := prsim

AER_PATH := ${ACT_PATH}/aer
MEM_PATH := ${AER_PATH}/mem

TESTS := $(sort $(shell find * -name '*.act'))
PRS_OBJS := $(TESTS:%.act=prs/%.prs)
SIM_OBJS := $(TESTS:%.act=sim/%.sim)

all: prs test

test: $(SIM_OBJS)

sim/%.sim: prs/%.prs %.rc
	@mkdir -p sim
	@printf '%-30s' $(subst .prs,,$(<F))
	@cat $(word 2,$^) | $(PRSIM) $< > $@
	@grep -e ERROR -e WARNING $@ > $(subst .sim,.err,$@) && (echo -e "${redfont}FAIL${resetterm}") && touch $< || \
	(grep -q -E "$(shell grep advance $(word 2,$^) | cut -b 9)[0-9]{$(shell expr $(shell grep advance $(word 2,$^) | cut -d \  -f 2 | wc -c) - 2)} " $@ && echo -e "${greenfont}PASS${resetterm}" || (echo -e "${redfont}DEADLOCK${resetterm}" && touch $<))

prs: $(PRS_OBJS)

prs/%.prs: %.act ${AER_PATH}/aerv/aerv.act ${AER_PATH}/aerv/bs_aerv.act ${MEM_PATH}/memory.act
	@mkdir -p prs
	@printf 'compiling %s...\n' $(subst .act,,$(<F))
	@$(CFLAT) $< > $@ || rm -f $@	

clean:
	@rm -rf prs
	@rm -rf sim
