function on_load() {
    document.querySelector('.plan_and_users').innerHTML = localStorage.getItem('plan') + " - " + localStorage.getItem('userAmount') + " пользователей";
    let resultSumYear = (localStorage.getItem('resultSumYear') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    let resultSumMonth = (localStorage.getItem('resultSumMonth') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    document.querySelector('.price_per_month').innerHTML = "(" + resultSumMonth + " руб / месяц)";
    document.querySelector('.price_per_year').innerHTML = resultSumYear + " руб / год";
    document.querySelector('#price_per_month_2').innerHTML = resultSumMonth + " руб / месяц";
}
on_load();