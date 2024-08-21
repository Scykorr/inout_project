const sliderEl4 = document.querySelector("#range4")
const sliderValue4 = document.querySelector(".value4")


sliderEl4.addEventListener("input", (event) => {
    const tempSliderValue = event.target.value;
    sliderValue4.textContent = tempSliderValue;

    const progress = (tempSliderValue / sliderEl4.max) * 100;

    sliderEl4.style.background = `linear-gradient(to right, #2066F1 ${progress}%, #ccc ${progress}%)`;
    // document.querySelector('#price_panel_about_label_id').innerHTML = 'Итоговая цена за ' + progress.toString() + ' пользователей';
    document.querySelector('#range_label').innerHTML = progress.toString();


})








