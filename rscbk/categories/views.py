from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .forms import AdditemForm
from categories.models import *

@login_required
def additems(request):
    addform = AdditemForm()
    if request.method == 'POST':
        addform = AdditemForm(request.POST,request.FILES)
        if addform.is_valid():
            form = addform.save(commit=False)
            form.itemuser = request.user
            form.save()
            return redirect('myuserdashboard')

    return render(request, 'additems.html', {'addform':addform})

@login_required
def view_item(request, item_id):
    itm_obj = Items.objects.get(id=item_id)

    context = {'obj':itm_obj}
    return render(request, 'item_details.html', context)