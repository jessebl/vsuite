pandoc_configs=--filter pandoc-citeproc

source_docs := $(wildcard *.md)

rendered_docs = \
		 $(wildcard $(source_docs:.md=.pdf)) \
		 $(wildcard $(source_docs:.md=.odt)) \
		 $(wildcard $(source_docs:.md=.docx))

# Define filetypes longhand (instead of using export_formats) for per-filetype
# flexibility
%.pdf : %.md
	pandoc $(pandoc_configs) -o $@ $<

%.docx : %.md
	pandoc $(pandoc_configs) -o $@ $<

%.odt : %.md
	pandoc $(pandoc_configs) -o $@ $<

.PHONY: clean

# Slightly more convoluted clean command for somewhat less-intimidating output
# for less Unix-savvy users
## Test to see if there are any rendered docs and then remove them
ifneq ($(strip $(rendered_docs)),)
clean_cmd = @echo $(rendered_docs); rm -f $(rendered_docs)
## If not, show nothing to user
else
clean_cmd = @true
endif

clean : $(rendered_docs)
	$(clean_cmd)
