include ${ACT_PATH}/aer/standard_defs.mk

TESTS := $(sort $(shell find * -name '*.act'))
PRS_OBJS := $(TESTS:%.act=prs/%.prs)
SIM_OBJS := $(TESTS:%.act=sim/%.sim)

all: prs test

test: $(SIM_OBJS)

# unit_eMx1of4_to_eMx1of2 has a deterministic test
# sim/unit_eMx1of4_to_eMx1of2.sim: prs/unit_eMx1of4_to_eMx1of2.prs unit_eMx1of4_to_eMx1of2.rc
# 	@mkdir -p sim
# 	@printf '%-30s' $(subst .prs,,$(<F))
# 	@cat $(word 2,$^) | prsim $< > $@
# 	@grep -e ERROR -e WARNING $@ > $(subst .sim,.err,$@) && echo -e "${redfont}FAIL${resetterm}" && touch $< || (grep -q "Out of values for unit_eMx1of4_to_eMx1of2.in." $@) && echo -e "${greenfont}PASS${resetterm}" || (echo -e "${redfont}DEADLOCK${resetterm}" && touch $<)

sim/%.sim: prs/%.prs %.rc
	@mkdir -p sim
	@printf '%-30s' $(subst .prs,,$(<F))
	@cat $(word 2,$^) | prsim $< > $@
	@grep -e ERROR -e WARNING $@ > $(subst .sim,.err,$@) && (echo -e "${redfont}FAIL${resetterm}") || \
	(grep -q -E "$(shell grep advance $(word 2,$^) | cut -b 9)[0-9]{$(shell expr $(shell grep advance $(word 2,$^) | cut -d \  -f 2 | wc -c) - 2)} " $@ && echo -e "${greenfont}PASS${resetterm}" || (echo -e "${redfont}DEADLOCK${resetterm}"))

prs: $(PRS_OBJS)

prs/%.prs: %.act
	@mkdir -p prs
	@printf 'compiling %s...\n' $(subst .act,,$(<F))
	@cflat -DLAYOUT=false $< > $@ || rm -f $@	

clean:
	@rm -rf prs
	@rm -rf sim
