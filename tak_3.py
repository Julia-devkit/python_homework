class Worker:
    def __init__(self,name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']
class Position(Worker):
    def full_name(self):
        print(self.name, self.surname, self.position)
    def total_income(self):
        print(self._income_wage + self._income_bonus)
worker_position = Position('Jon','Smith','manager',{'wage':40000,'bonus':3000})
worker_position.full_name()
worker_position.total_income()