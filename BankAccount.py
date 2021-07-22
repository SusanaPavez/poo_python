class BankAccount: #Esto es el molde. El objeto que asigne a esta clase tendrá las características que tengo acá especificadas
    def __init__(self, nombre, interes): # lo de e-mail es un atributo que puede ir en blanco para que al momento de imprimir no tire error
        self.nombre = nombre
        self.cuenta = 0
        self.interes = 0.02

    def __str__(self):
        return f"Cliente: {self.nombre}, saldo actual: {self.cuenta}" # devuelve el saldo


    def getDeposit(self, deposito): # Devolverá el depósito hecho. Por si acaso: los def son métodos.
        self.cuenta += deposito
        return self

    def getWithdrawal(self, retiro):  # devolverá cuenta - retiro
        self.cuenta -= retiro
        return self
    
    def displayAccountInfo(self, cuenta): # devolverá cuenta 
        self.cuenta = cuenta
        return f"Saldo Actual: $ {cuenta}"

    def yieldInterest (self, interes):
        if self.cuenta > 0:
            self.cuenta = self.cuenta * self.interes # cómo definir esto?
            return self
    


usuario = BankAccount("Susana", 0) #Se define usuario de cuenta y saldo (basado en una historia real)
usuario.getDeposit(1000000) # se deposita
usuario.getWithdrawal(1) # se retira
usuario.displayAccountInfo(())
# usuario.displayAccountInfo() # No estoy segura de cómo hacer un display usando esto, en particular si tengo una función que lo está haciendo
print(usuario)