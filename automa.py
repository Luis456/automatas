a=str(raw_input('Palabras:' ))
cadena = a
c=len(a)
a = ''
b = ''
for h in cadena:
    a = a + h
    print "PREFIJOS: " + str (a)
for h in cadena:
    b = h + b
    print "SUFIJOS: " +str(b)
print "CANTIDAD: "+str(c)
raw_input()