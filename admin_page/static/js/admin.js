let listPencilName = document.querySelectorAll(".pencil-name")
let listPencilDiscount = document.querySelectorAll(".pencil-discount")
let listPencilPrice = document.querySelectorAll(".pencil-price")
let listPencilDescription = document.querySelectorAll(".pencil-description")
let listPencilImage= document.querySelectorAll(".pencil-image")


function addListButton(classList, element) {
  for (let i = 0; i < classList.length; i++) {
      let currentElement = classList[i]
      currentElement.addEventListener(
        type = "click",
        listener = function(event){
          ChangeButton(event, element, i)
        } 
      )
  }          
}

addListButton(listPencilName, 'name')
addListButton(listPencilDiscount, 'discount')
addListButton(listPencilDescription, 'decription')
addListButton(listPencilPrice, 'price')



function ChangeButton(event, element, index){
  let listButtonPencil = []
  if (element == 'name'){
    listButtonPencil = listPencilName
  }
  else if (element == 'discount'){
    listButtonPencil = listPencilDiscount
  }
  else if (element == 'description'){
    listButtonPencil = listPencilDescription
  }
  else if (element == 'price'){
    listButtonPencil = listPencilPrice
  }

  idPencil = listButtonPencil[index].id
  console.log(listButtonPencil[index].id)
  let input = document.createElement("input")
  input.classList.add(`${element}-input`)
  input.id = idPencil
  console.log(input)
  let button = document.createElement("button")
  button.textContent = "OK"
  button.id = idPencil
  button.classList.add(`${element}-button`)
  document.body.append(input, button)
  console.log(button)
  button.addEventListener(
      type = "click",
      listener = function(event) {
          let newValue = input.value
          let elementValue = document.getElementById(`${element}-${idPencil}`)
          console.log(elementValue, `${element}-${idPencil}`)
          // elementValue.textContent = newValue
          // console.log(newValue)
          // input.remove()
          // button.remove() 
          if(newValue){
            elementValue.textContent = newValue
            console.log(newValue)
            input.remove()
            button.remove() 
          }
          else{
            newValue = elementValue.textContent
            input.remove()
            button.remove() 
          }
      }
  )
}



