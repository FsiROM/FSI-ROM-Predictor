import KratosMultiphysics as KM
from KratosMultiphysics.CoSimulationApplication.co_simulation_analysis import CoSimulationAnalysis
from rom_am.fluid_surrogate import FluidSurrog
from rom_am.fluid_hybrid_surrogate import HybridFluidSurrog

#from replicatingFluidSurrogate import FluidSurrog
#from replicatingFluidSurrogate import NewFluidSurrogNewer

from KratosMultiphysics.CoSimulationApplication.convergence_accelerators.myNewSurrogatesNewer import NewFluidSurrogNewer

parameter_file_name = "./fsi_ROM_parameters.json"
with open(parameter_file_name,'r') as parameter_file:
    parameters = KM.Parameters(parameter_file.read())

simulation = CoSimulationAnalysis(parameters)
simulation.Run()
