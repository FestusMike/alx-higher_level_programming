#!/usr/bin/node

/*
concats 2 files
*/

const fs = require('fs');
const args = process.argv;

const fileA = fs.readFileSync(args[2], 'utf-8').toString();
const fileB = fs.readFileSync(args[3], 'utf-8').toString();
fs.writeFileSync(args[4], fileA + fileB);
