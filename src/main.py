import os
from ultralytics import solutions
import cv2
import numpy as np

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Definir la región de interés (polígono)
ZONE = np.array([[400, 165], [400, 380], [450, 380], [450, 165]]) #240
#ZONE = np.array([[365, 300],[365, 450],[450, 450],[450, 300]])

# Ruta del video local
video_path = r"C:\Users\Miguel\Downloads\WIN_20241220_15_50_29_Pro.mp4"  # Cambia esta ruta por la de tu video
output_path = r"C:\Users\Miguel\Downloads\video_detectado_output.avi"  # Archivo de salida

# Configuración de redimensionamiento del video
resize_width, resize_height = 720, 480  # Tamaño al que se redimensionará el video

# Abrir el video
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: No se pudo abrir el archivo de video")
    exit()

# Obtener propiedades del video original
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Configurar el escritor de video
video_writer = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*'XVID'),
    fps,
    (resize_width, resize_height)
)

# Inicializar el ObjectCounter sin mostrar anotaciones (show=False)
counter = solutions.ObjectCounter(
    model=r"C:\Users\Miguel\Desktop\Industrial_CV\models\best.pt",  # Ruta del modelo YOLO entrenado
    region=ZONE,  # Región de interés
    show=False,  # No mostrar el video con detecciones
    classes=None,  # Si deseas contar todas las clases detectadas
    show_in=True,  # Mostrar objetos que entran al área
    show_out=False,  # No mostrar los que salen
)


# Configuración para reducir los frames procesados
frame_skip = 5  # Saltar 4 frames entre cada uno procesado (por ejemplo, procesar solo 1 de cada 5 frames)
frame_count = 0  # Contador de frames

# Procesar el video
while True:
    success, frame = cap.read()
    if not success:
        print("Fin del video o error al leer el frame.")
        break

    # Redimensionar el frame al tamaño deseado
    frame_resized = cv2.resize(frame, (resize_width, resize_height), interpolation=cv2.INTER_AREA)

    # Incrementar el contador de frames
    frame_count += 1
    if frame_count % frame_skip != 0:
        continue  # Saltar el frame si no es el correcto

    # Procesar el frame con ObjectCounter
    processed_frame = counter.count(frame_resized)

    # Escribir el frame procesado en el archivo de salida
    video_writer.write(processed_frame)

    # Mostrar el frame procesado en pantalla
    cv2.imshow('Video Detectado', processed_frame)
    print(f"Inward count: {counter.in_count}, Outward count: {counter.out_count}")
    print(f"Muestra objetos por clase: {counter.classwise_counts}")

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
video_writer.release()
cv2.destroyAllWindows()

print(f"Procesamiento completo. El video de salida se guardó en: {output_path}")