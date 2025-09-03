const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.set("view engine", "ejs");
app.use(bodyParser.urlencoded({ extended: true }));

// Serve the form
app.get("/", (req, res) => {
  res.render("index");
});

// Handle form submission and send data to Flask backend
app.post("/submit", async (req, res) => {
  const { name, email } = req.body;

  try {
    // Send data to Flask backend
    const response = await axios.post("http://127.0.0.1:5000/process", {
      name,
      email,
    });

    res.send(`<h2>Response from Flask: ${response.data.message}</h2>`);
  } catch (err) {
    res.send(`<h2>Error: ${err.message}</h2>`);
  }
});

app.listen(3000, () => {
  console.log("✅ Frontend running on http://localhost:3000");
});
