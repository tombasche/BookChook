


function getEventListeners(){
  var n = document.getElementById('id_name');
  var a = document.getElementById('id_author');
  n.addEventListener('blur', function() {
    var name = document.getElementById('id_name').value;
    console.log(name);
    document.cookie = "name="+name;
  });
  a.addEventListener('blur', function() {
    var author = document.getElementById('id_author').value;
    console.log(author);
    document.cookie = "author="+author;
  });
}

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

function getCookie(name) {
  var re = new RegExp(name + "=([^;]+)");
  var value = re.exec(document.cookie);
  return (value != null) ? unescape(value[1]) : null;
}

function getFormValues() {
  if (document.getElementById("id_name").value == '') {
    document.getElementById("id_name").value= getCookie("name");
  }

  if (document.getElementById("id_author").value == '') {
    document.getElementById("id_author").value = getCookie("author");
  }
}

function deleteCookie(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
};

function wipeCookies() {

  deleteCookie('name');
  deleteCookie('author');

}

document.onkeyup=function(e) {
  var e = e || window.event; // for IE to cover IEs window event-object
  // + to add a book
  if (e.which == '65' && document.getElementsByClassName('book-table').length > 0) {
    document.getElementById('add-book').click();
  }
}
