document.addEventListener(
    type = "DOMContentLoaded",
    listener = (event) =>{
        let totalAmount = 0
        let listProductPrice = document.querySelectorAll(".waiting-product-price")
        for (let ProductPrice of listProductPrice){
            totalAmount += Number(ProductPrice.innerText.split(" ")[0])
            // console.log()
        }
        console.log("totalAmount =", totalAmount)
        document.querySelector(".waiting-total-amount").textContent = `${totalAmount} грн`
    }
)