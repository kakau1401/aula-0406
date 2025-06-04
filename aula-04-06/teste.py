class Produto:
  def __init__(self, preco):
        self.__preco = preco

@property
def preco (self):
        return self.__preco

@preco.setter
def preco(self,novo_preco):
    if novo_preco <= 0:
        raise ValueError("o preço deve ser maior que zero")
    
    else:
     self.__preco = novo_preco