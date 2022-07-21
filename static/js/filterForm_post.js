var radioBtn = document.querySelectorAll("#checkbox")
var sortMain = document.getElementById('sort')
var sortAssist = document.getElementById('sort2')

const url_string = window.location.href;
var url = new URL(url_string);
var search_param = url.searchParams.get("search");


window.onload = (event) => { 
  
    function hasQueryParams(url) {
    return url.includes('?');
    }

    if (hasQueryParams(url_string) == false || search_param != null){
        radioBtn.forEach(function(btn){
            var output = sessionStorage.getItem(btn.name);
            if (output == "true"){
                sessionStorage.setItem(btn.name, false);
            }
        })
        sessionStorage.setItem("sort", "featured");
    }

    var windowWidth = window.innerWidth
    var element = document.getElementById('advancedSearch');
    if (windowWidth < 992 ){
        
        element.classList.remove("show");
    }
    else {
        element.classList.add("show");
    } 

    radioBtn.forEach(function(btn){
        var output = sessionStorage.getItem(btn.name);
        if (output == "true"){
            btn.checked = true;
        }
    })

    var sort = sessionStorage.getItem("sort")
    sortMain.value = sort
    sortAssist.value = sort
  };


radioBtn.forEach(btn=> {btn.addEventListener("click",send_request);
    
    function send_request(){
        document.getElementById("btn").click();
        sessionStorage.setItem(btn.name, btn.checked);
    }
});
    
sortMain.addEventListener('change', function() {
    sessionStorage.setItem("sort", sortMain.value);
    document.getElementById("btn").click();
  });

sortAssist.addEventListener('change', function() {
    sortMain.value = this.value
    sessionStorage.setItem("sort", sortMain.value);
    document.getElementById("btn").click();
  });

