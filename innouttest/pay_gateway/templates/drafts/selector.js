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
    a.innerHTML = selElmnt.options[selElmnt.selectedIndex].innerHTML;
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
document.addEventListener("click", closeAllSelect);
