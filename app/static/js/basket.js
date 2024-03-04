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

function updateBasket(id, obj){
    obj.disabled = true;
    fetch(`/api/basket/${id}`,{
        method: "put",
        body: JSON.stringify({
            "quantity": obj.value
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res){
        return res.json();
    }).then(function(data){
        obj.disabled = false;
        let items = document.getElementsByClassName('basket-counter');
        for (let item of items)
            item.innerText = data.total_quantity;

        let totals = document.getElementsByClassName('basket-total');
        for (let t of totals)
            t.innerText = data.total_amount;

        let tax = document.getElementsByClassName('basket-tax');
        for (let t of tax)
            t.innerText = data.tax_basket;

        let basketsum = document.getElementsByClassName('basket-total-all');
        for (let t of basketsum)
            t.innerText = data.total_basket;
    })
}

function deleteBasket(id, obj){
    if (confirm("Ban chac chan xoa?") == true){
        fetch(`/api/basket/${id}`,{
            method: "delete"
        }).then(function(res){
            return res.json();
        }).then(function(data){
            obj.disabled = false;
            let items = document.getElementsByClassName('basket-counter');
            for (let item of items)
                item.innerText = data.total_quantity;

            let d = document.getElementById(`product${id}`);
            d.style.display = "none";
        });
    }
}

function payCOD(){
    if(confirm("Bạn có chắc xác nhận đặt hàng? ") === true){
        fetch("/api/payCOD", {
            method: "post"
        }).then(res => res.json()).then(data => {
            if(data.status === 200){
                location.reload();
            }
            else {
                alert(data.err_msg)
            }
        })
    }
}
