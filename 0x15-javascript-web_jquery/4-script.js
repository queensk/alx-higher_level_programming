$(document).ready(function () {
  var toggleHeader = $("#toggle_header");

  toggleHeader.click(function () {
    var header = $("header");

    header.toggleClass("red green");
  });
});
