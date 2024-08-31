function hidden_about() {
    document.write('HEllo')
    let element = document.getElementById("hidden_text_about_payment_id");
    // if (element.isv == 'hidden'){
    //     element.style.visibility = 'visible';
    // }
    // else
    element.style.visibility = 'hidden';      // Hide

}

let hidden_element = document.getElementById("text_about_payment_id");
hidden_element.onclick(hidden_about);

function setPrice() {
    document.querySelector('.text_result_price').innerHTML = localStorage.getItem('resSumPay') + '  руб';
}
setPrice();