

function loadPizzas(){
    fetch('https://rnog-usersnack.herokuapp.com/api/v1/pizzas')
    .then(response => response.json())
    .then(pizzas => {
        let menu_panel = document.getElementById('pizzas-section');
        for (pizza of pizzas){
            p = new Pizza(pizza)
            console.log(p.name)
            menu_panel.appendChild(p.toElement())
        }
    })
    .catch(error => console.log('Error' + error))
}

loadPizzas();