import json
import os
import sys

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_dir)

from Web.Endpoints.VehicleEndpoints import VehicleEndpoints

vehicleEndpoints = VehicleEndpoints()


def vehicle(request):
    if request.method == 'GET':
        vehicles = vehicleEndpoints.GetAllVehicles()
        return render(request, 'vehicle.html', {'vehicles': vehicles})
    if request.method == 'POST':
        vehicleEndpoints.AddRange(request)
        vehicles = vehicleEndpoints.GetAllVehicles()
        return render(request, 'vehicle.html', {'vehicles': vehicles})


def get_vehicle(request):
    vehicle_id = request.POST.get('id_vehicle')
    vehicle = vehicleEndpoints.GetVehicleById(vehicle_id)
    return JsonResponse(vehicle)


def update_vehicle(request):
    vehicle = request.POST.get('vehicle')
    vehicle_json = json.loads(vehicle)
    vehicle = vehicleEndpoints.UpdateVehicle(vehicle_json)
    return JsonResponse(vehicle)


def delete_vehicle(request):
    vehicle_id = request.POST.get('id_vehicle')
    vehicleEndpoints.DeleteVehicle(vehicle_id)
    return HttpResponse(status=200)
