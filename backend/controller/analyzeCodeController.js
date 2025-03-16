import { geminiModel } from "../utils/geminiClient.js";
export const analyzeCode = async (req, res) => {
  try {
    const code = req.body.prompt;
    const prompt = `Analyze the following C++ code and provide a detailed explanation of its functionality,
        including step-by-step execution, diagrams if applicable, and any potential errors. ${code}`;

    // Get the response from the gemini model
    const result = await geminiModel.generateContent(prompt);
    res.status(200).send(result.response.text());
  } catch (error) {
    console.error("Error generating content:", error);
    res.status(500).send("An error occurred while generating content.");
  }
};
