document.getElementById("websites").addEventListener("click", displayWebsites);

function displayWebsites() {
  if(document.getElementById("website-list").style.display == "block" ){
    document.getElementById("websites").style.color = "#555";
    document.getElementById("website-list").style.display = "none";
  } else {
    document.getElementById("websites").style.color = "#33adff";
    document.getElementById("website-list").style.display = "block";
  }
  
}