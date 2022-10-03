""" Assignment #2 (Set 30, 2021)

--- Goal
Write a program to explore the properties of a few elementary Particles.
The program must contain a Base class Particle and two Child classes, Proton and Alpha, that inherit from it.

--- Specifications
- instances of the class Particle must be initialized with their mass, charge, and name
- the class constructor must also accept (optionally) and store one and only one of the following quantities: energy, momentum, beta or gamma
- whatever the choice, the user should be able to read and set any of the
  above mentioned quantites using just the '.' (dot) operator e.g.
  print(my_particle.energy), my_particle.beta = 0.5
- attempts to set non physical values should be rejected
- the Particle class must have a method to print the Particle information in
  a formatted way
- the child classes Alpha and Protons must use class attributes to store their mass, charge and name """

import math

s_o_l = 1 #setting the speed of light to 1


class Particle:
    """Class describing a few elementary particles"""

    def __init__(self, name, mass,
                charge, momentum = 0):
        """Costructor from particle's properties. Arguments:
        - name of the particle (Proton or Alpha)
        - mass (in Mev/c^2),
        - charge (in terms of electron charge, e)"""
        self._name = name
        self._mass = mass
        self._charge = charge
        self.momentum = momentum

    def part_print(self):
         """Printing function show the property of the particle"""
         print(f"Particle: {self.name}, mass = {self.mass} MeV/c^2 "
               f"charge = {self.charge} e, momentum = {self.momentum} MeV/c")


    @property
    def mass(self):
        return self._mass

    @property
    def name(self):
        return self._name

    @property
    def charge(self):
        return self._charge

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, new_value):
        if (new_value <0):
            print('Momentum must be set to a positive value.')
            self._momentum = 0
        else:
            self._momentum = new_value

    @property
    def energy(self):
        return math.sqrt((self.momentum)**2 + (self.mass*s_o_l**2)**2)

    @energy.setter
    def energy(self, new_value):
        if (new_value < self.mass):
            print('Energy must be greater equal than mass')
            return
        self.momentum = math.sqrt(new_value**2 + (self.mass*s_o_l**2)**2)\
                        /s_o_l**2

    @property
    def beta(self):
        return self.momentum/self.energy*s_o_l

    @beta.setter
    def beta(self, new_value):
        if (new_value < 0.) or (new_value > 1.):
            print('Beta values must be positive and <1')
            return
        if (new_value > 1 ) and (self.mass > 0):
            print("Massive particles can't exced the speed of light, +\
                   while just photons may travel at c.")
        self.momentum = s_o_l * new_value * \
                    self.mass / math.sqrt(1 - new_value**2)


class Proton(Particle):
      """Class describing a Proton."""
      name = 'Proton'
      mass = 938.2
      charge = +1

      def __init__(self, momentum = 0):
          Particle.__init__(self, self.name, self.mass, self.charge, momentum)


class Alpha(Particle):
      """Class describing an Alpha particle."""
      name = 'Alpha'
      mass = 3727.3
      charge = +2

      def __init__(self, momentum = 0):
          Particle.__init__(self, self.name, self.mass, self.charge, momentum)


if __name__ == '__main__':
    alpha = Alpha(100.)
    alpha.part_print()
    alpha.beta = 0.5
    alpha.part_print()
    alpha.energy = 300.
    proton = Proton(150)
    proton.part_print()
