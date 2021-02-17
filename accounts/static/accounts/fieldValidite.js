function isNumber(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

function onChange() {
    const password = document.querySelector('input[name=password1]');
    const confirm = document.querySelector('input[name=password2]');
    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
    } else {
        confirm.setCustomValidity('رمزهای عبور باید یکسان باشند');
    }
}

function fuulNameJS(){
    const name = document.querySelector('input[name=full_name]');
    if(name.value === ''){
        name.setCustomValidity('نام و نام خانوادگی خود را وارد کنید');
    }
}
