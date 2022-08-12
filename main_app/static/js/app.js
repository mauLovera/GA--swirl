// song = document.getElementById('song')
// play = document.getElementById('play')
// count = document.getElementById('count')

let picture = document.querySelector(".details-image-container")

let pictureUrlExtract = picture.style.backgroundImage
let pictureUrlSplit1 = pictureUrlExtract.split('url("').join("")
let pictureUrlSplit2 = pictureUrlSplit1.split('")')
let pictureUrl = pictureUrlSplit2[0]

Vibrant.from(pictureUrl)
  .getPalette()
  .then((palette) => {
    // console.log(palette)
    let darkRgb = palette.DarkMuted._rgb
    let lightRgb = palette.LightMuted._rgb
    let darkRgbBG = `rgb(${darkRgb[0]} ${darkRgb[1]} ${darkRgb[2]})`
    let lightRgbBG = `rgb(${lightRgb[0]} ${lightRgb[1]} ${lightRgb[2]})`

    let banner = document.querySelector(".details-banner")
    let add = document.querySelector(".details-add-song-button")
    let cancel = document.querySelector(".details-cancel-song-button")
    let addForm = document.querySelectorAll(".details-add-song-form")
    let modal = document.querySelector(".details-add-song-modal")
    let editButton = document.querySelectorAll(".details-song-details")

    add.addEventListener("click", () => {
      modal.classList.toggle("invisible")
    })

    cancel.addEventListener("click", () => {
      modal.classList.toggle("invisible")
    })

    if (editButton) {
      editButton.forEach((button) => {
        button.addEventListener("click", () => {
        
        })
      })
    }

    banner.style.background = darkRgbBG
    add.style.background = darkRgbBG
    addForm.forEach(form => form.style.background = darkRgbBG)
  })
