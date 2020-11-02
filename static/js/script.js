// Parse the URL parameter
	function getParameterByName(name, url) {
	    if (!url) url = window.location.href;
	    name = name.replace(/[\[\]]/g, "\\$&");
	    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
	        results = regex.exec(url);
	    if (!results) return null;
	    if (!results[2]) return '';
	    return decodeURIComponent(results[2].replace(/\+/g, " "));
	}

// Give the parameter a variable name
var dynamicContent = getParameterByName('dc');

$(document).ready(function() {
	// Check if the URL parameter is contact-contact-form
	if (dynamicContent == 'box1') {
		$('#category-box').addClass('d-block');
        $('#category-box').removeClass('d-none');
        $('#product-box').addClass('d-none');
		$('#product-box').removeClass('d-block');
	}
	// Check if the URL parameter is contact-register-form
	else if (dynamicContent == 'product-box') {
		$('#category-box').addClass('d-none');
        $('#category-box').removeClass('d-block');
        $('#product-box').addClass('d-block');
		$('#product-box').removeClass('d-none');
	}
	// Check if the URL parmeter is empty or not defined, display default content
	else {
        $('#product-box').addClass('d-block');
        $('#category-box').addClass('d-block');
	}
});

