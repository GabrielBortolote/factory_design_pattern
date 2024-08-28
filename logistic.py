from abc import ABC, abstractmethod
from package import Package
from transport import Transport, Ship, Truck

class Logistic(ABC):
  @abstractmethod
  def create_transport(self) -> Transport:
    pass

  def deliver(self, package: Package) -> None:
    transport = self.create_transport()
    transport.deliver(package)

class SeaLogistics(Logistic):
  def create_transport(self):
    return Ship()

class EarthLogistics(Logistic):
  def create_transport(self):
    return Truck()