

function loadPizza(id){
    fetch('/api/v1/pizza/'+id)
    .then(response => response.json())
    .then(pizza => {
        let menu_panel = document.getElementById('selected-pizza');
        p = new Pizza(pizza)
        console.log(p.name)
        menu_panel.appendChild(p.toElement())
    })
    .catch(error => console.log('Error' + error))
}

