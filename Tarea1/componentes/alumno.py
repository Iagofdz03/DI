class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self._nota = 0
        self.nota = nota

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= 10:
            self._nota = valor
        else:
            print("Nota inválida (0..10). Se mantiene el valor anterior.")
