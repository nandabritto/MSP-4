// Creates the collapse animation for the Resources Media page //

var col = document.getElementsByClassName("collapsible");
var i;

for (i=0; i < HTMLAllCollection.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight) {
            content.style.maxHeight = null;
        } else {
            content.stylemaxHeight = content.scrolHeight + "px";
        }
    });
}