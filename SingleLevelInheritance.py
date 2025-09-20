class alekhya(): // This Is A Parent Class
          def __init__(self,name,age,salary):
                    self.name=name
                    self.age=age
                    self.salary=salary
class marnisha(alekhya): // This Is A Child Class
          def __init__(self,name,age,salary,id):
                    self.name=name
                    self.age=age
                    self.salary=salary
                    self.id=id
ale=alekhya("shaike Alekhya",35,500000)
print(ale.age)
                    
                    

