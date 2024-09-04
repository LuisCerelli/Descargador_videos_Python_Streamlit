## Descargador de videos en Python y Streamlit

Este proyecto es una aplicación web que permite descargar videos de YouTube utilizando la librería `yt_dlp` y la interfaz de usuario con `Streamlit`. El programa extrae la información del video a partir de una URL proporcionada por el usuario, muestra los detalles del video y permite elegir entre diferentes formatos y resoluciones disponibles antes de proceder con la descarga.

**En el contexto de la ingeniería de datos, esta aplicación puede servir para la recolección de datos multimedia, un proceso que puede ser útil en el análisis de grandes volúmenes de contenido audiovisual o en la creación de datasets para proyectos de *machine learning* o *big data*.**

## Funcionamiento

1. **Entrada de URL**: El usuario introduce la URL del video de YouTube que desea descargar.

2. **Extracción de información**: La aplicación utiliza la librería `yt_dlp` para extraer la información del video, sin realizar la descarga inicial. Esto incluye el título, el autor, los diferentes formatos disponibles y las resoluciones del video.

3. **Selección de formato**: La aplicación presenta una lista con las resoluciones y tipos de archivo disponibles. El usuario selecciona el formato que desea descargar.

4. **Información del archivo**: Después de la selección, la aplicación muestra detalles como el tamaño del archivo, la resolución del video y el nombre del autor.

5. **Descarga del video**: Si el usuario confirma que desea proceder con la descarga, el archivo se descarga en el formato y resolución seleccionados.

## Ejemplo de uso

1. El usuario ingresa la URL de un video de YouTube en el campo de texto proporcionado por la aplicación.
2. El programa muestra el título del video y las opciones de resolución disponibles, como 720p o 1080p, y permite elegir una opción.
3. Se muestra el tamaño del archivo y otros detalles antes de solicitar confirmación para proceder con la descarga.
4. Si el usuario presiona el botón "Descargar", el video se descargará en la resolución y formato seleccionados.

## Consideraciones

- **Requisitos**: Para que la aplicación funcione correctamente, es necesario tener las librerías `yt_dlp` y `Streamlit` instaladas. Puedes instalarlas usando los siguientes comandos:

  ```
  pip install yt-dlp
  pip install streamlit
  ```

- **Compatibilidad**: La aplicación depende de `yt_dlp`, que se mantiene actualizada con las últimas políticas de YouTube. Sin embargo, puede haber casos en los que los videos estén protegidos o tengan restricciones que impidan su descarga.

**Este tipo de soluciones es relevante en *data engineering* cuando se trata de extraer y gestionar datos multimedia en gran escala, permitiendo procesar contenido audiovisual de forma estructurada para su posterior análisis o integración en flujos de datos más complejos.**
