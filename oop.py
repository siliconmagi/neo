# create class employee
# class is blueprint for creating instances
# each employee class will be an instance of employee class


class Employee:

    num_of_emp = 0
    raise_amount = 1.04

    # regular methods automatically take instance
    # as first argument 'self'
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Declare class b/c override unintended
        Employee.num_of_emp += 1

    # define method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # method referring to class variable
    # using self allows class instance override
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # classmethod
    # receives class 'cls' as 1st argument, 'amount' as param
    # instead of instance 'self'
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # alternative constructor, accepts employee string
    @classmethod
    def from_str(cls, empStr):
        first, last, pay = empStr.split('-')
        return cls(first, last, pay)


# initialize employees
# added to num_of_emp
emp1 = Employee('Chrono', 'Trigger', 9000)
emp2 = Employee('Xeno', 'Gears', 10000)
emp_str_1 = 'Chrono-Trigger-9000'
emp_str_2 = 'Xeno-Gears-10000'
emp3 = Employee.from_str(emp_str_1)

# edit instance variable
emp1.raise_amount = 1.05

Employee.set_raise_amt(1.05)

# emp1 inherets above assignment
# emp2 inherets class variable
print(emp1.__dict__)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.num_of_emp)
print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
print(emp3.email)
print(emp3.pay)
