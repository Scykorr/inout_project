var x, i, j, l, ll, selElmnt, a, b, c, x1, l1;
/* Look for any elements with the class "custom-select": */
x = document.getElementsByClassName("custom-select");
x1 = document.getElementsByClassName("hidden_block");

l = x.length;
essential_block = document.getElementsByClassName("ess_block")

for (i = 0; i < l; i++) {
    selElmnt = x[i].getElementsByTagName("select")[0];

    ll = selElmnt.length;
    /* For each element, create a new DIV that will act as the selected item: */
    a = document.createElement("DIV");
    a.setAttribute("class", "select-selected");
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
    x1.innerHTML = a.innerHTML;
    x[i].appendChild(a);
    /* For each element, create a new DIV that will contain the option list: */
    b = document.createElement("DIV");
    b.setAttribute("class", "select-items select-hide");
    for (j = 0; j < ll; j++) {
        /* For each option in the original select element,
        create a new DIV that will act as an option item: */
        c = document.createElement("DIV");
        c.innerHTML = selElmnt.options[j].innerHTML;
        c.addEventListener("click", function (e) {
            /* When an item is clicked, update the original select box,
            and the selected item: */
            var y, i, k, s, h, sl, yl;
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
                    }
                    else if (i == 1) {
                        blocks = document.querySelectorAll('.show_1');
                        blocks.forEach(block => {
                            block.style.display = "block";
                        });
                    }
                    else if (i == 2) {
                        blocks = document.querySelectorAll('.show_2');
                        blocks.forEach(block => {
                            block.style.display = "block";
                        });
                    }


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
        essential_block.style.display = "essential_block";

    });
}

function closeAllSelect(elmnt) {
    /* A function that will close all select boxes in the document,
    except the current select box: */
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

/* If the user clicks anywhere outside the select box,
then close all select boxes: */
document.addEventListener("click", closeAllSelect);

// let select = document.getElementById('select_plan');
// let block = document.querySelectorAll('.block');
// let lastIndex = 0; // После каждой смены опции, сохраняем сюда индекс предыдущего блока
//
// select.addEventListener('change', function () {
//     block[lastIndex].style.display = "none";
//     // Чтобы сразу делать именно его невидимым при следующей смене
//
//     let index = select.selectedIndex; // Определить индекс выбранной опции
//     block[index].style.display = "block"; // Показать блок с соответствующим индексом
//
//     lastIndex = index; // Обновить сохраненный индекс.
// });