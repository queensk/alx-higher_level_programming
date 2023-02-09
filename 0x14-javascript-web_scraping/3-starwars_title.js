#!/usr/bin/node
// prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
