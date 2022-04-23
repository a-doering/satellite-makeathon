let showIn = function(event) {
    let image = document.getElementById('inImg');
    console.log(event)
    image.src = URL.createObjectURL(event.target.files[0]);
};

console.log(document)
let showOut = function() {
    wait(1500)
    document.getElementById('outImg').style.visibility = 'visible';
}

let wait = function(ms) {
    var start = new Date().getTime();
    var end = start;
    while (end < start + ms) {
        end = new Date().getTime();
    }
}