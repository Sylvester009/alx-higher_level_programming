$(document).ready(function () {
  // add item
  $("DIV#add_item").click(function (e) {
    e.preventDefault();
    $("UL.my_list").append("<li>Item</li>");
  });

  //remove item
  $("DIV#remove_item").click(function (e) {
    e.preventDefault();
    $("UL.my_list li").last().remove();
  });

  //clear item
  $("DIV#clear_list").click(function (e) {
    e.preventDefault();
    $("UL.my_list").empty();
  });
});
