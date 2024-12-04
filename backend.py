import face_recognition_models
import face_recognition
import psycopg2
import numpy as np
from PIL import Image

cursor = None
conn = None

# Guardar el encoding facial en la base de datos
def add_person(name, image_path):

    iniciar_conexion()

    image = face_recognition.load_image_file(image_path)
    img = Image.open(image_path)
    encoding = face_recognition.face_encodings(image)[0]
    encoding_bytes = np.array(encoding).tobytes()

    cursor.execute("INSERT INTO people (name, face_encoding) VALUES (%s, %s)", (name, encoding_bytes))
    conn.commit()

    cerrar_conexion()
    print(f"¡{name} ha sido agregado a la base de datos!")

# Coincidencia de rostros
def match_face(image_path):

    iniciar_conexion()

    image = face_recognition.load_image_file(image_path)
    unknown_encoding = face_recognition.face_encodings(image)[0]

    cursor.execute("SELECT * FROM people")
    rows = cursor.fetchall()

    cerrar_conexion()

    for row in rows:
        name = row[1]
        encoding = np.frombuffer(row[2], dtype=np.float64)
        
        # Comprobar coincidencia
        matches = face_recognition.compare_faces([encoding], unknown_encoding)
        if matches[0]:
            print(f"Coincidencia encontrada: {name}")
            return row
    print("No hay coincidencias.")
    return None


def iniciar_conexion():
    global conn 
    global cursor

    conn = psycopg2.connect(
        host="localhost",
        database="sarc",
        user="postgres",
        password="almacenandoAndo07"
    )
    cursor = conn.cursor()

def cerrar_conexion():
    global conn 
    global cursor

    cursor.close()
    conn.close()

# Ejemplo de uso
# add_person("", "jorge.png")
#match_face("lilian.jpg")

# Cerrar la conexión
