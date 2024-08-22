// document.querySelectorAll('.range_box input').forEach(item => {
//
//     item.addEventListener('mousemove', function () {
//
//         this.closest('.range_box').querySelector('.rangeValue').innerHTML = this.value;
//     })
//
// });


const boxes = document.querySelectorAll('.box');
if (boxes.length) {
   boxes.forEach(box => box.addEventListener('click', myBoxClickHandler));
} else {
  console.log('These aren\'t the boxes you\'re looking for.');
   // на самом деле вся ветка 'else' не нужна
}