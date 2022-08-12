let picture = document.querySelector(".details-image-container")
let pictureUrlExtract = picture.style.backgroundImage
let pictureUrlSplit1 = pictureUrlExtract.split('url("').join("")
let pictureUrlSplit2 = pictureUrlSplit1.split('")')
let pictureUrl = pictureUrlSplit2[0]

Vibrant.from(pictureUrl)
  .getPalette()
  .then((palette) => {
    console.log(palette)
    let darkRgb = palette.DarkMuted._rgb
    let lightRgb = palette.LightMuted._rgb  
    let darkRgbBG = `rgb(${darkRgb[0]} ${darkRgb[1]} ${darkRgb[2]})`
    let lightRgbBG = `rgb(${lightRgb[0]} ${lightRgb[1]} ${lightRgb[2]})`

    let input = document.querySelectorAll("input")
    let link = document.querySelectorAll(".link")
    let song = document.querySelectorAll(".song")
    let banner = document.querySelector(".details-banner")
    let add = document.querySelector(".details-add-song-button")
    let cancel = document.querySelector(".details-cancel-song-button")
    let addForm = document.querySelectorAll(".details-add-song-form")
    let modal = document.querySelector(".details-add-song-modal")
    let btn = document.querySelectorAll(".btn")
    let editButton = document.querySelectorAll(".details-song-details")

    if (add) {
      add.addEventListener("click", () => {
        modal.classList.toggle("invisible")
      })
    }

    song.forEach((selectedSong) => {
      selectedSong.addEventListener("mouseover", () => {
        selectedSong.style.background = lightRgbBG
      })
      selectedSong.addEventListener("mouseout", () => {
        selectedSong.style.background = ""
      })
    })

    input.forEach((inputEl) => {
      if (darkRgbBG) {
        inputEl.style.borderColor = lightRgbBG
      } else {
        inputEl.style.borderColor = "whitesmoke"
      }
    })

    link.forEach((li) => {
      li.addEventListener("mouseover", () => {
        if (lightRgbBG) {
          li.style.borderColor = darkRgbBG
        } else {
          li.style.borderColor = "black"
        }
      })
      li.addEventListener("mouseout", () => {
        li.style.borderColor = ""
      })
    })

    cancel.addEventListener("click", () => {
      modal.classList.toggle("invisible")
    })

    if (editButton) {
      editButton.forEach((button) => {
        button.addEventListener("click", () => {})
      })
    }

    if (darkRgbBG !== null) {
      banner.style.background = darkRgbBG
      add.style.background = darkRgbBG
      addForm.forEach((form) => {
        form.style.color = darkRgbBG
        form.style.borderColor = darkRgbBG
      })
      btn.forEach((button) => {
        button.style.background = darkRgbBG
      })
    } else {
      banner.style.background = lightRgbBG
      add.style.background = lightRgbBG
      addForm.forEach((form) => {
        form.style.color = lightRgbBG
        form.style.borderColor = lightRgbBG
      })
      btn.forEach((button) => {
        button.style.background = lightRgbBG
      })
    }
  })
