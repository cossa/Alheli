let submit = document.querySelector("input[type=submit]");

let fname = document.querySelector("input[name=fname]");
let lname = document.querySelector("input[name=lname]");
let email = document.querySelector("input[name=email]");
let birth = document.querySelector("input[name=birth]");
let age = document.querySelector("input[name=age]");
let country = document.querySelector("input[name=country]");
let gender = document.querySelector("input[name=gender]");
let color = document.querySelector("input[name=color]");
let npassword = document.querySelector("input[name=npassword]");






submit.addEventListener("click", printInfo);

function printInfo(){
    
    console.log(fname.value + lname.value + email.value + birth.value + age.value + country.value + gender.value + color.value + npassword.value)
}
