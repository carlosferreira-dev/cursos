class Calculadora():
    def __init__(self):
        self.funcoes = {
            "soma" : self.soma,
            "subtracao" : self.subtracao,
            "multiplicacao" : self.multiplicacao,
            "divisao" : self.divisao,
            "raiz_quadrada" : self.raiz_quadradada,
            "porcentagem" : self.porcentagem
        }
    
    def soma(self, x, y):
        return x + y
    
    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y): 
        return x * y
    
    def divisao(self, x, y):
        return x / y
    
    def raiz_quadradada(self, x):
        return x ** 0.5
    
    def porcentagem(self, x, y):
        return (x * y) / 100

if __name__ == "__main__":
    calc = Calculadora()
    print(calc.funcoes["soma"](1, 2))
    print(calc.funcoes["subtracao"](1, 2))
    print(calc.funcoes["multiplicacao"](1, 2))
    print(calc.funcoes["divisao"](1, 2))
    print(calc.funcoes["raiz_quadrada"](4))
    print(calc.funcoes["porcentagem"](10, 50))    