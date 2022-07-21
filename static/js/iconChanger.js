var usageCount = 0

function usage(){
    var element = document.getElementById("usage-js")
    
    usageCount = usageCount + 1
    if (usageCount%2 == 0) {
        element.className = "bi bi-chevron-up";
    }
    else {
        element.className = "bi bi-chevron-down";
    }
    
}

var typeCount = 0

function filtertype(){
    var element = document.getElementById("type-js")
    
    typeCount = typeCount + 1
    if (typeCount%2 == 0) {
        element.className = "bi bi-chevron-up";
    }
    else {
        element.className = "bi bi-chevron-down";
    }
    
}

var widthCount = 0

function width(){
    var element = document.getElementById("width-js")
    
    widthCount = widthCount + 1
    if (widthCount%2 == 0) {
        element.className = "bi bi-chevron-up";
    }
    else {
        element.className = "bi bi-chevron-down";
    }
    
}


function advancedsearch(){
    var element = document.getElementById("filter-main-title");
    var element2 = document.getElementById("advanced-js");
    
    var inclass = element.classList.contains('collapsed');
    
    if (inclass) {
        element2.className = "bi bi-chevron-down";
    }
    else {
        element2.className = "bi bi-chevron-up";
    }
    
}


function sortcollapse(){
    var element = document.getElementById("sort-main-title");
    var element2 = document.getElementById("sort-js");
    
    var inclass = element.classList.contains('collapsed');
    
    if (inclass) {
        element2.className = "bi bi-chevron-down";
    }
    else {
        element2.className = "bi bi-chevron-up";
    }
    
}




window.addEventListener("resize", function(event) {

    var windowWidth = window.innerWidth
    var element = document.getElementById('advancedSearch');
    if (windowWidth < 992 ){
        
        element.classList.remove("show");
    }
    else {
        element.classList.add("show");
    }
})


// function sortcollapse(){
//     var advancedId = document.getElementById("filter-main-title");
//     var advancedMenu = document.getElementById("advancedSearch");
//     var advancedBoolean = advancedId.classList.contains('collapsed')

//     if (advancedBoolean == false){
//         advancedMenu.classList.add("collapsing");
//     }

//     var element = document.getElementById("sort-main-title");
//     var element2 = document.getElementById("sort-js");
    
//     var inclass = element.classList.contains('collapsed');
    
//     if (inclass) {
//         element2.className = "bi bi-chevron-down";
//     }
//     else {
//         element2.className = "bi bi-chevron-up";
//     }
    
// }