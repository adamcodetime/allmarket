let title = document.getElementById("am-title");
let title_state = false;
setInterval(function() {
    if (title_state == false) {
        title.innerHTML = "Facebook";
    } else if (title_state == true) {
        title.innerHTML = "AllMarket";
    }
    title_state = !title_state;
}, 2000)