class Usuario: #Esto es el molde. El objeto que asigne a esta clase tendrá las características que tengo acá especificadas
    def __init__(self, nombre, email, cuenta, interes = 0.2, balance): # lo de e-mail es un atributo que puede ir en blanco para que al momento de imprimir no tire error
        self.nombre = nombre
        self.email = email
        self.cuenta = cuenta
        self.interest = interest
        self.balance = balance
        self.log ("objeto creado")
    
    def registrarLog(self, mensaje):
        f = open("historial.txt","a",encoding="utf8")  #para guardar estos registros,se usa esto,a de append para que no borre el historial previo
        f.write(mensaje + "\n")
        f.close()
        return self
    
    def deposit(self, deposito): # por si acaso: los def son métodos.
        self.cuenta += deposito
        self.log(f"Cliente deposita $ {deposito}")
        return self.cuenta

    def make_withdrawal(self, retiro):  # devolverá el balance actual usando los atributos seleccionados MENOS el retiro
        if self.cuenta < retiro:
            self.log(f"Cuenta {self.nombre} no tiene saldo suficiente para retiro")
            print(f"No tiene saldo suficiente")
            return self
        self.cuenta -= retiro
        self.log(f"Cliente realiza retiro de {retiro}")
        return self.cuenta
    
    def display_user_balance(self):
        self.log(f"Cliente {self.nombre} solicita balance")
        return f"Cliente: {self.nombre}, saldo CLP: {self.cuenta}" # devuelve el saldo post retiro (si hubiere)
        
    
    # def transfer_money(self, retiro, deposito):
    #     self.cuenta -= retiro
    #     self.cuenta += deposito
            # return f"Cliente {self.nombre} transfirio QUÉ SÉ YO a {self.nombre}"

    def transfer_money (self, other_user, amount): # que tengo que hacer para transferir dinero?
        other_user.make_deposit(amount) #hacer un deposito a otro usuario
        self.make_withdrawal(amount) #de mi mismo hacer un giro para transferirlo
        self.display_user_balance() #una vez hecho el giro,ver mi saldo
        other_user.display_user_balance() #una vez hecha la transferencia,ver el saldo del otro usuario

    
    def __str__(self):
        return f"Cliente: {self.nombre}, saldo CLP: {self.cuenta}" # devuelve el saldo post retiro (si hubiere)
    

usuario1 = Usuario("Susana", "susana.pavez@gmail.com", 1000000) # aquí estoy instanciando (ese verbo está ok?) lo que debe ejecutarse con la clase
usuario1.deposit(10000).deposit(20000).deposit(30000).make_withdrawal(40000) 
usuario1.display_user_balance()


usuario2 = Usuario("Juanito Arcoiris", "juanitoarcoiris@gmail.com", 1000000) 
usuario2.deposit(50000).deposit(60000).make_withdrawal(50000).make_withdrawal(40000)

usuario3 = Usuario("Max Power", "maxpower@gmail.com", 1000000) 
usuario3.deposit(150000).make_withdrawal(10000).make_withdrawal(20000).make_withdrawal(30000)


print (usuario1)
print (usuario2)
print (usuario3)
