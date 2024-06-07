let listPencilName = document.querySelectorAll(".pencil-name")
let listPencilDiscount = document.querySelectorAll(".pencil-discount")
let listPencilPrice = document.querySelectorAll(".pencil-price")
let listPencilDescription = document.querySelectorAll(".pencil-description")
let listPencilImage= document.querySelectorAll(".pencil-image")
let myForm = document.querySelector(".form")

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
  console.log(myForm)
  myForm.append(input)
  document.querySelector('.modal-window').style.display = 'flex'
  let button = document.querySelector(".name-button")
  button.id = idPencil
  button.style.display = "flex"
  button.addEventListener(
      type = "click",
      listener = function(event) {
          let newValue = input.value
          let elementValue = document.getElementById(`${element}-${idPencil}`)
          console.log(elementValue, `${element}-${idPencil}`)
          button.value = newValue + "^" + button.id + "^" + element
          elementValue.textContent = newValue
          console.log(newValue)
          input.remove()
          button.style.display = none 
          // if(newValue){
          //   elementValue.textContent = newValue
          //   input.remove()
          // }
          // else{
          //   newValue = elementValue.textContent
          //   input.remove()
          // }
      }
  )
}