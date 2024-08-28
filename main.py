from package import Package
from logistic import SeaLogistics, EarthLogistics

if __name__ == '__main__':
  # create logistics
  seaLogistics = SeaLogistics()
  earthLogistics = EarthLogistics()

  # create the package2
  package_1 = Package(name='Package Being Delivered by Sea')
  package_2 = Package(name='Package Being Delivered by Earth')

  # deliver
  seaLogistics.deliver(package_1)
  earthLogistics.deliver(package_2)
