import KratosMultiphysics as KM
from KratosMultiphysics.CoSimulationApplication.co_simulation_analysis import CoSimulationAnalysis

parameter_file_name = "ProjectParametersCoSim.json"

with open(parameter_file_name,'r') as parameter_file:
    parameters = KM.Parameters(parameter_file.read())

simulation = CoSimulationAnalysis(parameters)
simulation.Run()
