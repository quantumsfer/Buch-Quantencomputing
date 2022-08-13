import qiskit 
		
#Erstelle einen Quantenregister mit einem Qubit 
qreg = qiskit.QuantumRegister(1, name='qreg')
		
#Erstelle ein klassisches Register mit einem Qubit 
creg = qiskit.ClassicalRegister(1, name='creg')
		
#Erstelle eine Quantenschaltung mit den oben definierten Registern
circ  = qiskit.QuantumCircuit(qreg, creg)
		
#Hinzufuegen einer NOT-Ops. fuer das Qubit
circ.x(qreg[0])
		
#Messung
circ.measure(qreg, creg)
		
#Schaltungen anzeigen
print(circ.draw())
		
#Backend Simulator definieren fuer die Ausfuehrung
backend = qiskit.BasicAer.get_backend("qasm_simulator")
		
#Schaltung im Backend 10 mal ausfuehren und Messergebnisse erhalten
job = qiskit.execute(circ, backend, shots=10)
result = job.result()
		
#Ergenisse anzeigen
print(result.get_counts()) 
		
circ.draw(filename="qiskit_circuit", output="latex")