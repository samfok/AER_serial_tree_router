.PHONY: all clean

CONVERT := convert -resize 1080 -density 300 -background white -alpha remove
CONVERT_ANI_OPTS := -delay 60 -loop 0


PDFS := $(shell find -name '*pdf')
# PNGS := $(PDFS:%.pdf=%.png)

all: serial_protocol_req_res.gif serial_protocol_demo.gif

serial_protocol_req_res.gif: $(PDFS)
	$(CONVERT) $(CONVERT_ANI_OPTS) \
	serial_protocol_petri_net_init.pdf \
	serial_protocol_petri_net_req*pdf \
	serial_protocol_petri_net_ready.pdf \
	serial_protocol_petri_net_res*pdf \
	serial_protocol_req_res.gif

serial_protocol_demo.gif: $(PDFS)
	$(CONVERT) $(CONVERT_ANI_OPTS) \
	serial_protocol_petri_net_init.pdf \
	serial_protocol_petri_net_req*pdf \
	serial_protocol_petri_net_ready.pdf \
	serial_protocol_petri_net_data0*pdf \
	serial_protocol_petri_net_ready.pdf \
	serial_protocol_petri_net_data1*pdf \
	serial_protocol_petri_net_ready.pdf \
	serial_protocol_petri_net_res*pdf \
	serial_protocol_demo.gif

# make pngs from pdfs
# %.png: %.pdf
# 	@convert -resize 1080 -density 300 -background white -alpha remove $< $@

clean :
	@rm -f *png *gif
