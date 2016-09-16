include ${ACT_PATH}/aer/standard_defs.mk

CFLAT := cflat -DLAYOUT=false -DPRSIM=true
PRSIM := prsim
PYTHON := python

ACT_REF_FILES := $(sort $(shell find * -name '*.act.ref'))
GEN_ACT_OBJS := $(ACT_REF_FILES:%.ref=gen_%)

ACT_FILES := $(sort $(shell find * -name '*.act')) $(GEN_ACT_OBJS)
PRS_OBJS := $(ACT_FILES:%.act=prs/%.prs)
SIM_OBJS := $(ACT_FILES:%.act=sim/%.sim)

all: prs test

test: $(SIM_OBJS)

sim/%.sim: prs/%.prs %.rc
	@mkdir -p sim
	@printf '%-30s' $(subst .prs,,$(<F))
	@cat $(word 2,$^) | ($(PRSIM) $< > $@ && \
	((grep -e ERROR -e WARNING $@ > $(subst .sim,.err,$@) && (echo -e "${redfont}FAIL${resetterm}") && touch $<) || \
	(grep -q -E "$(shell grep advance $(word 2,$^) | cut -b 9)[0-9]{$(shell expr $(shell grep advance $(word 2,$^) | cut -d \  -f 2 | wc -c) - 2)} " $@ && echo -e "${greenfont}PASS${resetterm}" || (echo -e "${redfont}DEADLOCK${resetterm}" && touch $<))) || \
	(echo -e "${redfont}FAIL${resetterm}"; touch $<))

prs: $(PRS_OBJS)

prs/%.prs: %.act ${ACT_PATH}/aer/aer/bs_aer.act ${ACT_PATH}/aer/aer/aer.act ${ACT_PATH}/aer/aer/ref_aer.act ${ACT_PATH}/aer/aerv/aerv.act ${ACT_PATH}/aer/aerv/ref_aerv.act ${ACT_PATH}/aer/aext/aext.act ${ACT_PATH}/aer/aext/ref_aext.act  ${ACT_PATH}/aer/interface/interface.act ${ACT_PATH}/aer/interface/ref_interface.act ${ACT_PATH}/aer/mem/memory.act
	@mkdir -p prs
	@printf 'compiling %s...\n' $(subst .act,,$(<F))
	@$(CFLAT) $< > $@ || (rm -f $@; exit 1)

$(GEN_ACT_OBJS): gen_%: %.ref
	@printf 'generating act for %s...\n' $(subst .act.ref,,$(<F))
	@$(PYTHON) ${ACT_PATH}/aer/aer/index_tile_ij.py $< > $@

clean:
	@rm -rf $(GEN_ACT_OBJS)
	@rm -rf prs
	@rm -rf sim
