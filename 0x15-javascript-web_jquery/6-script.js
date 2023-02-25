$(document).ready(function () {
  var updateHeader = $("#update_header");

  updateHeader.click(function () {
    var header = $("header");

    header.text("New Header!!!");
  });
});
