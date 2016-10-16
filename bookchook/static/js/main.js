function displaySeriesNumber() {
  var s = document.getElementById("id_series");
  var name = s.options[s.selectedIndex].text;

  if (name != '---------') {
    document.getElementById("seriesNumber").style.visibility = "visible";
  }
  else {
      var num = document.getElementById("id_number");
      num.value = ''; 
      document.getElementById("seriesNumber").style.visibility = "hidden";
  }
}
