"""
This subpackage contains

* :class:`domain` a container object for a data specific to a particular
  mesh(es), grid(s)
* :mod:`~polyadcirc.run_framework.random_manningsn` a class and associated set of
  methods to run a set of ADCIRC simulations with varying parameters
* :mod:`~polyadcirc.run_framework.plotADCIRC` a set of functions for plotting
  simulation outputs

"""

__all__ = ['random_manningsn', 'domain', 'subdomain',
    'fulldomain', 'random_wall', 'random_wall_Q']