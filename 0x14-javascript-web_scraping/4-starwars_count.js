#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, body) {
  if (err) {
    console.error(err);
    return;
  }
  obj_json = JSON.parse(body).results;
  let cont = 0;
  for (let obj of obj_json) {
    for (let str of obj.characters) {
      if (str.includes('18')) {
        cont++;
      }
    }
  }
  console.log(cont);
});
