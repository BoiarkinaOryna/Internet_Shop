document.addEventListener(
    type = "DOMContentLoaded",
    listener = function(event){
        let listCountProducts = document.querySelectorAll('.products')
        let productCountId = document.getElementById('count-product')
        let totalPriceId = document.getElementById('total-price')
        productCountId.textContent = listCountProducts.length
        let listNumberPrices = []
        let totalPrice = 0
        
        // let listCountCount = []

        // let product = products[productPrice]
        let listProductPrices = document.querySelectorAll(".product-price")
        for(let productPrice = 0; productPrice < listProductPrices.length; productPrice++ ){
            console.log(listProductPrices[productPrice])
            // console.log("innerText =", productPrice.textContent)
            let onlyNumberPrice = Number(listProductPrices[productPrice].textContent.split(" ")[0])
            let elementId = listProductPrices[productPrice].id
            console.log("id =", elementId, document.getElementById(`quantity ${elementId}`).textContent)

            // listNumberPrices.push(onlyNumberPrice * document.getElementById(`quantity ${elementId}`).textContent)
            let quantity = Number(document.getElementById(`quantity ${elementId}`).textContent)
            let totalPriceResult = onlyNumberPrice * quantity

            listNumberPrices.push(totalPriceResult)
            totalPrice += totalPriceResult
        }
        console.log("total price:", totalPrice)
        document.getElementById("total-price").textContent = `${totalPrice} `

        let totalTotalPrice = Number(totalPrice) - 25459
        document.querySelector("#total-amount").textContent = `${totalTotalPrice} грн`
    }
)