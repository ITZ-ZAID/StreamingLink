function shortenURL() {
  var longURL = document.getElementById("long-url-input").value;
  if (longURL === "") {
    alert("Please enter a URL");
    return;
  }

  // Here you can implement your URL shortening logic using an API or a custom algorithm
  // For demonstration purposes, we'll simply prepend the GitHub Pages URL with a unique identifier
  var shortURL = "https://itz-zaid.github.io/" + generateUniqueID();

  document.getElementById("short-url").innerHTML = "Short URL: <a href='" + shortURL + "' target='_blank'>" + shortURL + "</a>";
}

function generateUniqueID() {
  // Generate random alphanumeric string as a unique identifier
  var chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  var id = "";
  for (var i = 0; i < 6; i++) {
    id += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return id;
}
