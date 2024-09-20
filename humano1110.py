print("Act 9 clase humano")
print("Miriam Vargas Mat:22308051281110")
# Zona de class

class Humano1110:
    # Zona de atributos dentro de la clase
    edad= 0
    Genero= 0
    FechaNaci= 0
    estatura= 0
    Ojos= 0
    Nacionalidad= 0

    # Zona de funciones dentro de la clase
    def correr1110(self,n):
        print(f"{n} esta corriendo ufff....")
    def bailar1110(self,n):
        print(f"{n} esta bailando case 143")
    def saltar1110(self,n):
        print(f"{n} esta saltando")
    def dormir1110(self,n):
        print(f"{n} esta durmiendo en su cuarto")
    def jugando1110(self,n):
        print(f"{n} esta jugando videojuegos")
    
    # Zona de creacion de objetos
Miriam=Humano1110()
Felix=Humano1110()

# Zona de usando objetos
print("\n-------Resultados para Miriam-------") 
Miriam.edad=16
print(f"Edad : {Miriam.edad}")

Miriam.Genero="Femenino"
print(f"Genero : {Miriam.Genero}")

Miriam.FechaNaci="25 de noviembre del 2007"
print(f"Fecha de nacimiento : {Miriam.FechaNaci}")

Miriam.estatura=160
print(f"Estatura : {Miriam.estatura}")

Miriam.Ojos="Cafe"
print(f"Color de ojos : {Miriam.Ojos}")

# Funciones
print("\n----Funciones----")
Miriam.correr1110("Miriam")
Miriam.jugando1110("Miriam")
Miriam.saltar1110("Miriam")
Miriam.dormir1110("Miriam")



print("\n-------Resultado para Felix-------")
Felix.edad=24
print(f"Edad : {Felix.edad}")
Felix.correr1110("Felix")

Felix.Genero="Masculino"
print(f"Genero : {Felix.Genero}")

Felix.FechaNaci="15 de septiembre del 2000"
print(f"Fecha de nacimiento : {Felix.FechaNaci}")

Felix.estatura=1.71
print(f"Estatura : {Felix.estatura}")

Felix.Ojos="Cafe"
print(f"Color de ojos : {Felix.Ojos}")

Felix.Nacionalidad="Australiano"
print(f"Nacionalidad : {Felix.Nacionalidad}")

# Funciones
print("\n----Funciones----")
Felix.correr1110("Felix")
Felix.jugando1110("Felix")
Felix.saltar1110("Felix")
Felix.dormir1110("Felix")
Felix.bailar1110("Felix")