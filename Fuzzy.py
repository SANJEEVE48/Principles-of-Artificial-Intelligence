import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define fuzzy variables
x = ctrl.Antecedent(np.arange(0, 11, 1), 'x')
y = ctrl.Antecedent(np.arange(0, 11, 1), 'y')
z = ctrl.Consequent(np.arange(0, 11, 1), 'z')

# Auto-membership function population
x.automf(3)
y.automf(3)
z.automf(3)

# Define fuzzy rules
rule1 = ctrl.Rule(x['poor'] & y['poor'], z['poor'])
rule2 = ctrl.Rule(x['average'] & y['average'], z['average'])
rule3 = ctrl.Rule(x['good'] & y['good'], z['good'])

# Control system
z_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
z_sim = ctrl.ControlSystemSimulation(z_ctrl)

# Input values
z_sim.input['x'] = 7
z_sim.input['y'] = 5

# Compute output
z_sim.compute()

# Print result
print(f'Output z: {z_sim.output["z"]}')
z.view(sim=z_sim)
