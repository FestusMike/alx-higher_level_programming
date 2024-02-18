#!/usr/bin/node
/*
Script that computes the number of tasks completed by user ID.
*/

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const taskResults = {};
    const tasksData = JSON.parse(body);

    for (let i = 0; i < tasksData.length; i++) {
      const task = tasksData[i];

      if (task.completed === true) {
        if (taskResults[task.userId] !== undefined) {
          taskResults[task.userId] += 1;
        } else {
          taskResults[task.userId] = 1;
        }
      }
    }

    console.log(taskResults);
  }
});
