$(document).ready(function () {
  var moviesList = $("#list_movies");

  $.get(
    "https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data) {
      var movies = data.results;
      for (var i = 0; i < movies.length; i++) {
        var movie = movies[i];
        var title = movie.title;

        var li = $("<li></li>").text(title);
        moviesList.append(li);
      }
    }
  );
});
