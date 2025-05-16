let headsbutton = document.querySelector("#up");
let tailsbutton = document.querySelector("#down");
let resultDiv = document.querySelector("#result");

function flip(x, y){
let coin = Math.random();
    if (coin <= 0.5){
        return("Win " + x)
    } else {
        return("Lose " + y)
    }
    
}
function flip2(x, y){
let coin = Math.random();
    if (coin <= 0.5){
        return("Win " + y)
    } else {
        return("Lose " + x)
    }
    
}

headsbutton.addEventListener("click",function() {
    flip("Heads", "Tails")
    resultDiv.textContent = flip("Heads", "Tails");

})

tailsbutton.addEventListener("click",function() {
    flip2("Heads", "Tails")
    resultDiv.textContent = flip2("Heads", "Tails");
})
