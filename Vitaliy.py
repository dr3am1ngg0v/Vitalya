import os

os.system('cls')

class Robot:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.name = "V"
            cls.__instance.inventory_number = "AA001221-56"
            cls.__instance.operating_company = None
            cls.__instance.functions = []
        return cls.__instance

    def set_name(self, new_name):
        self.name = new_name

    def set_operating_company(self, new_operating_company):
        self.operating_company = new_operating_company

    def get_info(self):
        return f"Name: {self.name}, Inventory Number: {self.inventory_number}, Operating Company: {self.operating_company}, Functions: {self.functions}"

class RobotDecorator:
    def __init__(self, robot):
        self.robot = robot

    def build_house(self):
        self.robot.functions.append("build_house")

    def build_shed(self):
        self.robot.functions.append("build_shed")

    def add_floor(self):
        self.robot.functions.append("add_floor")

    def remove_floor(self):
        self.robot.functions.append("remove_floor")

if __name__ == "__main__":
    robot = Robot()
    robot_decorator = RobotDecorator(robot)
    robot_decorator.build_house()
    robot_decorator.build_shed()
    print(robot.get_info())
    # Name: V, Inventory Number: AA001221-56, Operating Company: None, Functions: ['build_house', 'build_shed']

    robot.set_name("VITA")
    robot.set_operating_company("OOO Koshmarik")
    robot_decorator.add_floor()
    print(robot.get_info())
    # Name: VITA, Inventory Number: AA001221-56, Operating Company: OOO Koshmarik, Functions: ['build_house', 'build_shed', 'add_floor']

    robot_decorator.remove_floor()
    print(robot.get_info())
    # Name: VITA, Inventory Number: AA001221-56, Operating Company: OOO Koshmarik, Functions: ['build_house', 'build_shed', 'add_floor', 'remove_floor']

    robot2 = Robot()
    print(robot2.get_info())
    # Name: VITA, Inventory Number: AA001221-56, Operating Company: OOO Koshmarik, Functions: ['build_house', 'build_shed', 'add_floor', 'remove_floor']