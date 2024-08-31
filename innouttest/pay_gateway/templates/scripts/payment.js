function hidden_about() {
    element.style.visibility = 'hidden';      // Hide
    element.style.visibility = 'visible';

}

function setPrice() {
    document.querySelector('.text_result_price').innerHTML = localStorage.getItem('resSumPay') + '  руб';
}
setPrice();