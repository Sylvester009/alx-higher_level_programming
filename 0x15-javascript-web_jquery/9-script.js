$(document).ready(function () {
  $.ajax({
    type: "get",
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
    dataType: "json",
    success: function (response) {
      $("DIV#hello").append(`${response.hello}`);
    },
  });
});
