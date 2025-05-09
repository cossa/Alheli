let balloon = document.querySelector("p");
let size = 1;

document.addEventListener("keydown", function(event){
    console.log(event.key);
    if (size <= 10){ 
        if(event.key === "ArrowUp"){
            inflate();
        }else if (event.key === "ArrowDown"){deflate();
    
        }

    } else {
        balloon.textContent = "💥"
    }
});

function inflate(){
    size += 1;
    balloon.style.fontSize = size + "rem";
    console.log(size);
}

function deflate(){
    size -= 0.1;
    balloon.style.fontSize = size + "rem";
}

