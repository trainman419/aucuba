
all: Complete_output.class Complete_outputTextResource.class

Complete_output.java: aucuba.py complete_output.json
	./aucuba.py complete_output.json com.sample

%.class: %.java
	javac $<

clean:
	rm -f *.class com/asherah/*.class com/asherah/internal/*.class

.phony: all
.phony: clean
