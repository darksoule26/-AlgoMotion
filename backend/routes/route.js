import express from "express";
import { analyzeCode } from "../controller/analyzeCodeController.js";
import { root } from "../controller/rootController.js";
const router = express.Router();

router.get("/", root);
router.post("/analyze", analyzeCode);

export default router;
