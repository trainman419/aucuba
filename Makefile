
all: Complete_output.class Complete_outputTextResource.class

Complete_output.java: aucuba.py complete_output.json
	./aucuba.py complete_output.json

%.class: %.java
	javac $<
