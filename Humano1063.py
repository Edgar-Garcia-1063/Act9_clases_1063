print("Act 9 clase humano")
print("Edgar Axel Garcia Aguirre  22308051281063")

print("")

# Zona De Clases
class Humano1063:
    # Zona de atributos
    
    edad=0
    genero=""
    colordeojos=""
    colordepelo=""
    estatura=0
    musicafav=""
    
    # Zona de funciones dentro de la clase
    def tocar1063(self, n):
        print(f"{n} esta tocando la guitarra")
    
    def ver1063(self, n):
        print(f"{n} esta viendo la tele")
        
    def correr1063(self, n):
        print(f"{n} esta corriendo")
        
    def trabajar1063(self, n):
        print(f"{n} esta trabajando")


# Zona de creación de objetos

larrondo=Humano1063()
guisho=Humano1063()

# Zona usando objetos

larrondo.edad=17
larrondo.genero="hombre"
larrondo.colordeojos="cafe"
larrondo.colordepelo="cafe"
larrondo.estatura=1.74
larrondo.musicafav="travis scott"

print("Resultado para larrondo")
print(f"Edad: {larrondo.edad}")
print(f"larrondo es del genero: {larrondo.genero}")
print(f"Los ojos de larrondo son color: {larrondo.colordeojos}")
print(f"El color de cabello de larrondo es: {larrondo.colordepelo}")
print(f"larrondo mide: {larrondo.estatura}")
print(f"el artisra fav de larrondo es: {larrondo.musicafav}")

print("")

guisho.edad=17
guisho.genero="hombre"
guisho.colordeojos="cafe"
guisho.colordepelo="negro"
guisho.estatura=1.72
guisho.musicafav="taylor swift"

print("")

print("")
print("Resultado para guisho")
print(f"Edad: {guisho.edad}")
print(f"guisho es del genero: {guisho.genero}")
print(f"Los ojos de guisho son color: {guisho.colordeojos}")
print(f"El color de cabello de guisho es: {guisho.colordepelo}")
print(f"guisho mide: {guisho.estatura}")
print(f"el artista fav de guisho es: {guisho.musicafav}")

print("")

# Zona usando funciones
print("Resultado para larrondo")
larrondo.tocar1063("larrondo")
larrondo.ver1063("larrondo")
larrondo.correr1063("larrondo")
larrondo.trabajar1063("larrondo")

print("")

print("Resultado para guisho")
guisho.tocar1063("guisho")
guisho.ver1063("guisho")
guisho.correr1063("guisho")
guisho.trabajar1063("guisho")