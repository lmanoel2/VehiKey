function add_camera(){
    const container = document.getElementById('form-camera')
    const html = "<br> <div class='row'> <div class='col'> <input type='text' placeholder='nome' class='form-control' name='name'></div> <div class='col'> <input type='text' placeholder='ip' class='form-control' name='ip'> </div> <div class='col'> <input type='number' placeholder='porta' class='form-control' name='port'> </div> </div>"
    container.innerHTML += html
}

function exibir_form(tipo){
    const addCamera = document.getElementById('adicionar-camera')
    const attCamera = document.getElementById('att_camera')

    if (tipo === "1"){
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

    data.append('id_camera', camera.value)

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
        document.getElementById('name').value = data['name']
        document.getElementById('ip').value = data['ip']
        document.getElementById('password').value = data['password']
        document.getElementById('port').value = data['port']
        document.getElementById('user').value = data['user']
    })
}