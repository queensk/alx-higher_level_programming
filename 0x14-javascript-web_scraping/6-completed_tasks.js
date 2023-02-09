#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request(url, (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const completed = body[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
