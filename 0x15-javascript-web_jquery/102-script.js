$(document).ready(function () {
  $("INPUT#btn_translate").click(function () {
    const langCode = $("INPUT#language_code").val();

    $.ajax({
      type: "GET",
      url: "https://hellosalut.stefanbohacek.dev/?lang=" + langCode,
      dataType: "json",
      success: function (response) {
        console.log(response); // Log the response to the console
        $("DIV#hello").text(response.hello);
      },
      error: function (error) {
        $("DIV#hello").text("Error fetching translation.");
      },
    });
  });
});
