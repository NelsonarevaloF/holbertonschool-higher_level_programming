#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(JSON.parse(body).title);
});
