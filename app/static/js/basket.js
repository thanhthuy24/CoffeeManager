function addToBasket(id, name, price, image){
    fetch('/api/basket',{
        method: "post",
        body: JSON.stringify({
            "id": id,
            "name": name,
            "price": price,
            "image": image
        }), headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res){
        return res.json()
    }).then(function(data){
        let items = document.getElementsByClassName('basket-counter');
        for (let item of items)
            item.innerText = data.total_quantity;
    });
}