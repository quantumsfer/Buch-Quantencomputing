import pyquil
		
#Erstelle ein Quantenprogramm
prog = pyquil.Program()
		
#Deklariere ein klassisches Register
creg = prog.declare("ro", memory_type="BIT", memory_size=1)
		
#Hinzufuegen einer NOT-Ops. und Messung an einem Qubit
prog += [
	pyquil.gates.X(0),
	pyquil.gates.MEASURE(0, creg[0])
	]
		
#Programm anzeigen
print("Programm:")
print(prog)
		
#Ein Quantencomputer laufen lassen
computer = pyquil.get_qc("1q-qvm")
		
#Programm mehrere Male simulieren
prog.wrap_in_numshots_loop(10)
		
result = computer.run(prog)
		
#Ergebnisse anzeigen 		
print(result)