import React, { Component, useState } from 'react';
const fetch = require("node-fetch");
async function postData(url="http://127.0.0.1:9000/api/v1/getresultstest?title=test"){
  const response = await fetch(url);
  return response.json();
}