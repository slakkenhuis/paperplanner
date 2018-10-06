planner.pdf:$(sort $(patsubst %.svg,%.pdf,$(wildcard planner-*.svg)))
	pdfunite $^ $@

%.pdf: %.svg
	inkscape $< --export-dpi=1200 --export-pdf=$@

clean: 
	gvfs-trash planner-*

.PHONY: clean
