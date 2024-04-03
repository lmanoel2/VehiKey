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
    console.log('Cheguei em dados camera')
    const camera = document.getElementById("client-select")
    const data = {
        "ip":"10.7.7.146",
        "port": 80,
        "user": "admin",
        "password": "admin123",
        "name": "Camera bancada",
        "manufacturer": "INTELBRAS"
    }

    fetch('http://127.0.0.1:5000/camera/2', {
        method: "PUT",
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
        console.log(data)
    })
}