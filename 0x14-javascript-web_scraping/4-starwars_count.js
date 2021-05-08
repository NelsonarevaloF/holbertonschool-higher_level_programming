#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  const results = JSON.parse(body).results;
  let cont = 0;
  for (const obj of results) {
    for (const str of obj.characters) {
      if (str.includes('18')) {
        cont++;
      }
    }
  }
  console.log(cont);
});
