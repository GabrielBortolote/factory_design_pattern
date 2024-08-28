from abc import ABC, abstractmethod
from package import Package

class Transport(ABC):
  @abstractmethod
  def deliver(self, package: Package):
    pass

class Ship(Transport):
  def deliver(self, package: Package):
    message = f'The package "{package.name}" is being delivered by SHIP'
    print(message)

class Truck(Transport):
  def deliver(self, package: Package):
    message = f'The package "{package.name}" is being delivered by TRUCK'
    print(message)
    