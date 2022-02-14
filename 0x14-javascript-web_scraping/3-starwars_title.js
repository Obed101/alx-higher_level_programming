#!/usr/bin/node
// This file prints data from a Star Wars API
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/{}'.format(id);
const request = require('requests');

request(url, (error, response) => {
  if (error) console.log(error);

  if (response.keys('episode_id') === id) console.log(response.keys('title'));
});
