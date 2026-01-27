function enviar() {
    const mensaje = document.getElementById("mensaje").value;
    const personaje = document.getElementById("personaje").value;

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje, personaje })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("respuesta").innerText = data.respuesta;
    });
}
