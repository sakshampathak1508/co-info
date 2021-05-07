from django.shortcuts import render
from django.http import HttpResponse
from .models import  Oxygen,Plasma,Hospital,Medicine
# Create your views here.

def index(request):
    params  = {}
    return render(request,"home/index.html",params)

def beds(request):
    if request.method=='POST':
        st = request.POST.get('state','')
        t_bed = request.POST.get('type_of_bed','')
        bed1 = Hospital.objects.all().filter(state=st)
        bed2 = Hospital.objects.all().filter(type_of_bed=t_bed) 
        if st!='' and t_bed!='':
            bed = bed1.intersection(bed2).order_by('-time_stamp','type_of_bed','state','name','number_of_beds')
        elif st=='':
            bed = bed2.order_by('-time_stamp','type_of_bed','state','name','number_of_beds')
        else:
            bed  = bed1.order_by('-time_stamp','type_of_bed','state','name','number_of_beds')
        params  = {'bed':bed}
        return render(request,"fact/beds.html",params)
    bed = Hospital.objects.all().order_by('-time_stamp','type_of_bed','state','name','number_of_beds')
    params  = {'bed':bed}
    return render(request,"fact/beds.html",params)

def oxygen(request):
    if request.method=='POST':
        st = request.POST.get('state','')
        otype = request.POST.get('otype','')
        oxy1 = Oxygen.objects.all().filter(state=st)
        oxy2 = Oxygen.objects.all().filter(type_of_facility=otype)
        if st!='' and otype!='':
            oxy = oxy1.intersection(oxy2).order_by('type_of_facility','-time_stamp','quantity','price','name')
        elif st=='':
            oxy = oxy2.order_by('type_of_facility','-time_stamp','quantity','price','name')
        else:
            oxy = oxy1.order_by('type_of_facility','-time_stamp','quantity','price','name')
        params  = {'oxy':oxy}
        return render(request,"fact/oxygen.html",params)
    oxy = Oxygen.objects.all().order_by('type_of_facility','-time_stamp','quantity','price','name')
    params  = {'oxy':oxy}
    return render(request,"fact/oxygen.html",params)
# solve plasma filter
def plasma(request):
    if request.method=='POST':
        st = request.POST.get('state','')
        aplus = request.POST.get('aplus', 'off')
        aminus = request.POST.get('aminus', 'off')
        bplus = request.POST.get('bplus', 'off')
        bminus = request.POST.get('bminus', 'off')
        abplus = request.POST.get('abplus','off')
        abminus = request.POST.get('abminus','off')
        oplus = request.POST.get('oplus','off')
        ominus = request.POST.get('ominus','off')
        p = Plasma.objects.all().filter(blood_group='z+')
        if aplus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='A+'))
        if aminus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='A-'))
        if bplus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='B+'))
        if bminus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='B-'))
        if abplus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='AB+'))
        if abminus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='AB-'))
        if oplus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='O+'))
        if ominus=='on':
            p = p.union(Plasma.objects.all().filter(blood_group='O-'))
        
        plasma = p
        params  = {'plasma':plasma}
        return render(request,"fact/plasma.html",params)
    plasma = Plasma.objects.all().order_by('blood_group','days_since_recovery','-time_stamp')
    params  = {'plasma':plasma}
    return render(request,"fact/plasma.html",params)

def meds(request):
    if request.method=='POST':
        st = request.POST.get('state','')
        medicine = request.POST.get('medicine','')
        med1 = Medicine.objects.all().filter(state=st)
        med2 = Medicine.objects.all().filter(medicine_name=medicine)
        if st!='' and medicine!='':
            meds = med1.intersection(med2).order_by('medicine_name','-time_stamp','quantity','price') 
        elif st=='':
            meds = med2.order_by('medicine_name','-time_stamp','quantity','price') 
        else:
            meds  = med1.order_by('medicine_name','-time_stamp','quantity','price') 
        params  = {'meds':meds}
        return render(request,"fact/meds.html",params)
    meds = Medicine.objects.all().order_by('medicine_name','-time_stamp','quantity','price') 
    params  = {'meds':meds}
    return render(request,"fact/meds.html",params)

