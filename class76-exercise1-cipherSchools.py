# class phone: #base class/parent class
#     def __init__(self,brand,model_name,price):
#         self.brand =brand
#         self.model_name = model_name
#         self._price = max(price,0)

#     def full_name(self):
#         return f"{self.brand} {self.model_name}"
    
#     def make_a_call(self,number):
#         return f"calling{number}...."

# class Smartphone(phone): #derived / child class
#     def __init__(self, brand, model_name, price):
#         #two ways
#         # phone.__init__(self,brand,model_name,price ,ram, internal memory, rear_camera):
#         super().__init__(brand, model_name, price)
#         self.ram = ram
#         self.internal_memory = 
#         self.rear_camera = 

# phone = phone('nokia' , '1100' , 1000)
# smartphone = Smartphone('onePlus' , '5', 30000 , '6 GB' , '64 GB' , '20 MP')
# print(phone.full_name())
# print(Smartphone.full_name() + f"and price is {smartphone._price}")