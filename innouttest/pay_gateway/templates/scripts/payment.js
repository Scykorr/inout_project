function setPrice() {

    resultSumWithDot = (localStorage.getItem('resSumPay') + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    document.querySelector('.text_result_price').innerHTML = resultSumWithDot + '  руб';
}

setPrice();








