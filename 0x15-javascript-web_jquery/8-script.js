$(document).ready(function () {
  $.ajax({
    type: "get",
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    dataType: "json",
    success: function (response) {
      response.results.forEach(function (film) {
        $("UL#list_movies").append(`<li>${film.title}</li>`);
      });
    },
  });
});
