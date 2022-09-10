#Sebastián Barón

class Veterinaria:

#--------------------------------------#
#---------------Atributos--------------#
#--------------------------------------#

    nit = 0

    telefono = 0

    direccion = ""

    nombre = ""

    numSedes = 0

#----------------------------------------#
#---------------Constructor--------------#
#----------------------------------------#

    def __init__( self, nit, telefono, direccion, nombre, horario ):

        self.nit = nit

        self.telefono = telefono

        self.direccion = direccion

        self.nombre = nombre

        self.horario = horario

#-------------------------------------#
#---------------Métodos---------------#
#-------------------------------------#

    def sedes( numSedes ):

        if numSedes == 0:

            print( "No existe ninguna veterinaria" )

        if numSedes == 1:

            print( "La veterinaria únicamente tiene 1 sede" )

        if numSedes > 1:

            print( "La veterinaria cuenta con varias sedes e instalaciones" )

    sedes( 4 )

class Animal:

#--------------------------------------#
#---------------Atributos--------------#
#--------------------------------------#

    nombre = ""

    tipoDeRaza = 0

    peso = 0

    edad = 0

    tipoDeDificultad = ""

#----------------------------------------#
#---------------Constructor--------------#
#----------------------------------------#

    def __init__( self, nombre, tipoDeRaza, peso, edad, tipoDeDificultad ):

        self.nombre = nombre

        self.tipoDeRaza = tipoDeRaza

        self.peso = peso

        self.edad = edad

        self.tipoDeDificultad = tipoDeDificultad

#-------------------------------------#
#---------------Métodos---------------#
#-------------------------------------#

    def añosAnimal( edad ):

        if edad < 4:

            print( "El animal es joven" )

        if edad > 4:

            print( "El animal es adulto" )

    añosAnimal( 5 )

class Cliente:

#--------------------------------------#
#---------------Atributos--------------#
#--------------------------------------#

    nombreCliente = ""

    telefono = 0

    direccionResidencia = ""

    numMascotas = 0
 
    numVisitas = 0

#----------------------------------------#
#---------------Constructor--------------#
#----------------------------------------#

    def __init__( self, nombreCliente, telefono, direccionResidencia, numMascotas, numVisitas ):

        self.nombre = nombreCliente

        self.telefono = telefono

        self.direccionResidencia = direccionResidencia

        self.numMascotas = numMascotas

        self. numVisitas = numVisitas

#-------------------------------------#
#---------------Métodos---------------#
#-------------------------------------#

    def clienteHabitualAño( numVisitas ):

        if numVisitas < 3:

            print( "Cliente bajamente constante en la veterinaria" )

        if numVisitas == 6:

            print( "Cliente medianamente constante en la veterinaria" )

        if numVisitas > 6:

            print( "Cliente altamente constante en la veterinaria" )

    clienteHabitualAño( 7 )

class Medicamentos:

#--------------------------------------#
#---------------Atributos--------------#
#--------------------------------------#

    nombreMedicamento = ""

    formula = ""

    medicamentoTipoAnimal = ""

    numDosis = 0

    formaFarmaceutica = 0

#----------------------------------------#
#---------------Constructor--------------#
#----------------------------------------#

    def __init__( self, nombreMedicamento, formula, medicamentoTipoAnimal, numDosis, formaFarmaceutica ):

        self.nombreMedicamento = nombreMedicamento

        self.formula = formula

        self.medicamentoTipoAnimal = medicamentoTipoAnimal

        self.numDosis = numDosis

        self.formaFarmaceutica = formaFarmaceutica

#-------------------------------------#
#---------------Métodos---------------#
#-------------------------------------#

    def formaFarmaceuticaMedicamento( formaFarmaceutica ):

        if formaFarmaceutica == 1:

            print( "Mediamento en forma farmaceutica de tabletas" )

        if formaFarmaceutica == 2:

            print( "Medicamento en forma farmceutica líquida" )

    formaFarmaceutica( 2 )

class Quirofano:

#--------------------------------------#
#---------------Atributos--------------#
#--------------------------------------#

    instrumentosQuirurgicos = ""

    nombreVeterinario = ""

    numAnimales = 0

    numSalasQuirurgicas = 0

    numVeterinarios = 0

#----------------------------------------#
#---------------Constructor--------------#
#----------------------------------------#

    def __init__( self, instrumentosQuirurgicos, nombreVeterinario, numAnimales, numSalasQuirurjicas, numVeterinarios ):

        self.instrumentosQuirurgicos = instrumentosQuirurgicos

        self.nombreVeterinario = nombreVeterinario

        self.numAnimales = numAnimales

        self.numSalasQuirurgicas = numSalasQuirurjicas

        self.numVeterinarios = numVeterinarios

#-------------------------------------#
#---------------Métodos---------------#
#-------------------------------------#

    def tamañoVeterinaria( numSalasQuirugicas ):

        if numSalasQuirugicas == 1:

            print( "La veterinaria es pequeña" )

        if numSalasQuirugicas == 2:

            print( "La veterinaria es mediana" )

        if numSalasQuirugicas > 2:

            print( "La veterinaria es grande" )

    tamañoVeterinaria( 4 )