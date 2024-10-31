function setPlan(plan) {
    const url = `/payment/add_ons/?plan=${plan}`;
    window.location.href = url;
}