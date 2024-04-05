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
        document.getElementById("btn-edit-cameras").style.display = 'block'
        document.getElementById('name').value = data['name']
        document.getElementById('ip').value = data['ip']
        document.getElementById('password').value = data['password']
        document.getElementById('port').value = data['port']
        document.getElementById('user').value = data['user']
    })
}

function update_camera(){
    const camera = document.getElementById("camera-select")
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
    let data = new FormData()
    console.log('cheguei em update_camera!')
    // data.append('id_camera', camera.value)
    //
    // fetch('get_camera/', {
    //     method: "POST",
    //     headers: {
    //       'X-CSRFToken': csrf_token.value
    //     },
    //     body: data
    // }).then(function (result){
    //     return result.json()
    // }).then(function (data){
    //     document.getElementById("form-att-camera").style.display = 'block'
    //     document.getElementById('name').value = data['name']
    //     document.getElementById('ip').value = data['ip']
    //     document.getElementById('password').value = data['password']
    //     document.getElementById('port').value = data['port']
    //     document.getElementById('user').value = data['user']
    // })
}