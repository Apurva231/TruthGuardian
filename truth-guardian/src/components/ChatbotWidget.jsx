import React, { useState, useRef, useEffect } from "react";
import chatbotIcon from "../assets/chatbot.jpg"; // replace with your actual path
import "./Chatbot.css";

const ChatbotWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const toggleChat = () => setIsOpen(!isOpen);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: input }),
      });

      const data = await res.json();
      const botMsg = { role: "bot", content: data.response || "No response" };
      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      console.error("API error", err);
      setMessages((prev) => [
        ...prev,
        { role: "bot", content: "Sorry, something went wrong." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Floating Icon */}
      <div className="chatbot-icon" onClick={toggleChat}>
        <img src={chatbotIcon} alt="Chatbot" />
      </div>

      {/* Chat Container */}
      {isOpen && (
        <div className="chatbot-container">
          <div className="chatbot-header">
            SmartBot
            <button onClick={toggleChat}>×</button>
          </div>

          <div className="chatbot-messages">
            {messages.map((msg, idx) => (
              <div
                key={idx}
                className={`chatbot-message ${
                  msg.role === "user" ? "user-message" : "bot-message"
                }`}
              >
                {msg.content}
              </div>
            ))}
            {loading && (
              <div className="bot-message chatbot-message loading-message">
                Typing...
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="chatbot-input">
            <input
              type="text"
              placeholder="Type your message..."
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            />
            <button onClick={sendMessage}>Send</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default ChatbotWidget;
