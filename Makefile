PYTHON3=python3
ALTIUM_TOOL=../library.py

ROOT_DIRECTORY=.

SOURCES := ${sort ${wildcard ${ROOT_DIRECTORY}/*/*.LibPkg}}
OBJECTS = $(SOURCES:.LibPkg=.csv)

.PHONY: all
all: Overview.md

.PHONY: clean
clean:
	rm $(OBJECTS) Overview.md

Overview.md: $(OBJECTS)
	$(PYTHON3) ./make_wiki.py $(OBJECTS) -o Overview.md

%.csv: %.LibPkg
	$(PYTHON3) $(ALTIUM_TOOL) $< --output $@