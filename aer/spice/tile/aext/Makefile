include ${ACT_PATH}/standard_defs.mk

TESTS := $(sort $(shell find * -maxdepth 1 -name '*.act'))

LAYOUT_OBJS := $(TESTS:%.act=layout/%)
SPICE_OBJS := $(TESTS:%.act=spice/%)
TLINT_OBJS := $(TESTS:%.act=spice/%/tlint.txt) $(TESTS:%.act=spice/%/parse_tlint.txt)

TECH := /ufs/cad/lib/netgen/st28soi.conf

all: spice tlint

layout: $(LAYOUT_OBJS)
spice: $(SPICE_OBJS)
tlint: $(TLINT_OBJS)

# Make can fail to find these rules (and give unhelpful errors) if the xml or act
# is mis-named, so if it's not working double-check
layout/%: celltk_conf_%.xml %.act
	@mkdir -p layout
	@mkdir -p $@
	@test -e $@/.gitignore || echo "*" > $@/.gitignore
	@celltk -w$@ -c$<

# uses cosim.pl
spice/%: cosim_conf_%.xml %.act
	@printf '%-30s' $@
	@mkdir -p spice
	@mkdir -p $@
	@test -e $@/.gitignore || echo "*" > $@/.gitignore
	@cp $(subst spice/,,$@).act $@
	@test -e $(subst spice/,,$@)_inject.py && python $(subst spice/,,$@)_inject.py && cp *.inject $@ || echo "foo" > /dev/null
	@cp $< $@
	@cd $@; ~/bin/cosim_vpsub_vnsub.pl -C $< 2> cosim_stderr.txt > cosim_log.txt && echo ${greenfont}PASS${resetterm} || echo ${redfont}FAIL${resetterm}

spice/%/tlint.txt: spice/%/hsim.xprs
	@printf '%-30s' $@
	@cd $(@:%/tlint.txt=%); cflat -DLAYOUT=false -DPRSIM=true $(@:spice/%/tlint.txt=%).act > $(@:spice/%/tlint.txt=%).prs
	@cd $(@:%/tlint.txt=%); cat $(@:spice/%/tlint.txt=%).prs hsim.xprs > hsim.prs
	@cd $(@:%/tlint.txt=%); csh -c 'run_tlint.csh'

# I think backticks in Makefile is sketchy, but this was a pain in the ass so I'm leaving it
# for some reason $(shell cat $@) thinks the file doesn't exist
spice/%/parse_tlint.txt: spice/%/tlint.txt
	@parse_tlint.py $^ $@
	@$(eval MSG := `cat $@`)
	@grep -e PASS $@ > foo.txt && echo ${greenfont}${MSG}${resetterm} || echo ${redfont}${MSG}${resetterm}

clean: cleanlayout cleanspice

cleanlayout:
	@rm -rf layout

cleanspice:
	@rm -rf spice

