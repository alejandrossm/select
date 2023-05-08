class Alumno:
    rut=""
    paterno=""
    materno=""
    nombre=""

    def __str__(self):
        return f"{self.nombre} {self.paterno} {self.materno}"