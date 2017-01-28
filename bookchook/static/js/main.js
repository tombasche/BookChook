/**
 * getEventListeners adds event listeners on blur to name and author fields
 * should they exist (on the book form)
 */
function getEventListeners(){
  var n = document.getElementById('id_name');
  var a = document.getElementById('id_author');

  if(n != null) {
    n.addEventListener('blur', function() {
      var name = document.getElementById('id_name').value;
      document.cookie = "name="+name;
    });
  }

  if (a != null) {
    a.addEventListener('blur', function() {
      var author = document.getElementById('id_author').value;
      document.cookie = "author="+author;
    });
  }
}

/* displaySeriesNumber hides the series number if a series has
 * not been selected on the book form
 */
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

/* getCookie returns a cookie by name
 *
 * @param name - name of the cookie
 * @returns the value of that cookie
 */
function getCookie(name) {
  var re = new RegExp(name + "=([^;]+)");
  var value = re.exec(document.cookie);
  return (value != null) ? unescape(value[1]) : null;
}

/* getFormValues returns the values stored in cookies for
 * the book form.
 */
function getFormValues() {

  var name = document.getElementById("id_name");
  var author = document.getElementById("id_author");

  if(name != null) {
    if (document.getElementById("id_name").value == '') {
      document.getElementById("id_name").value= getCookie("name");
    }
  }

  if (author != null) {
    if (document.getElementById("id_author").value == '') {
      document.getElementById("id_author").value = getCookie("author");
    }
  }
}

/* deleteCookie deletes a cookie stored for the session
 *
 * @param name - name of the cookie to delete
 */
function deleteCookie(name) {
    document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
};

/* wipeCookies is a wrapper function to wipe name and author cookies
 */
function wipeCookies() {
  deleteCookie('name');
  deleteCookie('author');
}

// pressing 'a' while on the book list screen will add a new book
document.onkeyup=function(e) {
  var e = e || window.event; // for IE to cover IEs window event-object
  if (e.which == '65' && document.getElementsByClassName('container-book-list').length > 0) {
    document.getElementById('add-book').click();
  }
}
