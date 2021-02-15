from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from accounts.forms import LoginForm
from django.utils.translation import gettext_lazy as _
from accounts.forms import LoginForm


# Create your views here.
def LoginPage(request):
    if request.method == 'POST':
        global code, phone
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            if User.objects.filter(phone=phone).exists():
                request.session['phone'] = f"0{phone}"
                return redirect('accounts:verify')
            else:
                messages.error(request, _('در ارسال رمزعبور مشکلی پیش آمده است، لطفا لحظات دیگری تلاش کنید'),
                               'warning')
                return redirect('accounts:login')
    else:
        form = PhoneLoginForm()
    return render(request, 'accounts/login.html', {'form': form})
