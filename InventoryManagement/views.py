from django.shortcuts import render,HttpResponse,redirect
from InventoryManagement.models import VehicleInventory
from InventoryManagement.form import VehicleForm
from InventoryManagement.form import FeedbackForm
from InventoryManagement.form import TestDriveForm

# Create your views here.
def index(request):
    vehicles=VehicleInventory.objects.all()
    return render(request,'index.html',{'vehicleData':vehicles})

def upload(request):
 
    #to create a empty form
    upload=VehicleForm()
 
    #code to be executed after form is submitted
    if request.method=='POST':
        upload=VehicleForm(request.POST,request.FILES)
 
        #if form data is valid , save it to database
 
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("<H2 style='color:red'> Form Data is Incorrect </h2>")
 
    else:
        #for request method other than POST, bydefault GET
        return render(request,'VehicleRegisterForm.html',{'upload_form':upload})
    

def update_vehicle(request,vehicle):
    vehicle=int(vehicle)
    try:
        vehicle_selected=VehicleInventory.objects.get(id=vehicle)
    except VehicleInventory.DoesNotExist:
        return redirect('index')
 
    vehicle_form=VehicleForm(request.POST or None, instance=vehicle_selected)
 
    if vehicle_form.is_valid():
        vehicle_form.save()
        return redirect('index')
    return render(request,'VehicleRegisterForm.html',{'upload_form':vehicle_form})
 
def delete_vehicle(request,vehicle):
    vehicle=int(vehicle)
    try:
        vehicle_selected=VehicleInventory.objects.get(id=vehicle)
    except VehicleInventory.DoesNotExist:
        return redirect('index')
 
    vehicle_selected.delete()
    return redirect('index')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<H2 style='color:red'> Thanks you for the Feedback </h2>")
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form})

def test_drive_view(request):
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<H2 style='color:red'> Test Drive Scheduled </h2>")
    else:
        form = TestDriveForm()
    return render(request, 'testdrive_form.html', {'test_drive_form': form})