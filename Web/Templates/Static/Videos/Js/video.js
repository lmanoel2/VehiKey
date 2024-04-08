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

    data.append('id_vehicle', vehicle.value)

    fetch('get_vehicle/', {
        method: "POST",
        headers: {
          'X-CSRFToken': csrf_token.value
        },
        body: data
    }).then(function (result){
        return result.json()
    }).then(function (data){
        console.log(data)
        document.getElementById("form-att-vehicle").style.display = 'block'
        document.getElementById("btn-edit-vehicles").style.display = 'block'
        document.getElementById('plate').value = data['plate']
        document.getElementById('color').value = data['color']
    })
}