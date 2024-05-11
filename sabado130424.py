class Coffee:
    def __int__(self, name, price):
        self.name = name
        self.price = float(price)


    def check_budget(self, budget):
        if not isinstance(budget, (int, float)):
            print("digite float ou int")

        if budget < 0:
            print('vc n tem dinheiro')
            exit()
    def get_chance(self, budget):
        return budget - self.price

    def sell(self, budget):
        self.check_budget(budget)
        if budget >= self.price:
           print(f'vc pode comprar{self.name} coffee')
           if budget == self.price:
               print('está pronto')
           else:
               print(f"aqui tá o troco R${self.get_change(budget)}")

           exit("obrigado pela compra  ")

