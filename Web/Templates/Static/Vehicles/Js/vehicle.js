function add_vehicle() {
    let original = document.getElementById('form-vehicle');
    let clone = original.cloneNode(true);

    clone.querySelector("input[name='color']").value = '';
    clone.querySelector("input[name='plate']").value = '';

    original.parentNode.appendChild(clone);
}

function display_form(tipo){
    const addVehicle = document.getElementById('add-vehicle')
    const attVehicle = document.getElementById('att_vehicle')

    if (tipo === "1"){
        attVehicle.style.display = "none"
        attVehicle.style.display = "none"
        addVehicle.style.display = "block"
    } else if(tipo === "2"){
        attVehicle.style.display = "block"
        addVehicle.style.display = "none"
    }
}

function vehicle_data(){
    const vehicle = document.getElementById("vehicle-select")
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
    let data = new FormData()

    let vehicle_string = vehicle.value.replace(/None/g, 'null').replaceAll("'", '"');
    const vehicle_json = JSON.parse(vehicle_string)


    data.append('id_vehicle', vehicle_json.id)

    fetch('get_vehicle/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrf_token.value
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
        document.getElementById("form-att-vehicle").style.display = 'block'
        document.getElementById("btn-edit-vehicles").style.display = 'block'
        document.getElementById('plate').value = data['plate']
        document.getElementById('color').value = data['color']
    })
}

function update_vehicle(){
    let data = new FormData()
    const vehicle_select = document.getElementById("vehicle-select")
    const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')

    let vehicle = {};
    vehicle.plate = document.getElementById('plate').value
    vehicle.color = document.getElementById('color').value

    let vehicle_string = vehicle_select.value.replace(/None/g, 'null').replaceAll("'", '"');
    const vehicle_json = JSON.parse(vehicle_string)

    vehicle.id = vehicle_json.id
    console.log(vehicle)

    data.append('vehicle', JSON.stringify(vehicle))

    fetch('update_vehicle/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrf_token.value
        },
        body: data
    }).then(function (result){
        return result.json()
    })
}