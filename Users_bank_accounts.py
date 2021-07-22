client_list = []
class BankAccount:
    def __init__(self, name, last_name, email,int_rate = 0.2,balance= 0):  # constructor
        self.name = name
        self.last_name = last_name
        self.email = email
        self.int_rate = int_rate
        self.log("created")
        self.balance = balance
        
    def getBalance(self):
        self.log(f"Cliente {self.name} {self.last_name} solicita balance")
        return f"Saldo disponible: $ {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.log(f"{self.name} {self.last_name} acaba de hacer un depósito de {amount} a {self.name} {self.last_name} quedando un saldo de : {self.getBalance()}")
        return self

    def withdrawal(self, amount):
        if self.balance < amount:
            print(f"{self.name} {self.last_name} no tiene saldo suficiente - Saldo: {self.balance} diferencia pendiente para retiro: {amount - self.balance}")
            return self
        self.balance -= amount
        self.log(f"{self.name} {self.last_name} realizo un giro de {amount} . Saldo actual: {self.getBalance()}")
        return self
    
    def log(self, message):
        f = open("registry.txt","a",encoding="utf8")  #para guardar estos registros,se usa esto,a de append para que no borre el historial previo
        f.write(message + "\n")
        f.close()
        return self

    def transfer(self, user_destiny, amount):
        if self.balance < amount:
            print(f"{self.name} no tiene saldo suficiente para esta operacion - SALDO: {self.balance}")
            return self

        self.withdrawal(amount)
        user_destiny.deposit(amount)

        return self
    
    def updatedBalanceInt(self):
        if self.balance > 0:
            self.totalInt = (self.balance * self.int_rate)
            self.totalAccount = self.balance + self.totalInt
        else:
            print('No hay saldo disponible')
        return self

    def __str__(self): 
        self.log("El usuario imprimio el objeto usuario")
        return "Objeto Usuario:\t" + self.name + " " + self.last_name

user1 = BankAccount("Paquita","Navajas", "bla@bla.com")
print(user1)
user1.deposit(100000).deposit(200000).deposit(300000).withdrawal(400000).updatedBalanceInt()
print(user1.getBalance())

user2 = BankAccount("Juanito", "Arcoiris", "bleh@bleh.com")
print(user2)
user2.deposit(1000000).deposit(900000).withdrawal(800000).withdrawal(700000).withdrawal(600000).withdrawal(500000).updatedBalanceInt()
print(user2.getBalance())