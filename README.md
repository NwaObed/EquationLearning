# EquationLearning

# Abstract
During mitosis, the chromosomes undergoes a stochastic oscillations due to the Kinetochore-Microtubule (KT-MT) attachment. These oscillations are generally associated with the different forces acting on the kinetochores. Studies shows that these forces are the K-fibre forces, polar ejection forces (PEF), the spring force and some random forces. Here, we modelled the force balance at the metaphase as a stochastic differential equation (sDE). We want to learn the governing equation describing the time evolution of the probability density function of the stochastic kinetochore oscillations using simulated data. We implemented a sparse regression technique capable of discovering the governing partial differential equation (PDE) validated using Akaike Information Criterion (AIC) with PDE-FIND via AIC algorithm. The regression algorithm uses a sparsity promoting methodology to select feature terms that most probably represent the dynamics of the oscillations. The learned model with the least AIC is selected as the most probable governing equation for the kinetochore oscillations

# Pipeline
![Home](https://github.com/NwaObed/EquationLearning/blob/main/Plots/eql_pipeline.png)
