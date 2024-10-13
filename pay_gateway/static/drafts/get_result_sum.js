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



myRange.onmousemove = function () {

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


});







