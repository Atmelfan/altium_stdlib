PYTHON3=python3
ALTIUM_TOOL=bin/library.py

ROOT_DIRECTORY=.

SOURCES := ${sort ${wildcard ${ROOT_DIRECTORY}/*/*.LibPkg}}
OBJECTS = $(SOURCES:.LibPkg=.csv)

.PHONY: all
all: Wiki/Overview.md

.PHONY: clean
clean:
	rm $(OBJECTS) Overview.md

Wiki/Overview.md: $(OBJECTS)
	mkdir Wiki
	$(PYTHON3) ./make_wiki.py $(OBJECTS) -o Wiki/Overview.md

%.csv: %.LibPkg
	$(PYTHON3) $(ALTIUM_TOOL) $< --output $@