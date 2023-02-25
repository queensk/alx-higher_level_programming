$(document).ready(function () {
  var addItem = $("#add_item");

  addItem.click(function () {
    var myList = $("UL.my_list");

    myList.append("<li>Item</li>");
  });
});
