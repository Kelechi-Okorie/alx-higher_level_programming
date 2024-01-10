$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $.each(data.results, (index, value) => {
    $('<li>' + value.title + '</li>').appendTo('#ul#list_movies');
  });
});
