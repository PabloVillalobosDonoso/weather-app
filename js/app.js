// Iconos simples según temperatura
function obtenerIcono(temp) {
    if (temp > 30) return "🔥";
    if (temp > 20) return "☀️";
    if (temp > 10) return "⛅";
    if (temp > 0) return "🌥️";
    return "❄️";
}

async function obtenerCoordenadas(ciudad, pais) {
    const res = await fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${ciudad},${pais}&count=1`);
    if (!res.ok) throw new Error("Error en el servidor");

    const data = await res.json();
    if (!data.results) throw new Error("Ciudad no encontrada");

    const r = data.results[0];
    return { lat: r.latitude, lon: r.longitude, ciudad: r.name, pais: r.country };
}

async function obtenerClima(lat, lon) {
    const res = await fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&daily=temperature_2m_max,temperature_2m_min,windspeed_10m_max&timezone=auto`);
    if (!res.ok) throw new Error("Error en clima");

    const data = await res.json();
    return data.daily;
}

async function consultarClima() {
    const ciudad = document.getElementById("ciudad").value.trim();
    const pais = document.getElementById("pais").value.trim();

    if (!ciudad || !pais) return mostrarError("Campos vacíos");
    if (/\d/.test(ciudad + pais)) return mostrarError("No usar números");

    try {
        const coord = await obtenerCoordenadas(ciudad, pais);
        const clima = await obtenerClima(coord.lat, coord.lon);

        document.getElementById("titulo").innerText =
            `${coord.ciudad}, ${coord.pais}`;

        const cont = document.getElementById("dias");
        cont.innerHTML = "";

        for (let i = 0; i < 5; i++) {
            const div = document.createElement("div");
            div.className = "dia";
            div.style.animationDelay = (i * 0.1) + "s";

            const icono = obtenerIcono(clima.temperature_2m_max[i]);

            div.innerHTML = `
                <div class="icono">${icono}</div>
                <strong>${clima.time[i]}</strong><br>
                Max: ${clima.temperature_2m_max[i]}°C<br>
                Min: ${clima.temperature_2m_min[i]}°C<br>
                💨 ${clima.windspeed_10m_max[i]} km/h
            `;

            cont.appendChild(div);
        }

    } catch (e) {
        mostrarError(e.message);
    }
}

function mostrarError(msg) {
    document.getElementById("mensajeError").innerText = msg;
    document.getElementById("modal").style.display = "flex";
}

function cerrarModal() {
    document.getElementById("modal").style.display = "none";
}