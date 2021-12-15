window.onload = function () {
    setInterval('letsound()',100)
}
function letsound() {
    var music = document.getElementById('mc');
    if(music.paused){
        music.paused = false;
        music.play();
    }
    
}