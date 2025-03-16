import express from "express";
import { root } from "../controller/rootController.js";
import { analyzeCode } from "../controller/analyzeCodeController.js";
import { debugCode } from "../controller/debugCodeController.js";
const router = express.Router();

router.get("/", root);
router.post("/analyze", analyzeCode);
router.post("/debug", debugCode);

export default router;
