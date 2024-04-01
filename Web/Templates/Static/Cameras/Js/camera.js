function add_camera(){

    container = document.getElementById('form-camera')

    html = "<br> <div class='row'> <div class='col'> <input type='text' placeholder='nome' class='form-control' name='name'></div> <div class='col'> <input type='text' placeholder='ip' class='form-control' name='ip'> </div> <div class='col'> <input type='number' placeholder='porta' class='form-control' name='port'> </div> </div>"

    container.innerHTML += html
}