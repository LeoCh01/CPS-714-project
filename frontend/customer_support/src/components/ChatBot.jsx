import ChatBot from "react-chatbotify";
import { useState } from "react";
import { GoogleGenerativeAI } from "@google/generative-ai";

const MyChatBot = () => {
  const genAI = new GoogleGenerativeAI("AIzaSyB5IXg5PJUgaH5uGFDd2dtiMEyblMPbJwQ");

  const liveChatInstructions = `You are the virtual assistant for Greenleaf Innovations. GreenLeaf Innovations, a leading provider of eco-friendly home solutions, is launching a Client
    Engagement Web Portal aimed at enhancing customer interactions, promoting green products,
    and fostering client loyalty. The portal will reward clients for purchasing GreenLeaf products,
    enrolling in energy-saving programs, and participating in environmental initiatives.
    The web portal will feature a client interface where users can manage their profiles, track
    purchases, earn and redeem rewards, and access educational resources about sustainable living.
    An administrative backend will allow GreenLeaf to manage the loyalty program, gather client
    feedback, and oversee support services.
    You will handle customer support inquiries. You will generally deal with:
    - General questions about eco friendly products and services
    - Helping customers understand the general idea of what products are sold and their functions and purposes
    - Providing guidance on submitting tickets for simple and complex issues
    
    This is the definition of a ticket: Support requests related to products or accounts.
    You need to respond in a professional, friendly manner and keep answers concise unless further detail is required.
    If you are unsure about a question from a user, encourage them to write a ticket in the ticketing system for further assistance.
    `;

  async function run(prompt, streamMessage, retries = 3) {
    for (let i = 0; i < retries; i++) {
      try {
        const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

        // Live chat instructions in the prompt
        const fullPrompt = `${liveChatInstructions}\n\nUser Query: ${prompt}`;

        const result = await model.generateContentStream(fullPrompt);
        let text = "";
        for await (const chunk of result.stream) {
          const chunkText = chunk.text();
          text += chunkText;
          streamMessage(text);
        }
        return text;
      } catch (error) {
        if (error.message.includes("overloaded") && i < retries - 1) {
          console.log(`Retrying... (${i + 1}/${retries})`);
          await new Promise((resolve) => setTimeout(resolve, 2000)); // Wait 2 seconds before retrying
        } else {
          throw error;
        }
      }
    }
  }

  const flow = {
    start: {
      message: "Hello, how may I assist you today?",
      path: "model_loop",
    },
    model_loop: {
      message: async (params) => {
        return await run(params.userInput, params.streamMessage);
      },
      path: "model_loop",
    },
  };

  return (
    <div>
      <h1>Chatbot</h1>
      <ChatBot flow={flow} />
    </div>
  );
};

export default MyChatBot;
