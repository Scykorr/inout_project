var myRange = document.querySelector('.range-input');
var myValue = document.querySelector('#myValue');
var off = myRange.offsetWidth / (parseInt(myRange.max) - parseInt(myRange.min));
var px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetParent.offsetWidth / 2);

myValue.parentElement.style.left = px + 'px';
myValue.parentElement.style.top = myRange.offsetHeight + 'px';
myValue.innerHTML = myRange.value;

myRange.oninput = function () {
    let px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetWidth / 2);
    myValue.innerHTML = myRange.value;
    myValue.parentElement.style.left = px + 'px';
};