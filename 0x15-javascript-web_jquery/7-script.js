$(document).ready(function () {
  $.ajax({
    type: "get",
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    dataType: "json",
    success: function (response) {
      $("DIV#character").text(`${response.name}`);
    },
  });
});
