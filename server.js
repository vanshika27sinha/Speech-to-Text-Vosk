const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();

// ✅ Enable CORS so frontend can call Flask backend
app.use(cors());

// ✅ Serve static files (like index.html)
app.use(express.static(__dirname));

// ✅ Route for root
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

// ✅ Start frontend server on port 5000
app.listen(5000, "127.0.0.1", () => {
  console.log("✅ Frontend running at http://127.0.0.1:5000");
});
