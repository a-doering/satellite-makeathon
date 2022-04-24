let modals = document.getElementsByClassName('modals')
let modalBtns = document.getElementsByClassName('modalBtns')
let closeSpans = document.getElementsByClassName('close')

for (let modalBtn of modalBtns) {
    modalBtn.onclick = function() {
        let modalId = modalBtn.dataset.modal
        let modal = document.getElementById(modalId)
        modal.style.display = "block";
    }
}

for (let span of closeSpans) {
    span.onclick = function() {
        let modalId = span.dataset.modal
        let modal = document.getElementById(modalId)
        modal.style.display = "none";
    }
}

let showIn = function() {
    wait(1000)
    document.getElementById('inImg').style.visibility = 'visible';
};

let showOut = function() {
    document.getElementById('wait').style.visibility = 'visible';
    document.getElementById('loading').style.visibility = 'visible';
    setTimeout(load, 2000);
}

let load = function() {
    document.getElementById('wait').style.visibility = 'hidden';
    document.getElementById('loading').style.visibility = 'hidden';
    document.getElementById('arrow').style.visibility = 'visible';
    document.getElementById('outImg').style.visibility = 'visible';
    document.getElementById('legend').style.visibility = 'visible';
}

let wait = function(ms) {
    var start = new Date().getTime();
    var end = start;
    while (end < start + ms) {
        end = new Date().getTime();
    }
}
