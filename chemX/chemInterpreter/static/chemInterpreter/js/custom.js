
var container = $('#div-1'),
    wrapper = $('#div-2');

// temporarily fix the outer div's width
container.css({width: wrapper.width()});
// fade opacity of inner div - use opacity because we cannot get the width or height of an element with display set to none
wrapper.fadeTo('slow', 0, function(){
    // change the div content
    container.html("<div id=\"2\" style=\"display: none;\">new content (with a new width)</div>");
    // give the outer div the same width as the inner div with a smooth animation
    container.animate({width: wrapper.width()}, function(){
        // show the inner div
        wrapper.fadeTo('slow', 1);
    });
});


var elements = document.getElementsByClassName("modal");
for (var i = 0; i < elements.length; i++) {
    elements[i].addEventListener("click", function() {
        var xhr = new XMLHttpRequest();
        // this.getElementsByTagName("div")[1].firstChild.firstChild.innerHTML <-- chemical symbol for element
        xhr.open("POST", serverURL /* to be filled in */ , false /* make async later */ );
        xhr.send(this.getElementsByTagName("div")[1].firstChild.firstChild.innerHTML);
    });
}

var elements = document.getElementsByClassName("modal");
for (var i = 0; i < elements.length; i++) {
	elements[i].addEventListener("click", function() {
		var xhr = new XMLHttpRequest();
		// this.getElementsByTagName("div")[1].firstChild.firstChild.innerHTML <-- chemical symbol for element
		xhr.open("POST", serverURL /* to be filled in */, false /* make async later */);
		xhr.send(this.getElementsByTagName("div")[1].firstChild.firstChild.innerHTML);
	});
}
function addAutocompleteWord(word) {
	$("#autocompletion").append("<p name='autocompletion' style='margin-bottom:5px;margin-top:5px;' value='" +  word + "'>" + word + "</p>");
}
function removeAutocompleteWord(word) {
	for (var i = 0; i < $("#autocompletion").children().length; i++) {
		if ($("#autocompletion").children()[i].innerHTML == word) {
			$("#autocompletion").children()[i].remove();
		}
	}
}
function removeAllAutocompleteWords() {
	$("#autocompletion").empty();
}
$("#searchinput").keyup(function() {
	if (this.value) {
		addAutocompleteWord(this.value);
	} else {
		removeAllAutocompleteWords();
	}
});

