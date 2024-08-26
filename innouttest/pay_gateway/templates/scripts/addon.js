function getCheckedCheckBoxes() {
    let resultSum, planPrice;
    resultSum = 0;
    let x12 = document.getElementsByClassName("hidden_block");
    let s11;
    let s14;
    let peopleAmount = document.getElementById("value_range");
    s11 = x12.innerHTML;
    peopleAmount = Number(peopleAmount.innerHTML.toString());

    localStorage.setItem('userAmount', peopleAmount.toString());

    if (s11 == "INOUT Проект База") {
        resultSum += 590 * peopleAmount;
    } else if (s11 == "INOUT Проект Бизнес") {
        resultSum += 1190 * peopleAmount;
    } else if (s11 == "INOUT Проект Платформа") {
        resultSum += 2390 * peopleAmount;
    }

    let checkboxHelpDesk = document.getElementById("help_desk")
    if (checkboxHelpDesk.checked) {
        resultSum += 490 * peopleAmount;
    }
    let checkboxDms = document.getElementById("basic_dms")
    if (checkboxDms.checked) {
        resultSum += 190 * peopleAmount;
    }
    let checkboxRisk = document.getElementById("risk_management")
    if (checkboxRisk.checked) {
        resultSum += 190 * peopleAmount;
    }
    let checkboxBrand = document.getElementById("custom_branding")
    if (checkboxBrand.checked) {
        resultSum += 90 * peopleAmount;
    }
    let checkboxGit = document.getElementById("gitlab_integration")
    if (checkboxGit.checked) {
        resultSum += 190 * peopleAmount;
    }
    let checkboxB2b = document.getElementById("b2b_crm")
    if (checkboxB2b.checked) {
        resultSum += 890 * peopleAmount;
    }
    let checkboxBase = document.getElementById("knowledge_base")
    if (checkboxBase.checked) {
        resultSum += 390 * peopleAmount;
    }
    let checkboxManage = document.getElementById("asset_config")
    if (checkboxManage.checked) {
        resultSum += 290 * peopleAmount;
    }
    let checkboxCloud = document.getElementById("private_cloud")
    if (checkboxCloud.checked) {
        resultSum += 39000 * peopleAmount;
    }

    let radioYear = document.getElementById("in_year")
    if (radioYear.checked) {
        resultSum *= 0.85;
    }
    let radioMonth = document.getElementById("in_month")
    if (radioMonth.checked) {
        resultSum += 0;
    }


    let resultSumYear = Math.round(resultSum);
    let resultSumMonth = Math.round(resultSum / 12);

    localStorage.setItem('resultSumYear', resultSumYear.toString())
    localStorage.setItem('resultSumMonth', resultSumMonth.toString())

    resultSumInYear = (resultSumYear + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    resultSumInMonth = (resultSumMonth + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    // document.write(resultSumInYear)
    document.querySelector('#price_in_year_label_id').innerHTML = resultSumInYear + '  руб / год';
    document.querySelector('#price_in_year_month_id').innerHTML = '( ' + resultSumInMonth + ' руб / месяц )';
}


function test_onload() {
    let plan_text = localStorage.getItem('plan');
    let x12 = document.getElementsByClassName("hidden_block");
    x12.innerHTML = plan_text;
    getCheckedCheckBoxes();
    let blocks = document.querySelectorAll('.show');
    blocks.forEach(block => {
        block.style.display = "none";
    });
    if (plan_text == "INOUT Проект База") {
        blocks = document.querySelectorAll('.show_0');
        blocks.forEach(block => {
            block.style.display = "block";

        });
    } else if (plan_text == "INOUT Проект Бизнес") {
        blocks = document.querySelectorAll('.show_1');
        blocks.forEach(block => {
            block.style.display = "block";

        });
    } else if (plan_text == "INOUT Проект Платформа") {
        blocks = document.querySelectorAll('.show_2');
        blocks.forEach(block => {
            block.style.display = "block";

        });
    }
}


var x, i, j, l, ll, selElmnt, a, b, c;
/* ищем любой элемент с классом "custom-select" */
x = document.getElementsByClassName("custom-select");
const x1 = document.getElementsByClassName("hidden_block");
l = x.length;
for (i = 0; i < l; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    ll = selElmnt.length;
    /* для каждого элемента создаем новый элемент DIV, который будет работать как элемент выбора */
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    // a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    a.innerHTML = localStorage.getItem('plan');
    x[i].appendChild(a);
    /* для каждого элемента создаем новый элемент DIV, который будет содержать список опций */
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j = 0; j < ll; j++) {
        /* для каждой опции в оригинальном выпадающем списке
        создаем новый элемент DIV, который будет работать как опция */
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function (e) {
            /* когда на элемент кликают, обновляем оригинальный выпадающий список
            и выбранный элемент */
            var y, i, k, s, h, sl, yl;
            s = this.parentNode.parentNode.getElementsByTagName("select")[0];
            sl = s.length;
            h = this.parentNode.previousSibling;

            let blocks = document.querySelectorAll('.show');
            // скрываем их
            blocks.forEach(block => {
                block.style.display = "none";
            });
            document.getElementById("help_desk").checked = false;
            document.getElementById("basic_dms").checked = false;
            document.getElementById("risk_management").checked = false;
            document.getElementById("custom_branding").checked = false;
            document.getElementById("gitlab_integration").checked = false;
            document.getElementById("b2b_crm").checked = false;
            document.getElementById("knowledge_base").checked = false;
            document.getElementById("asset_config").checked = false;
            document.getElementById("private_cloud").checked = false;
            for (i = 0; i < sl; i++) {
                if (s.options[i].innerHTML == this.innerHTML) {
                    s.selectedIndex = i;
                    h.innerHTML = this.innerHTML;
                    y = this.parentNode.getElementsByClassName("same-as-selected");
                    yl = y.length;
                    x1.innerHTML = this.innerHTML;
                    if (i == 0) {
                        blocks = document.querySelectorAll('.show_0');
                        blocks.forEach(block => {
                            block.style.display = "block";
                        });
                    } else if (i == 1) {
                        blocks = document.querySelectorAll('.show_1');
                        blocks.forEach(block => {
                            block.style.display = "block";
                        });
                    } else if (i == 2) {
                        blocks = document.querySelectorAll('.show_2');
                        blocks.forEach(block => {
                            block.style.display = "block";
                        });
                    }
                    getCheckedCheckBoxes()
                    for (k = 0; k < yl; k++) {
                        y[k].removeAttribute("class");
                    }
                    this.setAttribute("class", "same-as-selected");
                    break;
                }
            }
            h.click();
        });
        b.appendChild(c);
    }
    x[i].appendChild(b);
    a.addEventListener("click", function (e) {
        /* когда на выпадающий список кликают, закрываем другие элементы выбора
        и открываем/закрываем текущий элемент выбора */
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
    });
}


