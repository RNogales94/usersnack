

class Pizza {
    constructor(obj){
        this.id = obj.id;
        this.name = obj.name;
        this.price = obj.price;
        this.ingredients = obj.ingredients;
        this.img = obj.img;
    }

    toHTML(){

        return `<div class="card">
                  <div class="card-image">
                    <figure class="image is-4by3">
                      <img src=${"/static/images/"+this.img} alt="Pizza image">
                    </figure>
                  </div>
                  <div class="card-content">
                    <div class="media">
                      <div class="media-content">
                        <p class="title is-4">${this.name}</p>
                        <p class="subtitle is-6">${this.ingredients}</p>
                        <span class="tag is-success is-medium">USD ${this.price}</span>
                      </div>
                    </div>
                  </div>
                </div>`
    }

    toElement(){
        return htmlToElement(this.toHTML())
    }
}