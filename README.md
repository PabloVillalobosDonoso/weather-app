# 🌤️ Clima App - 5 Días

## 📌 Resumen del Proyecto

Esta aplicación web permite consultar el clima de una ciudad específica durante los próximos 5 días.
El usuario ingresa una **ciudad y un país**, y la aplicación obtiene automáticamente:

* Temperatura máxima y mínima 🌡️
* Velocidad del viento 💨
* Visualización en formato de tarjetas horizontales
* Iconos dinámicos según el clima

Todo esto se presenta con una interfaz moderna, animaciones suaves y manejo de errores amigable.

---

## ⚙️ Instrucciones de Instalación

No se requiere instalación compleja ni dependencias externas.

### Pasos:

1. Descarga o copia el archivo `index.html`
2. Ábrelo con cualquier navegador web moderno (Chrome, Edge, Firefox, etc.)
3. ¡Listo! 🎉

---

## 🚀 Guía de Uso

1. Ingresa el nombre de la **ciudad**
2. Ingresa el **país**
3. Haz clic en el botón **"Consultar"**
4. Visualiza el clima de los próximos 5 días en pantalla

Si ocurre un error:

* Se mostrará una ventana emergente con el mensaje correspondiente

---

## 🖼️ Ejemplo de Resultados

### Visualización:

```
Santiago, Chile

[ ☀️ Día 1 ] [ ⛅ Día 2 ] [ 🌥️ Día 3 ] [ ☀️ Día 4 ] [ ❄️ Día 5 ]
```

### Ejemplo de tarjeta:

```
☀️
2026-03-19
Max: 28°C
Min: 15°C
💨 10 km/h
```

---

## ✨ Funcionalidades

* 🔎 Búsqueda de ciudad y país
* 🌍 Geocodificación automática (latitud y longitud)
* 📅 Clima de 5 días
* 🎨 Interfaz moderna con CSS
* 🎬 Animaciones suaves (fade + slide)
* 🌤️ Iconos dinámicos según temperatura
* ⚠️ Manejo de errores con ventana emergente
* 📱 Diseño responsivo básico

---

## ⚠️ Manejo de Errores

La aplicación valida y maneja distintos tipos de errores:

* ❌ Campos vacíos
* 🔢 Entrada con números inválidos
* 🌐 Problemas de conexión
* 🔍 Ciudad no encontrada
* ⚙️ Fallos en la API

Todos los errores se muestran mediante un **modal emergente con botón "Aceptar"**, evitando que la aplicación se rompa.

---

## 🔗 Información de la API

### API utilizada:

**Open-Meteo**

#### Endpoints usados:

1. Geocoding:

```
https://geocoding-api.open-meteo.com/v1/search
```

2. Clima:

```
https://api.open-meteo.com/v1/forecast
```

#### Datos obtenidos:

* Latitud y longitud
* Temperatura máxima y mínima
* Velocidad del viento

📌 No requiere API Key (uso gratuito)

---

## 🚧 Mejoras Futuras

* 🌙 Modo oscuro
* 📍 Geolocalización automática del usuario
* 🌧️ Iconos reales según código meteorológico
* 📊 Gráficos de temperatura
* 📱 Diseño completamente responsive (mobile-first)
* 🔔 Notificaciones de clima
* 🌐 Soporte multi-idioma

---

## 📁 Estructura del Proyecto

```
📦 clima-app
 └── index.html
```

---

## 🛠️ Tecnologías Utilizadas

* HTML5
* CSS3
* JavaScript (Vanilla)
* API REST (Open-Meteo)

---

## 👨‍💻 Autor

Proyecto desarrollado como práctica de consumo de APIs, manejo de errores y diseño de interfaces web modernas.

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos y personales.
