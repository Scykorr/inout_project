let myRange = document.querySelector('.range-input');
let myValue = document.querySelector('#myValue');
let off = (myRange.offsetWidth - 30) / (parseInt(myRange.max) - parseInt(myRange.min));
let px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetParent.offsetWidth / 2);

myValue.parentElement.style.left = px + 'px';
myValue.parentElement.style.top = myRange.offsetHeight + 'px';
myValue.innerHTML = myRange.value;

myRange.oninput = function () {
    let px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetWidth / 2);
    myValue.innerHTML = myRange.value;
    myValue.parentElement.style.left = px + 'px';
    document.querySelector("#price_panel_about_label_id").innerHTML = 'Итоговая цена за ' + myRange.valueAsNumber.toString() + ' пользователей';

};

var sliderEl4 = document.querySelector("#range4")
var sliderValue4 = document.querySelector(".value4")

sliderEl4.addEventListener("input", (event) => {
    var tempSliderValue = event.target.value;
    sliderValue4.textContent = tempSliderValue;

    var progress = (tempSliderValue / sliderEl4.max) * 100;

    sliderEl4.style.background = `linear-gradient(to right, #2066F1 ${progress}%, #ccc ${progress}%)`;
    document.querySelector('#price_panel_about_label_id').innerHTML = 'Итоговая цена за ' + progress.toString() + ' пользователей';
    // document.querySelector('#range_label').innerHTML = progress.toString();


})