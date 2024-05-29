$(document).ready(function () {
  $("INPUT#btn_translate").click(function () {
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
  });
});
