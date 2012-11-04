GENERATED = *.o *.tab.hpp *.tab.cpp exprtest *.hh scanner.cpp

all: exprtest
exprtest: exprtest.o driver.o parser.tab.o scanner.o
	$(LINK.cpp) $^ $(LOADLIBES) $(LDLIBS) -o $@

exprtest.o: exprtest.cpp driver.hpp expression.hpp
driver.o: driver.cpp driver.hpp scanner.hpp parser.tab.hpp
parser.tab.o: parser.tab.cpp expression.hpp parser.tab.hpp driver.hpp scanner.hpp
scanner.o: scanner.cpp parser.tab.hpp scanner.hpp

parser.tab.hpp: parser.tab.cpp

%.tab.cpp: %.ypp
	bison $^

%.cpp: %.ll
	flex -t $^ > $@

clean:
	rm -rf $(GENERATED)

.PHONY: all clean