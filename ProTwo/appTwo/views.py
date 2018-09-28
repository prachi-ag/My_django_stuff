from django.shortcuts import render
from appTwo.forms import NewUserForm

def index(request):
    return render(request ,'appTwo/index.html')

# Create your views here.
def user(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid")

    return render(request,'appTwo/users.html', {'form':form})