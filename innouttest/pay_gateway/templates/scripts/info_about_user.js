function on_load() {
    document.querySelector('.plan_and_users').innerHTML = localStorage.getItem('plan') + " - " + localStorage.getItem('userAmount') + " пользователей";
    document.querySelector('.price_per_month').innerHTML = "(" + localStorage.getItem('resultSumMonth') + " руб / месяц)";
    document.querySelector('.price_per_year').innerHTML = localStorage.getItem('resultSumYear') + " руб / год";
    document.querySelector('#price_per_month_2').innerHTML = localStorage.getItem('resultSumMonth') + " руб / год";
}
on_load();