# Proyecto: Conteo y Clasificación de Objetos en Tiempo Real

## Descripción General
Este proyecto combina **Deep Learning** y **visión por computadora** para realizar el conteo y clasificación de objetos en tiempo real, utilizando el modelo **YOLOv11**. Su desarrollo está orientado a brindar herramientas innovadoras en el **Laboratorio de Automatización** de la **Universidad Nacional de General Sarmiento (UNGS)**, mejorando las prácticas de las ingenierías mediante sistemas de visión artificial.

---

![Conteo objetis](reports\figures\imgReadme.jpg)


## Características Clave
- **Conteo en tiempo real**: Identifica objetos que ingresan o salen de áreas definidas (como líneas o regiones).
- **Clasificación por categoría**: Rastrea y clasifica diferentes tipos de objetos con alta precisión.
- **Interfaz visual**: Los resultados son procesados y anotados directamente sobre las imágenes o videos analizados.

---

## Posibles Aplicaciones
- **Control de accesos**: Monitoreo de objetos o personas que ingresan o salen de zonas restringidas.
- **Monitoreo de flujos**: Conteo y clasificación de objetos en almacenes o procesos industriales.
- **Detección de fallas**: Identificación de defectos o irregularidades en objetos detectados.

---

## Avances Técnicos
1. **Entrenamiento del Modelo**:
   - Dataset personalizado con imágenes propias y técnicas de Data Augmentation.
   - Ajuste del modelo YOLOv11 para escenarios específicos.

2. **Procesamiento en Tiempo Real**:
   - Implementación de algoritmos para identificar objetos que cruzan líneas o regiones predefinidas.
   - Resultados mostrados directamente sobre las imágenes o videos analizados.

---

## Tecnologías y Herramientas
- **Modelo Base**: YOLOv11
- **Frameworks**: PyTorch, OpenCV
- **Hardware**: PC de alto rendimiento; dispositivos edge como Raspberry Pi (en progreso).
- **Protocolos**: MQTT para conectividad IoT e integración industrial.

---

## Instalación
1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/usuario/proyecto-vision.git
   cd proyecto-vision
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar el sistema**:
   ```bash
   python main.py
   ```

---

## Uso
1. Cargar las imágenes o videos en la carpeta `data/input`.
2. Configurar los parámetros en `config.yaml` (líneas de interés, áreas de detección, etc.).
3. Ejecutar el sistema y visualizar los resultados en tiempo real.

---

## Próximos Pasos
- **Optimizar métricas de rendimiento**:
  Continuar con el entrenamiento para mejorar la precisión y la eficiencia del modelo en entornos diversos.

- **Despliegue en dispositivos edge**:
  Implementar el sistema en **Raspberry Pi** para aplicaciones escalables y portátiles.

- **Conectividad IoT**:
  Integrar comunicación mediante **MQTT** para conectar el sistema con dispositivos industriales y redes IoT.

- **Detección de fallas**:
  Ampliar la funcionalidad para identificar defectos o anomalías en objetos detectados.

---

## Contacto
Para más información o consultas, contacta a:
- **Nombre**: [miguel.balderr@gmail.com]
- **Email**: [tu_email@ejemplo.com]
- **Institución**: Universidad Nacional de General Sarmiento

---

© 2025 - Proyecto de Visión por Computadora. Todos los derechos reservados.



