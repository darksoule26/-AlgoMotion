import express from "express";
import { GoogleGenerativeAI } from "@google/generative-ai";
import { CONFIG } from "./config/config.js";
import route from "./routes/route.js";
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

app.use("/", route);

app.listen(port, () => {
  console.log(`App listening on port http://localhost:${port}`);
});
