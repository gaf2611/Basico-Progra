class ExamenMedico:
    def __init__(self, medico, nombre, tipo):
        self.medico = medico
        self.nombre = nombre
        self.tipo = tipo

class CitaMedica:
    def __init__(self, numero, nombre_paciente, fecha):
        self.numero = numero
        self.nombre_paciente = nombre_paciente
        self.fecha = fecha
        self.examenes = [] 

    def registrar_examen(self, medico, nombre_examen, tipo):
        examen = ExamenMedico(medico, nombre_examen, tipo)
        self.examenes.append(examen)

    def primer_examen(self):
        if self.examenes:
            return self.examenes[0]
        else:
            return "No hay exámenes registrados para esta cita."

    def ultimo_examen(self):
        if self.examenes:
            return self.examenes[-1]
        else:
            return "No hay exámenes registrados para esta cita."

    def examenes_urgentes(self):
        urgentes = [examen for examen in self.examenes if examen.tipo == "Es urgente"]
        if urgentes:
            return urgentes
        else:
            return "No se han registrado exámenes urgentes para esta cita."

    def informacion_cita(self):
        informacion = f"Número de Cita: {self.numero}\nNombre del Paciente: {self.nombre_paciente}\nFecha de la Cita: {self.fecha}\n"
        if self.examenes:
            informacion += "Exámenes Registrados:\n"
            for examen in self.examenes:
                informacion += f" Solicita el Medico: {examen.medico}\n   Nombre del Examen: {examen.nombre}\n   Tipo: {examen.tipo}\n"
        else:
            informacion += "No se han registrado exámenes para esta cita."
        return informacion


