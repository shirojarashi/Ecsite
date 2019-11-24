from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'app/index.html')

def signup(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			input_email = form.cleaned_date['email']
			input_password = form.cleaned_date['password1']
			new_user = authenticate(email=input_email, password=input_password)
			if new_user is not None:
				login(request, new_user)
				return redirect('app:index')
	else:
		form = CustomUserCreationForm()
	return render(request, 'app/signup.html', {'form': form})