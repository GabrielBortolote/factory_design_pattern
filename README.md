# Factory

This project implements a use case for a Design Pattern, the Factory. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/factory-method).

## What it is?

A **Factory Design Pattern** can handle some structural issues with crossed inheritance. If you have a group of subclasses A that creates and executes operations in a group of subclasses B, Factory it's a good option to handle typing and instantiation issues.

This is the schema of a Factory pattern:

![schema](/factory-schema.png)

Note that there'are two inheritances happening. The **Product** inheritance and the **Creator** inheritance. Note that:

- The Creator classes are going to instantiate Product objects;
- For each Creator subclasses there's a subclass of Product.

Learn this schema and you'll forever know what is a Factory Design Pattern.

## Project

Let's implement a Logistic system scratch. A package have to be delivered, and it's going to be delivered by a **Logistic** object. There's two types of possible Logistics: 

1. **SeaLogistic**;
2. **EarthLogistic**.

The object that deliver the package is a **Transport** object, that can be a:

1. **Truck**;
2. **Ship**.

As you can see, we have two inheritances here, Logistics and Transport, where EarthLogistics uses Truck transportation and SeaLogistics uses Ship transportation. This can be easily implemented using the Factory. To implement this project let's use the top-down approach, so first:

### Step 1: call the deliver() method

There's nothing implemented yet, but we know that we are going to use Factory and we know that we have a package that can be delivered by Sea and by Earth, so let's start calling the *deliver(package)* method and than move on implementing whatever is missing:

main.py

```python
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

### Step 2: create Logistics

Now we need to create the logistic class and subclasses. We also need to create a simple Package class:

package.py

```python
class Package:
  def __init__(self, name:str):
    self.name = name
```

logistic.py

```python
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
```

As you can see, now we two Logistics, each Logistics uses a type of transport, each one with the correct transport subclass. Now we need to create the transport class and subclasses.

### Step 3: create Transport

```python
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
```

Now we have everything completed. We can execute the main code.

```bash
python main.py 
The package "Package Being Delivered by Sea" is being delivered by SHIP
The package "Package Being Delivered by Earth" is being delivered by TRUCK
```

As you can see, each package was delivered using a different logistic.

## Why is this amazing?

Can´t you see? We implemented two different ways of deliver a package, the logic of the deliver function can be implemented inside Truck or Ship or inside SeaLogistics and EarthLogistics, they could be totally different one from each other but both are Transport and both are being used the same way. The **client code** (in this case, the code inside *main.py*), don´t know what is Ship or a Truck, the client only instantiate a type of Logistics and call deliver, all the details are not implemented in the client scope, and all the operation can be customizable and the structure keep being the same.

In the same way we can extend TrainLogistic from Logistic and Train from Transport, implementing a totally new way to deliver, but using the same structure. We can also use the power of abstract classes to implements default behavior inside Transport.deliver().

Isn't this magic? Of course it is.
