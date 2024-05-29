$(document).ready(function () {
  $("DIV#toggle_header").click(function () {
    const red = $("header").hasClass("red");
    const green = $("header").hasClass("green");

    if (green) {
      $("header").removeClass("green").addClass("red");
    } else if (red) {
      $("header").removeClass("red").addClass("green");
    } else {
      $("header").addClass("green");
    }
  });
});
