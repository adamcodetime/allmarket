let title = document.getElementById("am-title");

const words = ["AllMarket"];
let i = 0;      // which word
let j = 0;      // which letter
let deleting = false;

function loop() {
    let current = words[i];

    if (!deleting) {
        // typing forward
        title.innerHTML = current.slice(0, j + 1);
        j++;

        if (j === current.length) {
            deleting = true;
            setTimeout(loop, 800); // pause before deleting
            return;
        }
    } else {
        // deleting backward
        title.innerHTML = current.slice(0, j - 1);
        j--;

        if (j === 0) {
            deleting = false;
            i = (i + 1) % words.length; // next word
        }
    }

    setTimeout(loop, 100); // typing speed
}

loop();
