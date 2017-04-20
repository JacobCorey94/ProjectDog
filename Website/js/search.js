function presentData(result) {
	if ($("#results").length ) {
		// Clear any search results that may be there
		$("#results").empty();
	} else {
		// Create it if none exists
		$("section").append("<section id='results'><section>");
	}
  $("#results").append("<table stile=\"width:100%\">");
  $("#results").append("<tr><th>Price</th><th>Item</th></tr>");
	for(var ind=0; ind < result.length; ind++) {
		//$("#results").append("<a href=\""+result[ind][2]+"\">$"+result[ind][1]+" - "+result[ind][0]+"</a><br />");
    $("#results").append("<tr><td>$"+result[ind][1]+"</td><td href=\""+result[ind][2]+"\">"+result[ind][0]+"</td></tr>");
  }
  $("#results").append("</table>");
	$("#runDog").css("display","none");
}
function displayWebsites() {
  if (document.getElementById("website-list").style.display === "block") {
    document.getElementById("websites").style.color = "#555";
    document.getElementById("website-list").style.display = "none";
  } else {
    document.getElementById("websites").style.color = "#33adff";
    document.getElementById("website-list").style.display = "block";
  }
}

function simplify_input(string_array) {
  for (var i = 0; i < string_array.length; i++) {
    string_array[i] = string_array[i].replace('\'', '');
    string_array[i] = string_array[i].replace(' ', '');
    string_array[i] = string_array[i].toLowerCase();
  }
  return string_array;
}

function search(e) {
  e.preventDefault();
  //var search_term = '\"';
  var search_term = "";
  search_term += document.getElementById("search-field").elements[0].value
  //search_term += '\"';
  var list_elements = document.getElementById("website-list").getElementsByTagName("li"),
    checked_websites = [];
  
//See which websites are checked
  var j = 0;
  for (var i = 0; i < list_elements.length; i++) {
    if(list_elements[i].getElementsByTagName("input")[0].checked === true){
      checked_websites[j++] = list_elements[i].getElementsByTagName("a")[0].text;
    }
  }
  console.log(checked_websites); //used for error checking, delete later
  checked_websites = simplify_input(checked_websites);
  console.log(checked_websites); //used for error checking, delete later
  console.log(search_term); //used for error checking, delete later

  var fetch;
  $("#runDog").css("display","block");
  var throwItem = $.ajax(
    { url: "fetch.php?item=" + search_term + "&sites=" + checked_websites,
      dataType: 'json',
      success: function(result) {
        // result will be a 2d array containing the following:
	// [ITEM][NAME, PRICE, URL]
	presentData(result);
	//alert("Fetched!");
      }
 });
 
}

document.getElementById("websites").addEventListener("click", displayWebsites);
document.getElementById("goFetch").addEventListener("click", search);
