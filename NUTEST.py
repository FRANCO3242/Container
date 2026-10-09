class IntegerContainer : 
    def __init__(self):
        self.numbers = {}
        self.total = 0
        self.soma = 0

#adiciona um valor no dicionário e retorna o total

    def add (self, value) :
        actual_value = self.numbers.get (value, 0)
        new_value = actual_value + 1
        self.numbers[value] = new_value
        self.total = self.total + 1
        self.soma = self.soma + value
        return self.total
    
#remove um valor da variável e do dicionário


    def remove (self, value) :
        actual_value = self.numbers.get (value, 0)
        if actual_value > 0 :
            self.numbers[value] = actual_value - 1
            self.total = self.total - 1
            self.soma = self.soma - value
            return True
        return False
    
#retorna a média 

    def media (self) :
        if self.total == 0 :
            return 0
        return self.soma / self.total

#retorna valor minímo dentro de self value

    def min (self) :
        if self.total == 0 :
            return None
        return min (self.numbers.keys())
    
#retorna o max

    def max (self) :
        if self.total == 0 :
            return None
        return max (self.numbers.keys())

#retorna quantas chaves diferentes existem dentro de self.numbers

    def distinct_count (self) :
       return len (self.numbers)

#verifica se o dicionário contém valores armazenados
    
    def contains (self, value) :
        actual_value = self.numbers.get (value, 0)
        if actual_value > 0 :
            return True
        return False

#retorna o número que mais aparece no dicionário 

    def most_frequent (self) :

        best_number = None
        best_quantity = 0

        for number, quantity in self.numbers.items() :
            if quantity > best_quantity :

                best_number = number
                best_quantity = quantity

        return best_number

#retorna o valor do meio de uma lista ordenada

    def mediana (self) :
        if self.total == 0 :
            return None

        complete_list = []
        for number, quantity in self.numbers.items() :
            complete_list.extend([number] * quantity)

        complete_list.sort()

        middle = self.total // 2

        if self.total % 2 == 1 :
            return complete_list[middle]
        else :
            return (complete_list[middle - 1] + complete_list[middle]) / 2


     


    
