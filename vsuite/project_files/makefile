pandoc_configs=--filter pandoc-citeproc

%.pdf : %.md
	pandoc $(pandoc_configs) -o $@ $<

%.docx : %.md
	pandoc $(pandoc_configs) -o $@ $<

%.odt : %.md
	pandoc $(pandoc_configs) -o $@ $<
