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


});