function closeAllSelect(elmnt) {
    /* функция, которая закрывает все элементы выбора в документе
    кроме текущего */
    var x, y, i, xl, yl, arrNo = [];
    x = document.getElementsByClassName("select-items");
    y = document.getElementsByClassName("select-selected");
    xl = x.length;
    yl = y.length;
    for (i = 0; i < yl; i++) {
        if (elmnt == y[i]) {
            arrNo.push(i)
        } else {
            y[i].classList.remove("select-arrow-active");
        }
    }
    for (i = 0; i < xl; i++) {
        if (arrNo.indexOf(i)) {
            x[i].classList.add("select-hide");
        }
    }
}

/* если пользователь кликает за пределами выпадающего списка,
то все элементы выбора закрываются */
function closeAllSelectCustomAddons() {
    document.addEventListener("click", closeAllSelect);
}


let myRange = document.querySelector('.range-input');
let myValue = document.querySelector('#myValue');
let off = (myRange.offsetWidth - 30) / (parseInt(myRange.max) - parseInt(myRange.min));
let px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetParent.offsetWidth / 2);

myValue.parentElement.style.left = px + 11 + 'px';
myValue.parentElement.style.top = myRange.offsetHeight + 'px';
myValue.innerHTML = myRange.value;

myRange.oninput = function () {
    let px = ((myRange.valueAsNumber + 2 - parseInt(myRange.min)) * off) - ((myValue.offsetWidth - 5) / 2);
    myValue.innerHTML = myRange.value;
    myValue.parentElement.style.left = px + 'px';
    getCheckedCheckBoxes()
    // document.querySelector("#price_panel_about_label_id").innerHTML = 'Итоговая цена за ' + myRange.valueAsNumber.toString() + ' пользователей';

};

var sliderEl4 = document.querySelector("#range4")
var sliderValue4 = document.querySelector(".value4")

sliderEl4.addEventListener("input", (event) => {
    var tempSliderValue = event.target.value;
    sliderValue4.textContent = tempSliderValue;

    var progress = (tempSliderValue / sliderEl4.max) * 100;

    sliderEl4.style.background = `linear-gradient(to right, #2066F1 ${progress}%, #ccc ${progress}%)`;
    document.querySelector('#price_panel_about_label_id').innerHTML = 'Итоговая цена за ' + progress.toString() + ' пользователей';
    getCheckedCheckBoxes();
    // document.querySelector('#range_label').innerHTML = progress.toString();


})

let resultSum, checkboxHelpDesk, checkboxDms,
    checkboxRisk, checkboxBrand, checkboxGit,
    checkboxB2b, checkboxBase, checkboxManage,
    checkboxCloud, redioYear, radioMonth;
resultSum = 0;
checkboxHelpDesk = document.getElementById("help_desk")
checkboxDms = document.getElementById("basic_dms")
checkboxRisk = document.getElementById("risk_management")
checkboxBrand = document.getElementById("custom_branding")
checkboxGit = document.getElementById("gitlab_integration")
checkboxB2b = document.getElementById("b2b_crm")
checkboxBase = document.getElementById("knowledge_base")
checkboxManage = document.getElementById("asset_config")
checkboxCloud = document.getElementById("private_cloud")
redioYear = document.getElementById("in_year")
radioMonth = document.getElementById("in_month")

checkboxHelpDesk.addEventListener('change', (event) => {
    getCheckedCheckBoxes();
})
checkboxDms.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxRisk.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxBrand.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxGit.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxB2b.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxBase.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxManage.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
checkboxCloud.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
redioYear.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})
radioMonth.addEventListener('change', (event) => {
    getCheckedCheckBoxes()
})


test_onload();


