const button_element = document.getElementById("button_element");
const date_of_birth = document.getElementById("birth");
const age = document.getElementById("age");

function age_calculator() {
    const birthday_value = date_of_birth.value;
    if (birthday_value == ""){
        alert("Please Enter Your birthday")
    }
    else {
        const fin_age = getAge(birthday_value);
        age.innerText = `Your age is ${fin_age} ${fin_age >1 ? "years" : "year"} old`;
    }
}
function getAge(birthday_value){
    const current_date = new Date();
    const birthday_date = new Date(birthday_value);
    let age = current_date.getFullYear() - birthday_date.getFullYear();
    const month = current_date.getMonth() - birthday_date.getMonth();
    if (month < 0 || (month === 0 && current_date.getDate() < birthday_date.getDate())){
        age--;
    }  
    return age;
}

button_element.addEventListener("click", age_calculator);