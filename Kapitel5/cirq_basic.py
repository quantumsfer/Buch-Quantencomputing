import cirq 
		
#Erstelle eine Quantenschaltung 
circuit = cirq.Cirquit(
cirq.X(qubit)**0.5, #NOT
cirq.measure(qubit, key='m') #Messung
		
#Quantenschaltung anzeigen
print("Circuit:")
print(circuit)
		
#Simulator erstellen
simulator = cirq.Simulator()
		
#Simuliere die Quantenschaltung mehrmals
result = simulator.run(circuit, repetitions=15)
		
#Ergebnisse anzeigen
print("Results:")
print(result)