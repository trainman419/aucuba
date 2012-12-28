
Sample.class: Complete_output.class Complete_outputTextResource.class

all: Sample.class

run: Sample.class
	java Sample

Complete_output.java: aucuba.py complete_output.json
	./aucuba.py complete_output.json

%.class: %.java
	javac $<

clean:
	rm -f *.class com/asherah/*.class com/asherah/internal/*.class

.phony: all
.phony: clean
.phone: run
