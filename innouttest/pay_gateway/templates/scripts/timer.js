const curr_date = new Date();
curr_date.setMinutes(curr_date.getMinutes() + 10);

// const endTime = new Date(`2024-11-16T04:25:03Z`).getTime();
const endTime = curr_date;
const timer = setInterval(() => {
    const now = new Date().getTime();
    const remaining = endTime - now;

    // const days = Math.floor(remaining / (24 * 60 * 60 * 1000));
    // const hours = Math.floor((remaining % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000));
    const mins = Math.floor((remaining % (60 * 60 * 1000)) / (60 * 1000));
    const secs = Math.floor((remaining % (60 * 1000)) / 1000);

    document.getElementById("demo").textContent = `${mins}:${secs}`;

    if (remaining < 0) {
        clearInterval(timer);
        document.getElementById("demo").textContent = "Время истекло";
        window.open("http://localhost:63342/innout_project/pay_gateway/templates/unsuccess_paymant.html?_ijt=83sb65rc7pupgchu5ov318rdfl", name='_self')
    }
}, 1000);


// document.addEventListener('visibilitychange', () => {
//     if (document.hidden) {
//         timer.pause();
//     } else {
//         timer.resume();
//     }
// });