class ConversorTemperatura:
    def Celsius_para_fahrenheit(c):
        if not ConversorTemperatura.__validar(c):
            raise ValueError("valor inválido para temperatura.")
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_para_Celsius(f):
        if not ConversorTemperatura .__validar(f):
            raise ValueError("valor inválido para temperatura.")
        return (f - 32) * 5/9

    @staticmethod
    def __validar(valor):
        return isinstance(valor,(int,float))