function getCheckedCheckBoxes() {
    let resultSum, checkboxHelpDesk, checkboxDms,
        checkboxRisk, checkboxBrand, checkboxGit,
        checkboxB2b, checkboxBase, checkboxManage,
        checkboxCloud, radioYear, radioMonth, resultSumInYear,
        resultSumInMonth, rangeUserAmount, planPrice;
    resultSum = 0;

    rangeUserAmount = document.getElementById("value_range").innerHTML;
    let numUserAmount = parseInt(rangeUserAmount);

    let x11 = document.getElementsByClassName("hidden_block");
    let s11;
    s11 = x11.innerHTML.toString();
    if (s11 == "INOUT Проект Essentials") {
        planPrice = 590 * numUserAmount;
    } else if (s11 == "INOUT Проект Business") {
        planPrice = 1190 * numUserAmount;
    } else if (s11 == "INOUT Проект Platform") {
        planPrice = 2390 * numUserAmount;
    }


    // let aboutPrice = document.getElementById("price_panel_about_label_id")
    // aboutPrice.innerHTML = 'Итоговая цена за ' + numUserAmount.toString() + ' пользователей';
    checkboxHelpDesk = document.getElementById("help_desk")
    if (checkboxHelpDesk.checked) {
        resultSum += 490 * numUserAmount;
    }
    checkboxDms = document.getElementById("basic_dms")
    if (checkboxDms.checked) {
        resultSum += 190 * numUserAmount;
    }
    checkboxRisk = document.getElementById("risk_management")
    if (checkboxRisk.checked) {
        resultSum += 190 * numUserAmount;
    }
    checkboxBrand = document.getElementById("custom_branding")
    if (checkboxBrand.checked) {
        resultSum += 90 * numUserAmount;
    }
    checkboxGit = document.getElementById("gitlab_integration")
    if (checkboxGit.checked) {
        resultSum += 190 * numUserAmount;
    }
    checkboxB2b = document.getElementById("b2b_crm")
    if (checkboxB2b.checked) {
        resultSum += 890 * numUserAmount;
    }
    checkboxBase = document.getElementById("knowledge_base")
    if (checkboxBase.checked) {
        resultSum += 390 * numUserAmount;
    }
    checkboxManage = document.getElementById("asset_config")
    if (checkboxManage.checked) {
        resultSum += 290 * numUserAmount;
    }
    checkboxCloud = document.getElementById("private_cloud")
    if (checkboxCloud.checked) {
        resultSum += 39000 * numUserAmount;
    }


    if (!isNaN(planPrice)) {
        resultSum += planPrice;
    }
    radioYear = document.getElementById("in_year")
    if (radioYear.checked) {
        resultSum *= 0.85;
    }
    radioMonth = document.getElementById("in_month")
    if (radioMonth.checked) {
        resultSum += 0;
    }

    let resultSumYear = Math.round(resultSum);
    let resultSumMonth = Math.round(resultSum / 12);
    resultSumInYear = (resultSumYear + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    resultSumInMonth = (resultSumMonth + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    // document.write(resultSumInYear)
    document.querySelector('#price_in_year_label_id').innerHTML = resultSumInYear + '  руб / год';
    document.querySelector('#price_in_year_month_id').innerHTML = '( ' + resultSumInMonth + ' руб / месяц )';
    return resultSum

}

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

const myRange = document.querySelector('.range-input');
const myValue = document.querySelector('#myValue');
const off = (myRange.offsetWidth - 30) / (parseInt(myRange.max) - parseInt(myRange.min));
const px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetParent.offsetWidth / 2);

myValue.parentElement.style.left = px + 'px';
myValue.parentElement.style.top = myRange.offsetHeight + 'px';
myValue.innerHTML = myRange.value;

myRange.oninput = function () {
    let px = ((myRange.valueAsNumber - parseInt(myRange.min)) * off) - (myValue.offsetWidth / 2);
    myValue.innerHTML = myRange.value;
    myValue.parentElement.style.left = px + 'px';
    document.querySelector("#price_panel_about_label_id").innerHTML = 'Итоговая цена за ' + myRange.valueAsNumber.toString() + ' пользователей';

};

myRange.onmousemove = function () {
    let res_sum = getCheckedCheckBoxes();

    let resultSumYear = Math.round(res_sum);
    let resultSumMonth = Math.round(res_sum / 12);
    let resultSumInYear = (resultSumYear + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    let resultSumInMonth = (resultSumMonth + '').replace(/(\d)(?=(\d\d\d)+([^\d]|$))/g, '$1.');
    document.querySelector('#price_in_year_label_id').innerHTML = resultSumInYear + '  руб / год';
    document.querySelector('#price_in_year_month_id').innerHTML = '( ' + resultSumInMonth + ' руб / месяц )';
};


window.addEventListener('load', () => {
    let blocks = document.querySelectorAll('.show');
    // скрываем их
    blocks.forEach(block => {
        block.style.display = "none";
    });

    blocks = document.querySelectorAll('.show_0');
    blocks.forEach(block => {
        block.style.display = "block";

    });
    // Check
    document.getElementById("basic_dms").checked = true;

// Uncheck
    document.getElementById("basic_dms").checked = false;

    x1.innerHTML = "INOUT Проект Platform";
    getCheckedCheckBoxes()


});


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



let x, i, j, l, ll, selElmnt, a, b, c, l1;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
 var x1 = document.getElementsByClassName("hidden_block");

l = x.length;
// essential_block = document.getElementsByClassName("ess_block")

for (i = 0; i < l; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];
    ll = selElmnt.length;
    /* For each element, create a new DIV that will act as the selected item: */
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    // x1.innerHTML = a.innerHTML;
    x[i].appendChild(a);
    /* For each element, create a new DIV that will contain the option list: */
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j = 0; j < ll; j++) {
        /* For each option in the original select element,
        create a new DIV that will act as an option item: */
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        getCheckedCheckBoxes()
        c.addEventListener("click", function (e) {
            /* When an item is clicked, update the original select box,
            and the selected item: */
            let y, i, k, s, h, sl, yl;
            s = this.parentNode.parentNode.getElementsByTagName("select")[0];
            sl = s.length;
            h = this.parentNode.previousSibling;

            let blocks = document.querySelectorAll('.show');
            // скрываем их
            blocks.forEach(block => {
                block.style.display = "none";
            });

            for (i = 0; i < sl; i++) {
                if (s.options[i].innerHTML == this.innerHTML) {
                    s.selectedIndex = i;
                    h.innerHTML = this.innerHTML;
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
                    document.getElementById("help_desk").checked = false;
                    document.getElementById("basic_dms").checked = false;
                    document.getElementById("risk_management").checked = false;
                    document.getElementById("custom_branding").checked = false;
                    document.getElementById("gitlab_integration").checked = false;
                    document.getElementById("b2b_crm").checked = false;
                    document.getElementById("knowledge_base").checked = false;
                    document.getElementById("asset_config").checked = false;
                    document.getElementById("private_cloud").checked = false;

                    y = this.parentNode.getElementsByClassName("same-as-selected");
                    yl = y.length;
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
        /* When the select box is clicked, close any other select boxes,
        and open/close the current select box: */
        e.stopPropagation();
        closeAllSelect(this);
        this.nextSibling.classList.toggle("select-hide");
        this.classList.toggle("select-arrow-active");
        // essential_block.style.display = "essential_block";
        x1.innerHTML = this.innerHTML;
    });
}

function closeAllSelect(elmnt) {
    /* A function that will close all select boxes in the document,
    except the current select box: */
    let x, y, i, xl, yl, arrNo = [];
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

document.addEventListener("click", closeAllSelect);

