function makeElements(){
    let container = document.querySelector("#container");

    let para = document.createElement("p");
    para.style.cssText = "color:red;";
    para.textContent ="Hey! I'm red.";
    container.appendChild(para);

    let tres = document.createElement("h3");
    tres.style.cssText = "color:blue;";
    tres.textContent ="I'm a blue h3!.";
    container.appendChild(tres);

    let divi = document.createElement("div");
    divi.style.cssText = "border:2px black solid; background-color:pink";
    container.appendChild(divi);
    let header = document.createElement("h1");
    header.style.cssText = "color:black";
    header.textContent = "I'm in a div";
    divi.appendChild(header);
    let parag = document.createElement("p");
    parag.style.cssText = "color:black";
    parag.textContent = "ME TOO!";
    divi.appendChild(parag);

    
}