#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const totalTasks = {};
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    for (const idx in tasks) {
      const task = tasks[idx];
      if (task.completed) {
        if (totalTasks[task.userId] === undefined) {
          totalTasks[task.userId] = 1;
        } else {
          totalTasks[task.userId]++;
        }
      }
    }
    console.log(totalTasks);
  }
});
