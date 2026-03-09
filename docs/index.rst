AE6310 Course Notes
===================

Welcome to AE6310: Optimization for the Design of Engineered Systems.

AE6310 is about the application of numerical optimization methods to the design of engineering systems.

Recommended references
**********************

I recommend the following reference textbooks for further information about the course material:

1. `Engineering Design Optimization <https://mdobook.github.io/>`, J.R.R.A. Martins and A. Ning

2. `Numerical Optimization <https://link.springer.com/book/10.1007/978-0-387-40065-5>`, J. Nocedal and S.J. Wright

3. `Practical Methods of Optimization <https://onlinelibrary.wiley.com/doi/book/10.1002/9781118723203>`, R. Fletcher

4. `Practical Optimization <https://epubs.siam.org/doi/book/10.1137/1.9781611975604>`, M.H. Wright, P.E. Gill, and W. Murray

5. `Trust Region Methods <https://epubs.siam.org/doi/10.1137/1.9780898719857>`, A.R. Conn, N.I.M. Gould, and P.L. Toint

6. `Convex Optimization <https://stanford.edu/~boyd/cvxbook/>`, S. Boyd and L. Vandenberghe

7. Numerical Optimization Techniques for Engineering Design, G.N. Vanderplaats

8. Multidisciplinary Design Optimization supported by Knowledge Based Engineering, Sobieski, Moris, and van Tooren

Engineering Design using Optimization
*************************************

In this course, we will look at how to apply optimization methods to engineering problems.
Below are two examples of complex design problems that are solved using numerical optimization methods.

Aeroelastic example
-------------------

Aircraft wings are flexible and deform under aerodynamic load, twisting and bending relative to their undeformed shape.
The aerodynamic loads, in turn, depend on the deformed shape of the wing.
As a result, there is a tight coupling between aerodynamics and structures.
To find the equilibrium shape of the wing, we have to couple aerodynamic and structural disciplines together into a single analysis.

Aerostructural optimization consists of finding the wing planform, shape and structural sizing variables that optimize the performance of the aircraft.
The following is a simple aerostructural optimization from the open source tool `OpenAeroStruct <https://github.com/mdolab/OpenAeroStruct>`_.

.. image:: _images/OpenAeroStruct_example.png
   :width: 600

A key consideration in multidisciplinary design problems is connecting the different disciplines together for analysis and design.
The extended design structure matrix (XDSM) diagram is a convenient way to visualize how the different analysis components interact together.
The following XDSM diagram is from the above aerostructural optimization problem.

.. image:: _images/aerostruct_xdsm.png
   :width: 600


Structural topology optimization example
----------------------------------------

In structural design you often do not know in advance the best structural shape or topology to meet design requirements.
Topology optimization methods are designed to generate an optimized structure, free from restrictions on the shape or topology.

.. image:: _images/beam_levelset_r0_025.png
   :width: 600

This image illustrates the results of a topology optimization case where the the objective is to minimize the mass of the structure subject to a constraint on the approximate maximum stress.
Topology optimization problems may involve millions of design variables and require the solution of a challenging finite-element simulation.
This course does not cover topology optimziation specifically, however this type of application can be tackled with the knowledge and theory developed in this course.

Table of Contents
*****************

.. toctree::
   :maxdepth: 2

   intro_to_python.rst
   jupyter/Introduction.ipynb
   jupyter/Unconstrained_Optimization_Theory.ipynb
   jupyter/Minimization_of_Quadratic_Functions.ipynb
   jupyter/Fundamentals_Unconstrained_Opt_Algorithms.ipynb
   jupyter/Line_Search_Methods.ipynb
   jupyter/Line_Search_Algorithms.ipynb
   jupyter/Trust_Region_Methods.ipynb
   jupyter/Constrained_Optimization_Theory.ipynb
   jupyter/Constrained_Optimization_Algorithms.ipynb
   jupyter/Introduction_to_Simulation-based_Optimization.ipynb
   jupyter/Trajectory_Optimization_Case_Study.ipynb
   jupyter/PDE_Constrained_Optimization.ipynb
   jupyter/Multidisciplinary_Optimization.ipynb
   jupyter/Surrogate_Modeling.ipynb
   jupyter/Derivative_Free_Optimization.ipynb
   jupyter/2026_project/race_car_problem.ipynb
   jupyter/2025_project/Class_Project_Description.ipynb


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
