from G2_M_v2 import *
from pysb import *
from pysb.util import *
from pysb.macros import *
from pysb.bng import *
from pysb.integrate import odesolve
import pylab as pl
from numpy import linspace
from sympy import sympify

# ***Generate ODEs and Plot***

# import os 
# print os.getcwd()
# quit()

declare_monomers()
declare_parameters()
declare_initial_conditions()
declare_observables()
declare_functions()
declare_rules()
     
generate_equations(model, verbose=True)
  
# for monomers in model.monomers:
#     print monomers
# print
#   
# for parameters in model.parameters:
#     print parameters
# print
#  
# for initial_conditions in model.initial_conditions:
#     print initial_conditions
# print
#  
# for obs in model.observables:
#     print obs, ":", obs.species, ",", obs.coefficients
#     obs_string = ''
#     for i in range(len(obs.coefficients)):
#         if i > 0: obs_string += " + "
#         obs_string += "__s"+str(obs.species[i])
#         if obs.coefficients[i] > 1:
#              obs_string += "*"+str(obs.coefficients[i])
#     print obs_string
#   
# for rules in model.rules:
#     print rules
# print
#  
# for i in range(len(model.species)):
#     print str(i)+":", model.species[i]
# print
#  
# for i in range(len(model.odes)):
#     print str(i)+":", model.odes[i]
# print
# 
# for x in model.parameters_initial_conditions():
#     print x, ":", x.value
# print 
# 
# for x in model.parameters_unused():
#     print x, ":", x.value
# print 
# 
# for x in model.parameters_rules():
#     print x
#    
# quit()
#  
# from pysb.generator.bng import BngGenerator
# print BngGenerator(model).get_content()

t = linspace(0,4000,4000) 
 
## ** Set No DNA Damage **
set_dna_damage(0.0)
y = odesolve(model,t,verbose=True)
 
pl.figure()
for obs in ["OBS_MPF", "OBS_p53", "OBS_Wee1"]:
    pl.plot(t, y[obs], label=obs)
pl.legend(loc='upper right')
pl.xlabel("Time (arbitrary units)")
pl.ylabel("Protein Level")
pl.title("Protein Dynamics (No DNA Damage)")
pl.savefig("G2-M Cell Cycle No DNA Damage1.png", format= "png")

pl.figure()
pl.plot(t, y["OBS_aCdc25"], label="OBS_aCdc25")
pl.legend(loc='upper left')
pl.xlabel("Time (arbitrary units)")
pl.ylabel("Protein Level (Active Cdc25)")
pl.title("Protein Dynamics (No DNA Damage)")
pl.savefig("G2-M Cell Cycle No DNA Damage2.png", format= "png")

## ** Set DNA Damage **
set_dna_damage(0.005)
y = odesolve(model,t,verbose=True)
 
pl.figure()
for obs in ["OBS_MPF", "OBS_p53", "OBS_Wee1"]:
    pl.plot(t, y[obs], label=obs)
pl.legend(loc='upper right')
pl.xlabel("Time (arbitrary units)")
pl.ylabel("Protein Level")
pl.title("Protein Dynamics (DNA Damage = 0.005)")
pl.savefig("G2-M Cell Cycle DNA Damage1.png", format= "png")
 
pl.figure()
pl.plot(t, y["OBS_aCdc25"], label="OBS_aCdc25")
pl.legend(loc='upper left')
pl.xlabel("Time (arbitrary units)")
pl.ylabel("Protein Level (Active Cdc25)")
pl.title("Protein Dynamics (DNA Damage = 0.005)")
pl.savefig("G2-M Cell Cycle DNA Damage2.png", format= "png")

pl.show()