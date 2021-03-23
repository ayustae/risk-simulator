# risk-simulator
Battle simulator for Risk Europe

## Files
* **risk_simulator_gui.py:** This is the launcher.
* **RiskSimGui.py:** This is the class for a Tk GUI used to build the interface.
* **RiskArmy:** This is a class representing a Risk Europe army.
* **simulation.py:** This is a collection of functions used to simulate the battles.

## To Do
* Properly handle exceptions when a non-integer is provided.
* Handle corner case when there is a tie in the combat (i.e. artillery killing eachother before proceding to further rounds).
* Properly handle the error when no value is given at all in some field (should default to 0).
