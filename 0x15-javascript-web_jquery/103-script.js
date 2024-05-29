$(document).ready(function () {
  $("INPUT#btn_translate").click(function () {
    translateHello();
  });

  // ENTER key press on language code input
  $("INPUT#language_code").keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });

  // Function to fetch and display translation of "Hello"
  function translateHello() {
    const langCode = $("INPUT#language_code").val();

    if (langCode) {
      $.ajax({
        type: "GET",
        url: `https://hellosalut.stefanbohacek.dev/?lang=${langCode}`,
        dataType: "json",
        success: function (response) {
          $("DIV#hello").text(response.hello);
        },
        error: function () {
          $("DIV#hello").text("Error fetching translation.");
        },
      });
    }
  }
});
