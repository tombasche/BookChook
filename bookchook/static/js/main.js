function displaySeriesNumber() {
  var s = document.getElementById("id_series");
  var name = s.options[s.selectedIndex].text;

  var num = document.getElementById("id_number");
  if (num.value = '') {
    document.getElementById("seriesNumber").style.visibility = "hidden"
  }

  if (name != '---------') {
    document.getElementById("seriesNumber").style.visibility = "visible";
  }
  else {
      var num = document.getElementById("id_number");
      num.value = '';
      document.getElementById("seriesNumber").style.visibility = "hidden";
  }
}

document.onkeyup=function(e){
  var e = e || window.event; // for IE to cover IEs window event-object
  // + to add a book
  if (e.which == '65' && document.getElementsByClassName('book-form').length == 0) {
    document.getElementById('add-book').click();
  }
}
