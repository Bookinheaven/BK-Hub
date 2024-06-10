const button_element = document.getElementById("calculate");
const bill_input = document.getElementById("bill");
const tip_input = document.getElementById("tip");
const total_output = document.getElementById("total");

function calculatetotal(){
    const bill_value = bill_input.value;
    const tip_value = tip_input.value;
    const total_value = bill_value * ( 1 + tip_value / 100);
    total_output.innerText = total_value.toFixed(2);
}

button_element.addEventListener("click", calculatetotal);
