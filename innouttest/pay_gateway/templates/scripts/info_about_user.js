function on_load() {
    document.querySelector('.plan_and_users').innerHTML = localStorage.getItem('plan') + " - " + localStorage.getItem('userAmount') + " пользователей";
    let resultSumYear = (localStorage.getItem('resultSumYear') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    let resultSumMonth = (localStorage.getItem('resultSumMonth') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    document.querySelector('.price_per_month').innerHTML = "(" + resultSumMonth + " руб / месяц)";
    document.querySelector('.price_per_year').innerHTML = resultSumYear + " руб / год";
    document.querySelector('#price_per_month_2').innerHTML = resultSumMonth + " руб / месяц";
}

on_load();

function validate_fields() {
    document.write("Hello!")
}


const EMAIL_REGEXP = /^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/iu;
const input_email = document.querySelector('.input_email');

function isEmailValid(value) {
    return EMAIL_REGEXP.test(value);
}

function onInputEmail() {
    if (isEmailValid(input_email.value)) {
        input_email.style.borderColor = 'green';
    } else {
        input_email.style.borderColor = 'red';
    }
}

input_email.addEventListener('input', onInputEmail);


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
        input_span.innerHTML = input_domain.title;
    }
}

input_domain.addEventListener('input', onInputDomain);


const NOTNULL_REGEXP = /^[\s\S]{1,10}/;
const input_org = document.querySelector('.input_org');
const input_phone = document.querySelector('.input_phone');
const input_country = document.querySelector('.input_country');
const input_city = document.querySelector('.input_city');
const input_address = document.querySelector('.input_address');
const input_inn = document.querySelector('.input_inn');

function isNotNullValid(value) {
    return NOTNULL_REGEXP.test(value);
}

function onInputOrg() {
    if (isNotNullValid(input_org.value)) {
        input_org.style.borderColor = 'green';
    } else {
        input_org.style.borderColor = 'red';
    }
}

input_org.addEventListener('input', onInputOrg);

function onInputPhone() {
    if (isNotNullValid(input_phone.value)) {
        input_phone.style.borderColor = 'green';
    } else {
        input_phone.style.borderColor = 'red';
    }
}

input_phone.addEventListener('input', onInputPhone);

function onInputCountry() {
    if (isNotNullValid(input_country.value)) {
        input_country.style.borderColor = 'green';
    } else {
        input_country.style.borderColor = 'red';
    }
}

input_country.addEventListener('input', onInputCountry);

function onInputCity() {
    if (isNotNullValid(input_city.value)) {
        input_city.style.borderColor = 'green';
    } else {
        input_city.style.borderColor = 'red';
    }
}

input_city.addEventListener('input', onInputCity);


function onInputAddress() {
    if (isNotNullValid(input_address.value)) {
        input_address.style.borderColor = 'green';
    } else {
        input_address.style.borderColor = 'red';
    }
}

input_address.addEventListener('input', onInputAddress);


function onInputInn() {
    if (isNotNullValid(input_inn.value)) {
        input_inn.style.borderColor = 'green';
    } else {
        input_inn.style.borderColor = 'red';
    }
}

input_inn.addEventListener('input', onInputInn);


