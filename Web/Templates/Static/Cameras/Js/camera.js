function add_camera() {
    let original = document.getElementById('form-camera');
    let clone = original.cloneNode(true);

    clone.querySelector("input[name='name']").value = '';
    clone.querySelector("input[name='ip']").value = '';
    clone.querySelector("input[name='port']").value = '';
    clone.querySelector("input[name='user']").value = '';
    clone.querySelector("input[name='password']").value = '';

    original.parentNode.appendChild(clone);
}

function exibir_form(tipo){
    const addCamera = document.getElementById('adicionar-camera')
    const attCamera = document.getElementById('att_camera')

    if (tipo === "1"){
        attCamera.style.display = "none"
        attCamera.style.display = "none"
        addCamera.style.display = "block"
    } else if(tipo === "2"){
        attCamera.style.display = "block"
        addCamera.style.display = "none"
    }
}

function dados_camera(){
    const camera = document.getElementById("camera-select")
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
    let data = new FormData()

    let camera_string = camera.value.replace(/None/g, 'null').replaceAll("'", '"');
    const camera_json = JSON.parse(camera_string)

    data.append('id_camera', camera_json.id)

    fetch('get_camera/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrf_token.value
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
        document.getElementById("form-att-camera").style.display = 'block'
        document.getElementById("btn-edit-cameras").style.display = 'block'
        document.getElementById('name').value = data['name']
        document.getElementById('ip').value = data['ip']
        document.getElementById('password').value = data['password']
        document.getElementById('port').value = data['port']
        document.getElementById('user').value = data['user']
    })
}

function update_camera(){
    let data = new FormData()
    const camera_select = document.getElementById("camera-select")
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')

    let camera = {};
    camera.port = document.getElementById('port').value
    camera.ip = document.getElementById('ip').value
    camera.name = document.getElementById('name').value
    camera.user = document.getElementById('user').value
    camera.password = document.getElementById('password').value

    let camera_string = camera_select.value.replace(/None/g, 'null').replaceAll("'", '"');
    const camera_json = JSON.parse(camera_string)

    camera.id = camera_json.id

    console.log(camera)

    data.append('camera', JSON.stringify(camera))
    console.log(JSON.stringify(camera))
    fetch('update_camera/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrf_token.value
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
        // document.getElementById("form-att-camera").style.display = 'block'
        // document.getElementById('name').value = camera_json['name']
        // document.getElementById('ip').value = data['ip']
        // document.getElementById('password').value = data['password']
        // document.getElementById('port').value = data['port']
        // document.getElementById('user').value = data['user']
    })
}