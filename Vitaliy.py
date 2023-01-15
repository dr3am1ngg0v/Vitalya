class Robot:
    def __init__(self, name, inventory_number, company_name):
        self.name = name
        self.inventory_number = inventory_number
        self.functions = []
        self.company_name = company_name

    def add_function(self, function):
        self.functions.append(function)

    def list_functions(self):
        return self.functions

    def change_name(self, new_name):
        self.name = new_name

robot = Robot("V", "AA001221-56", "Primary_school")
robot.add_function("build_house")
robot.add_function("build_shed")

robot.change_name("VITA")
robot.company_name = "OOO Koshmarik"
robot.add_function("add_floor")
robot.add_function("remove_top_floor")

robot.change_name("Vitaliy")

print(robot.name) # prints Vitaliy
print(robot.inventory_number) # prints AA001221-56
print(robot.company_name) # prints OOO Koshmarik
print(robot.list_functions()) # prints
