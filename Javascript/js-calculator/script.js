let num1Input = document.querySelector("#num1");
console.log(num1.value);
let num2Input = document.querySelector("#num2");

let plusbutton = document.querySelector("#plus");
let minusbutton = document.querySelector("#minus");
let multiplybutton = document.querySelector("#mult");
let divisionbutton = document.querySelector("#divi");

let resultDiv = document.querySelector("#result")

function addition(x,y){
    console.log(x + y);
    return x + y;
}

plusbutton.addEventListener("click", function () {
    let num1 =parseFloat(num1Input.value);
    let num2 = parseFloat(num2Input.value);
    resultDiv.textContent = addition(num1,num2);
});

function minus(x,y){
    console.log(x - y);
    return x - y;
}

minusbutton.addEventListener("click", function () {
    let num1 =parseFloat(num1Input.value);
    let num2 = parseFloat(num2Input.value);
    resultDiv.textContent = minus(num1,num2);
});

function multiply(x,y){
    console.log(x * y);
    return x * y;
}

multiplybutton.addEventListener("click", function () {
    let num1 =parseFloat(num1Input.value);
    let num2 = parseFloat(num2Input.value);
    resultDiv.textContent = multiply(num1,num2);
});

function division(x,y){
    console.log(x / y);
    return x / y;
}

divisionbutton.addEventListener("click", function () {
    let num1 =parseFloat(num1Input.value);
    let num2 = parseFloat(num2Input.value);
    resultDiv.textContent = division(num1,num2);
});




