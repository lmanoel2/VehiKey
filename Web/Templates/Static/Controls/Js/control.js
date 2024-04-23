function select_camera(){
    document.getElementById("btn-open-hardware").style.display = 'flex'
    document.getElementById("btn-keep-hardware").style.display = 'flex'
    document.getElementById("btn-close-hardware").style.display = 'flex'
}


function open_door(){
    let contextDataElement = document.getElementById('context-data');
    let csrfToken = contextDataElement.dataset.csrfToken;

    let data = new FormData()
    data.append('action','open')

    fetch('send_command/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrfToken
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
    })
}

function keep_door(){
    let contextDataElement = document.getElementById('context-data');
    let csrfToken = contextDataElement.dataset.csrfToken;

    let data = new FormData()
    data.append('action','keep')

    fetch('send_command/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrfToken
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
    })
}

function close_door(){
    let contextDataElement = document.getElementById('context-data');
    let csrfToken = contextDataElement.dataset.csrfToken;

    let data = new FormData()
    data.append('action','close')

    fetch('send_command/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrfToken
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
    })
}