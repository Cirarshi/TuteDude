//express app that serves the html files

var express = require("express");
var path = require("path");
var app = express();
var fetch = require("node-fetch");
const { json } = require("stream/consumers");

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

const URL = process.env.BACKEND_URL || "http://localhost:8000/api";

/*
const fetch = (...args) =>
  import("node-fetch").then(({ default: fetch }) => fetch(...args));
*/

app.get("/", async function (req, res) {
  const options = { method: "GET" };
  fetch(URL, options)
    .then((response) => response.json())
    .then((json) => console.log(json))
    .catch((err) => console.error("error:" + err));

  try {
    let response = await fetch(URL, options);
    response = await response.json();
    res.render("index", response);
  } catch (error) {
    console.error(error);
    res.status(500).json({ msg: "Error fetching data from backend" });
  }
});

app.listen(3000, function () {
  console.log(`Server is running on http://localhost:3000`);
});
