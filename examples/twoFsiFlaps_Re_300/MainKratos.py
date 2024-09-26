import KratosMultiphysics as KM
from KratosMultiphysics.CoSimulationApplication.co_simulation_analysis import CoSimulationAnalysis


parameter_file_name = "DoubleFlap_fsi_parameters_ROM.json"
with open(parameter_file_name,'r') as parameter_file:
    parameters = KM.Parameters(parameter_file.read())

simulation = CoSimulationAnalysis(parameters)
simulation.Run()
