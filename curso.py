class Curso():
    def __init__(self, codigo, nombre, prerrequisitos, opcionalidad, semestre, creditos, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisitos = prerrequisitos
        self.opcionalidad = opcionalidad
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado