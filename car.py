#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Modules k liye file .py k extension se banegi


# In[3]:


class Car():
    '''A simple Attempt to Represent a Car.'''
    def __init__(self,make,model,year):
        '''Initialize attributes to describe a car. '''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name'''
        long_name=f'{self.year} {self.make} {self.model}'
        return long_name.title()
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')
        
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles>0:
            self.odometer_reading += miles
        elif miles==0:
            print('LOL What is the increment in it?')
        else:
            print("Nah Nah You Can't do that")
    def fill_gas_tank(self):
        print("Kindly fill your gas tank!")


# In[4]:


class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")


# In[ ]:


class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


# In[ ]:




