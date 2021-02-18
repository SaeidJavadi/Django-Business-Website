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
    var goodColor = "#66cc66";
    var badColor = "#ff6666";

    if(password.value.length >= 8)
    {
        password.style.backgroundColor = goodColor;
    }else {
        password.style.backgroundColor = badColor;
        // password.setCustomValidity('رمزعبور باید بیشتر از 8 کاراکتر باشد')
    }

    if (confirm.value === password.value) {
        confirm.setCustomValidity('');
        confirm.style.backgroundColor = goodColor;
        password.style.backgroundColor = goodColor;
    } else {
        confirm.setCustomValidity('رمزهای عبور باید یکسان باشند');
        confirm.style.backgroundColor = badColor;
    }
}

function fuulNameJS(){
    const name = document.querySelector('input[name=full_name]');
    if(name.value === ''){
        name.setCustomValidity('نام و نام خانوادگی خود را وارد کنید');
    }
}
