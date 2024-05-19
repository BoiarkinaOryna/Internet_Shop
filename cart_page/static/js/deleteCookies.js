const listButtonsMinus = document.querySelectorAll(".minus")

for (let count = 0; count < listButtonsMinus.length; count++){
  let button = listButtonsMinus[count]
  button.addEventListener(
    type = "click",
    listener = (event) =>{
      let listIdProducts = document.cookie.split("=")[1].split(" ")

      for(let index = 0; index < listIdProducts.length; index){
          if (listIdProducts[index] == button.id){
            listIdProducts.splice(index, 1)
            break
          }
      if(listIdProducts.length > 0){
        document.cookie = `product = ${listIdProducts.join(" ")}; path = /`

      }
      button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1
       
      if(button.nextElementSibling.textContent == 0){
        document.querySelector(`#product-${button.id}`).remove()
      }

      if (document.cookie.split('=')[1] == ''){
        let p = document.createElement("p");
        p.textContent = "Корзина порожня";
        document.body.append(p)
      }
      
      }
    }
  )
}

const listButtonPlus = document.querySelectorAll(".plus")

for(let count = 0; count < listButtonPlus; count++){
    let button = listButtonPlus[count]
    button.addEventListener(
      type = "click",
      listener = (event) =>{
        let listIdProducts = document.cookie.split("=")[1].split(" ")
        listIdProducts.push(button.id.split("=")[1])
        document.cookie = `product=${listIdProducts.join(" ")}; path = /`
        button.nextElementSibling.textContent = Number(button.previousElementSibling.textContent) + 1
      }
    )
}
