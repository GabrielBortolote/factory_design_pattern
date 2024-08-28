# Factory

This project implements a use case for a Design Pattern, the Factory. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/factory-method).

## What it is?

A factory design pattern can handle some problem with crossed inheritance. If you have a group of subclasses that creates and executes operations in a group of subclasses B, Factory it's a good option to handle the problems with types and crossed inheritance.

This is the schema of a Factory pattern:

![schema](/factory-schema.png)

Note that there'are two inheritances happening. The product inheritance and the Creator inheritance. The Creator classes are going to instantiate Product objects, for each subclass of Creator there's a subclass of Product. Learn this schema and you'll forever know what is a Factory Design Pattern.

## Project

Let's implement a Logistic system scratch. A package have to be delivered, and it's going to be delivered by a Logistic class, the Logistic can be SeaLogistic or EarthLogistic. The object that deliver the package is a Transport object, that can be a Truck or a Ship. As you can see, we have two inheritances here, Logistics and Transport, where EarthLogistics uses Truck transportation and SeaLogistics uses Ship transportation. This can be easily implemented using the Factory. To implements this project let's use the top-down approach, so first:

### Step 1: call the deliver() method

There's nothing implemented yet, but we know that we are going to use Factory and we know that we have a package that can be delivered by Sea and by Earth, so let's start calling the *deliver(package)* method and than move on implementing whatever is missing:

python```
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
```