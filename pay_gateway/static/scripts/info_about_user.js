function on_load() {
    document.querySelector('.plan_and_users').innerHTML = localStorage.getItem('plan') + " - " + localStorage.getItem('userAmount') + " пользователей";
    let resultSumYear = (localStorage.getItem('resultSumYear') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    let resultSumMonth = (localStorage.getItem('resultSumMonth') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    document.querySelector('.price_per_month').innerHTML = "(" + resultSumMonth + " руб / месяц)";
    document.querySelector('.price_per_year').innerHTML = resultSumYear + " руб / год";
    document.querySelector('#price_per_month_2').innerHTML = resultSumMonth + " руб / месяц";
}

on_load();


const EMAIL_REGEXP = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;
const input_email = document.querySelector('.input_email');

function isEmailValid(value) {
    return EMAIL_REGEXP.test(value);
}


const DOMAIN_REGEXP = /^!?([A-Za-z]+)[A-Za-z0-9]{1,}$/;
const input_domain = document.querySelector('.input_domain');

function isDomainValid(value) {
    return DOMAIN_REGEXP.test(value);
}

function onInputDomain() {
    const input_span = document.querySelector('#domain_span');
    if (isDomainValid(input_domain.value)) {
        input_domain.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_domain.style.borderColor = 'red';
        input_span.innerHTML = "<br>Неверное имя домена: " + input_domain.innerHTML.toString() + ".inoutproject.com.<br>" +
            "Пожалуйста, используйте только буквы и цифры.<br>Имя не может начинаться с цифры.<br>Длина не менее двух символов.";
    }
}

input_domain.addEventListener('input', onInputDomain);

function onInputEmail() {
    const input_span = document.querySelector('#email_span');
    if (isEmailValid(input_email.value)) {
        input_email.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_email.style.borderColor = 'red';
        input_span.innerHTML = "Неверный формат email";
    }
}

input_email.addEventListener('input', onInputEmail);


input_email.addEventListener('input', onInputEmail);


const NOTNULL_REGEXP = /^[\s\S]{1,10}/;
const input_org = document.querySelector('.input_org');
const input_phone = document.querySelector('.input_phone');
const input_country = document.querySelector('.input_country');
const input_city = document.querySelector('.input_city');
const input_address = document.querySelector('.input_address');
const input_inn = document.querySelector('.input_inn');
const res_button = document.querySelector('.result_bottom');
const agreem_1 = document.querySelector('#agreem_1');
const agreem_2 = document.querySelector('#agreem_2');

function isNotNullValid(value) {
    return NOTNULL_REGEXP.test(value);
}

function onInputOrg() {
    const input_span = document.querySelector('#org_span');
    if (isNotNullValid(input_org.value)) {
        input_org.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_org.style.borderColor = 'red';
        input_span.innerHTML = "Поле не может быть пустым";
    }
}

input_org.addEventListener('input', onInputOrg);

function onInputPhone() {
    const input_span = document.querySelector('#phone_span');
    if (isNotNullValid(input_phone.value)) {
        input_phone.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_phone.style.borderColor = 'red';
        input_span.innerHTML = "Поле не может быть пустым";
    }
}

input_phone.addEventListener('input', onInputPhone);

function onInputCountry() {
    const input_span = document.querySelector('#country_span');
    if (isNotNullValid(input_country.value)) {
        input_country.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_country.style.borderColor = 'red';
        input_span.innerHTML = "Поле не может быть пустым";
    }
}

input_country.addEventListener('input', onInputCountry);

function onInputCity() {
    const input_span = document.querySelector('#city_span');
    if (isNotNullValid(input_city.value)) {
        input_city.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_city.style.borderColor = 'red';
        input_span.innerHTML = "Поле не может быть пустым";
    }
}

input_city.addEventListener('input', onInputCity);


function onInputAddress() {
    const input_span = document.querySelector('#address_span');
    if (isNotNullValid(input_address.value)) {
        input_address.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_address.style.borderColor = 'red';
        input_span.innerHTML = "Поле не может быть пустым";
    }
}

input_address.addEventListener('input', onInputAddress);


function onInputInn() {
    const input_span = document.querySelector('#inn_span');
    if (isNotNullValid(input_inn.value)) {
        input_inn.style.borderColor = 'green';
        input_span.innerHTML = "";
    } else {
        input_inn.style.borderColor = 'red';
        input_span.innerHTML = "Поле не может быть пустым";
    }
}

input_inn.addEventListener('input', onInputInn);


function checkRadio_1() {
    const input_span = document.querySelector('.agreem_1_span');
    if (agreem_1.checked) {
        input_span.innerHTML = "";
    } else {
        input_span.innerHTML = "<br>Требуется согласиться с правилами!";
    }


}

function checkRadio_2() {
    const input_span_2 = document.querySelector('.agreem_2_span');
    if (agreem_2.checked) {
        input_span_2.innerHTML = "";
    } else {
        input_span_2.innerHTML = "<br>Требуется согласиться с правилами!";
    }
}

agreem_1.addEventListener('click', checkRadio_1)
agreem_2.addEventListener('click', checkRadio_2)


function checkAll() {
    onInputDomain();
    onInputEmail();
    onInputOrg();
    onInputPhone();
    onInputCountry();
    onInputCity();
    onInputAddress();
    onInputInn();
    checkRadio_1();
    checkRadio_2();
    if ((agreem_2.checked) && (agreem_1.checked) && (isNotNullValid(input_inn.value)) && (isNotNullValid(input_address.value)) && (isNotNullValid(input_city.value)) && (isNotNullValid(input_country.value)) && (isNotNullValid(input_phone.value)) && (isNotNullValid(input_org.value)) && (isEmailValid(input_email.value)) && (isDomainValid(input_domain.value))) {
        window.open('https://ya.ru/', '_self' );
        // location.href = "/payment/payment/";
        // window.open('http://localhost:63342/innout_project/pay_gateway/templates/payment.html?_ijt=7nem6b1094tksvtdl0ggb6coro');
    }


}


res_button.addEventListener('click', checkAll);