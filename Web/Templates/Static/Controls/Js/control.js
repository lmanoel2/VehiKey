function select_camera(){
    document.getElementById("btn-open-hardware").style.display = 'flex'
    document.getElementById("btn-keep-hardware").style.display = 'flex'
    document.getElementById("btn-close-hardware").style.display = 'flex'
}


function open_door(){
    console.log('OPEN')
    const camera_select = document.getElementById("camera-select")
    let contextDataElement = document.getElementById('context-data');
    let csrfToken = contextDataElement.dataset.csrfToken;

    let data = new FormData()

    let camera_string = camera_select.value.replace(/None/g, 'null').replaceAll("'", '"');
    const camera_json = JSON.parse(camera_string)


    let json_data = {
        action: 'open',
        topic_suffix: camera_json.controller
    };

    data.append('control', JSON.stringify(json_data))

    fetch('send_command/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrfToken
        },
        body: data
    }).then(function (result){
        return result.json()
    })
}

function keep_door(){
    const camera_select = document.getElementById("camera-select")
    let contextDataElement = document.getElementById('context-data');
    let csrfToken = contextDataElement.dataset.csrfToken;

    let data = new FormData()

    let camera_string = camera_select.value.replace(/None/g, 'null').replaceAll("'", '"');
    const camera_json = JSON.parse(camera_string)

    let json_data = {
        action: 'keep',
        topic_suffix: camera_json.controller
    };

    data.append('control', JSON.stringify(json_data))

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
    const camera_select = document.getElementById("camera-select")
    let contextDataElement = document.getElementById('context-data');
    let csrfToken = contextDataElement.dataset.csrfToken;

    let data = new FormData()
    let camera_string = camera_select.value.replace(/None/g, 'null').replaceAll("'", '"');
    const camera_json = JSON.parse(camera_string)

    let json_data = {
        action: 'close',
        topic_suffix: camera_json.controller
    };

    data.append('control', JSON.stringify(json_data))

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