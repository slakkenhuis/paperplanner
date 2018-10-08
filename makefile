planner.pdf:$(sort $(patsubst %.svg,%.pdf,$(wildcard planner-*.svg)))
	pdfunite $^ $@

%.pdf: %.svg
	inkscape $< --export-dpi=1200 --export-pdf=$@

clean: 
	gvfs-trash planner-*

print: planner.pdf
	lp -o media=a4 -o number-up=2 -o number-up-layout=rl -o page-ranges=1-2 -o sides=one-sided $<

.PHONY: clean print
