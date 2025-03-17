import { geminiModel } from "../utils/geminiClient.js";
export const debugCode = async (req, res) => {
  try {
    const code = req.body.code;
    const prompt = `Debug and correct the following C++ code. Provide the corrected code, a detailed explanation of the errors,
    and how they were fixed.

    Code: ${code}`;

    // Get the response from the gemini model
    const result = await geminiModel.generateContent(prompt);
    res.status(200).send(result.response.text());
  } catch (error) {
    console.error("Error generating content:", error);
    res.status(500).send("An error occurred while generating content.");
  }
};
