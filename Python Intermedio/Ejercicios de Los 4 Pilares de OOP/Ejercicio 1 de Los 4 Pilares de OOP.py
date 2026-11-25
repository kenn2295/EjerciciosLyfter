class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        
    def deposite_money(self):
        my_transaction = float(input("Ingrese el monto a depositar: "))
        self.balance += my_transaction
        return self.balance, my_transaction
    
    def dispend_money(self):
        cash = float(input("Cuanto dinero desea retirar?: "))
        possible_transaction = self.balance - cash
        if possible_transaction < 0:
            print("No tiene fondos suficientes")
        else:
            self.balance = possible_transaction
            return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, balance, min_balance):
        super().__init__(balance)
        self.min_balance = min_balance
        
    def dispend_money(self):
        cash = float(input("Cuanto dinero desea retirar?: "))
        possible_transaction = self.balance - cash
        if possible_transaction <= self.min_balance:
            raise ValueError("No puedes retirar dinero: el saldo debe quedar por encima del saldo mínimo.\n")
        else:
            self.balance = possible_transaction
            return self.balance, cash
        
account = SavingsAccount(1000, 200)


while True:
    try:
        print(f"SALDO: {account.balance}")
        print("1 - Retirar Dinero")
        print("2 - Depositar Dinero")
        print("3 - Salir")
        
        my_option = int(input("Seleccione una opción: "))
        if my_option == 1:
            try:
                balance, cash = account.dispend_money()
                print(f"Acabas de retirar: {cash}\n")
            except ValueError as error:
                print(error)
        elif my_option == 2:
            balance, cash = account.deposite_money()
            print(f"Has depositado: {cash}")
        elif my_option == 3:    
            break    
        else:
            print("Numero invalido")
    except ValueError:
        print("Opción invalida\n")
            