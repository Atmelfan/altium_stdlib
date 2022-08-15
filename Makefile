PYTHON3=python3
ALTIUM_TOOL=bin/library.py
BRANCH=master


ROOT_DIRECTORY=.

SOURCES := ${sort ${wildcard ${ROOT_DIRECTORY}/*/*.LibPkg}}
OBJECTS = $(SOURCES:.LibPkg=.csv)

.PHONY: all
all: Wiki/Overview.md

.PHONY: clean
clean:
	rm -rf $(OBJECTS) Wiki

Wiki/Overview.md: $(OBJECTS)
	mkdir Wiki
	$(PYTHON3) ./make_wiki.py $(OBJECTS) --branch $(BRANCH) -o Wiki/Overview.md

%.csv: %.LibPkg
	$(PYTHON3) $(ALTIUM_TOOL) $< --output $@