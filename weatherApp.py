import requests

def obtener_coordenadas(ciudad, pais):
    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        params = {
            "name": f"{ciudad}, {pais}",
            "count": 1,
            "language": "es",
            "format": "json"
        }

        respuesta = requests.get(url, params=params, timeout=10)
        respuesta.raise_for_status()

        data = respuesta.json()

        if "results" in data and len(data["results"]) > 0:
            resultado = data["results"][0]
            return (
                resultado["latitude"],
                resultado["longitude"],
                resultado["name"],
                resultado.get("country", "Desconocido")
            )
        else:
            print("⚠️ No se encontró la ciudad con ese país. Intenta nuevamente.")
            return None, None, None, None

    except requests.exceptions.Timeout:
        print("⏱️ La solicitud tardó demasiado.")
    except requests.exceptions.ConnectionError:
        print("🌐 Error de conexión a internet.")
    except requests.exceptions.HTTPError:
        print("❌ Error en la respuesta del servidor.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

    return None, None, None, None


def obtener_clima(lat, lon):
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }

        respuesta = requests.get(url, params=params, timeout=10)
        respuesta.raise_for_status()

        data = respuesta.json()

        if "current_weather" in data:
            clima = data["current_weather"]
            temperatura = clima.get("temperature")
            viento = clima.get("windspeed")

            return temperatura, viento
        else:
            print("⚠️ No se pudo obtener el clima.")
            return None, None

    except requests.exceptions.Timeout:
        print("⏱️ La solicitud del clima tardó demasiado.")
    except requests.exceptions.ConnectionError:
        print("🌐 Error de conexión a internet.")
    except requests.exceptions.HTTPError:
        print("❌ Error en la API del clima.")
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

    return None, None


def pedir_datos():
    while True:
        ciudad = input("Ingresa el nombre de la ciudad: ").strip()
        pais = input("Ingresa el país: ").strip()

        if ciudad == "" or pais == "":
            print("⚠️ Ni la ciudad ni el país pueden estar vacíos.\n")
        elif any(char.isdigit() for char in ciudad + pais):
            print("⚠️ No deben contener números.\n")
        else:
            return ciudad, pais


def main():
    while True:
        ciudad, pais = pedir_datos()

        lat, lon, nombre_ciudad, nombre_pais = obtener_coordenadas(ciudad, pais)

        if lat is None:
            continue

        temperatura, viento = obtener_clima(lat, lon)

        if temperatura is not None:
            print("\n--- Clima Actual ---")
            print(f"Ciudad: {nombre_ciudad}")
            print(f"País: {nombre_pais}")
            print(f"Temperatura: {temperatura} °C")
            print(f"Viento: {viento} km/h")
            break
        else:
            print("Intentando nuevamente...\n")


if __name__ == "__main__":
    main()