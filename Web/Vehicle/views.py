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
    cam_id = request.POST.get('id_vehicle')
    cam = vehicleEndpoints.GetVehicleById(cam_id)
    return JsonResponse(cam)


def update_vehicle(request):
    cam_id = request.POST.get('id_vehicle')
    cam = vehicleEndpoints.GetVehicleById(cam_id)
    return JsonResponse(cam)