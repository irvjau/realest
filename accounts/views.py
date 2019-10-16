from django.shortcuts import render, HttpResponse

# Create your views here.

def home(default):
    return HttpResponse("home page")

def signup_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/') 
        else:
            print(form.errors)
    else:
        form = SignUpForm

    args = {'form': form}
    return render(request, 'signup_form.html', args)


