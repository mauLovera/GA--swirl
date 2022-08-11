// song = document.getElementById('song')
// play = document.getElementById('play')
// count = document.getElementById('count')

picture = document.querySelector('.details-image-container')
pictureUrlExtract = picture.style.backgroundImage
pictureUrlSplit1 = pictureUrlExtract.split('url(').join('')
pictureUrlSplit2 = pictureUrlSplit1.split(')')
pictureUrl = pictureUrlSplit2[0]

console.log(Vibrant)
