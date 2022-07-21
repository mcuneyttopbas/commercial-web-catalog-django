// Variant Photo
var btnImage = document.querySelectorAll('#variantPhoto');
// Detail Image Screen
var detailScreen = document.querySelector('#detailScreen');
// Close Button 
var btnClose = document.querySelector("#closeBtn")

btnImage.forEach(photo =>{
    photo.addEventListener("click", showPhoto);

    function showPhoto() {
        detailScreen.src = this.src
        // css 
        this.style.border = "var(--clr-grey-2)";
        detailScreen.style.display = "block";
        btnClose.style.display = "block";
    }
})

btnClose.addEventListener("click", closeScreen);

function closeScreen() {
    detailScreen.style.display = "none";
    btnClose.style.display = "none";
}
