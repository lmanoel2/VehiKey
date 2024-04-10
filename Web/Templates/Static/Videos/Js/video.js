function submitForm() {
    document.getElementById("camera-form").submit();
}

function changeCam() {
    const camera = document.getElementById("camera-select")
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
    let data = new FormData()

    data.append('camera', camera.value)

    fetch('changed-cam/', {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token.value
        },
        body: data
    }).then(r  => r)
}