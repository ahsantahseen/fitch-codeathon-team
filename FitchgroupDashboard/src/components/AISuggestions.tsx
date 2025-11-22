import { Sparkles, Lightbulb, CheckCircle2, AlertCircle, MessageSquare, Send } from "lucide-react";
import { useState } from "react";

interface Suggestion {
  title: string;
  description: string;
  impact: "high" | "medium" | "low";
  category: string;
  estimatedReduction: string;
}

interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  timestamp: string;
}

export function AISuggestions() {
  const [activeTab, setActiveTab] = useState<"recommendations" | "chat">("recommendations");
  const [chatInput, setChatInput] = useState("");

  // Static chat messages for demo
  const [chatMessages] = useState<ChatMessage[]>([
    {
      role: "assistant",
      content: "Hello! I'm your AI sustainability advisor. I can help you understand your emissions data, suggest improvement strategies, and answer questions about your sustainability goals. How can I assist you today?",
      timestamp: "10:30 AM"
    },
    {
      role: "user",
      content: "What are the main contributors to our Scope 1 emissions?",
      timestamp: "10:32 AM"
    },
    {
      role: "assistant",
      content: "Based on your current data, your Scope 1 emissions (12,500 tCO₂e) primarily come from three sources:\n\n1. Manufacturing processes (7,200 tCO₂e - 58%)\n2. Fleet & logistics (3,100 tCO₂e - 25%)\n3. On-site heating systems (2,200 tCO₂e - 17%)\n\nYour manufacturing processes are the largest contributor. Would you like specific recommendations for reducing emissions in this area?",
      timestamp: "10:32 AM"
    }
  ]);

  const suggestions: Suggestion[] = [
    {
      title: "Transition to Renewable Energy Sources",
      description: "Your Scope 2 emissions are 34% above industry average. Switching to renewable energy contracts or installing on-site solar could significantly reduce your carbon footprint.",
      impact: "high",
      category: "Energy",
      estimatedReduction: "-2,800 tCO₂e/year"
    },
    {
      title: "Optimize Manufacturing Process Efficiency",
      description: "Analysis suggests potential inefficiencies in your manufacturing processes. Implementing lean manufacturing principles and upgrading equipment could reduce direct emissions.",
      impact: "high",
      category: "Operations",
      estimatedReduction: "-1,500 tCO₂e/year"
    },
    {
      title: "Implement Energy Management System (ISO 50001)",
      description: "Companies with certified energy management systems show 15-20% better emission performance. This would improve your environmental score and reduce operational costs.",
      impact: "medium",
      category: "Governance",
      estimatedReduction: "-900 tCO₂e/year"
    },
    {
      title: "Fleet Electrification Initiative",
      description: "Your logistics operations contribute significantly to Scope 1 emissions. Transitioning company vehicles to electric or hybrid models would demonstrate environmental commitment.",
      impact: "medium",
      category: "Transport",
      estimatedReduction: "-600 tCO₂e/year"
    },
    {
      title: "Supply Chain Carbon Assessment",
      description: "Engaging with suppliers to track and reduce their emissions would position you as an industry leader and improve your overall sustainability score.",
      impact: "low",
      category: "Supply Chain",
      estimatedReduction: "-400 tCO₂e/year"
    }
  ];

  const getImpactColor = (impact: string) => {
    switch (impact) {
      case "high":
        return "bg-red-100 text-red-700 border-red-200";
      case "medium":
        return "bg-amber-100 text-amber-700 border-amber-200";
      case "low":
        return "bg-blue-100 text-blue-700 border-blue-200";
      default:
        return "bg-slate-100 text-slate-700 border-slate-200";
    }
  };

  const handleSendMessage = () => {
    // Placeholder for future chat logic
    if (chatInput.trim()) {
      console.log("Message sent:", chatInput);
      setChatInput("");
    }
  };

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200">
      <div className="p-6 border-b border-slate-100">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <h2 className="text-slate-900">AI-Powered Recommendations</h2>
              <p className="text-slate-500 text-sm">Personalized suggestions to improve your sustainability score</p>
            </div>
          </div>
          <div className="flex items-center gap-2 px-3 py-1.5 bg-violet-50 border border-violet-200 rounded-lg">
            <AlertCircle className="w-4 h-4 text-violet-600" />
            <span className="text-violet-700 text-sm">Action Required</span>
          </div>
        </div>

        {/* Tab Navigation */}
        <div className="flex gap-2 mt-6">
          <button
            onClick={() => setActiveTab("recommendations")}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
              activeTab === "recommendations"
                ? "bg-violet-600 text-white"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            <Lightbulb className="w-4 h-4" />
            <span>Recommendations</span>
          </button>
          <button
            onClick={() => setActiveTab("chat")}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${
              activeTab === "chat"
                ? "bg-violet-600 text-white"
                : "bg-slate-100 text-slate-600 hover:bg-slate-200"
            }`}
          >
            <MessageSquare className="w-4 h-4" />
            <span>AI Assistant</span>
          </button>
        </div>
      </div>

      {/* Recommendations Tab Content */}
      {activeTab === "recommendations" && (
        <div className="p-6">
          <div className="space-y-4">
            {suggestions.map((suggestion, index) => (
              <div
                key={index}
                className="group border border-slate-200 rounded-lg p-5 hover:border-violet-300 hover:shadow-md transition-all duration-200"
              >
                <div className="flex items-start gap-4">
                  <div className="mt-1 w-10 h-10 rounded-lg bg-gradient-to-br from-violet-100 to-purple-100 flex items-center justify-center flex-shrink-0 group-hover:from-violet-200 group-hover:to-purple-200 transition-all">
                    <Lightbulb className="w-5 h-5 text-violet-600" />
                  </div>
                  <div className="flex-1 min-w-0">
                    <div className="flex items-start justify-between gap-4 mb-2">
                      <h3 className="text-slate-900">{suggestion.title}</h3>
                      <div className="flex items-center gap-2 flex-shrink-0">
                        <span className={`px-2.5 py-1 border rounded text-xs ${getImpactColor(suggestion.impact)}`}>
                          {suggestion.impact.toUpperCase()} IMPACT
                        </span>
                        <span className="px-2.5 py-1 bg-slate-100 text-slate-700 rounded text-xs">
                          {suggestion.category}
                        </span>
                      </div>
                    </div>
                    <p className="text-slate-600 mb-3">{suggestion.description}</p>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2">
                        <div className="flex items-center gap-1.5 px-3 py-1.5 bg-emerald-50 border border-emerald-200 rounded">
                          <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                          <span className="text-emerald-700 text-sm">
                            Estimated Impact: <span>{suggestion.estimatedReduction}</span>
                          </span>
                        </div>
                      </div>
                      <button className="px-4 py-2 bg-violet-600 text-white rounded-lg hover:bg-violet-700 transition-colors text-sm">
                        View Details
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Chat Tab Content */}
      {activeTab === "chat" && (
        <div className="flex flex-col h-[600px]">
          {/* Chat Messages */}
          <div className="flex-1 overflow-y-auto p-6 space-y-4">
            {chatMessages.map((message, index) => (
              <div
                key={index}
                className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}
              >
                <div
                  className={`max-w-[70%] ${
                    message.role === "user"
                      ? "bg-violet-600 text-white rounded-lg rounded-tr-sm"
                      : "bg-slate-100 text-slate-900 rounded-lg rounded-tl-sm"
                  } px-4 py-3`}
                >
                  <p className="text-sm whitespace-pre-line">{message.content}</p>
                  <p
                    className={`text-xs mt-2 ${
                      message.role === "user" ? "text-violet-200" : "text-slate-500"
                    }`}
                  >
                    {message.timestamp}
                  </p>
                </div>
              </div>
            ))}
          </div>

          {/* Chat Input */}
          <div className="border-t border-slate-100 p-6">
            <div className="flex gap-3">
              <input
                type="text"
                value={chatInput}
                onChange={(e) => setChatInput(e.target.value)}
                onKeyPress={(e) => e.key === "Enter" && handleSendMessage()}
                placeholder="Ask about your emissions, request recommendations, or get sustainability advice..."
                className="flex-1 px-4 py-3 bg-slate-50 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-violet-500 focus:border-transparent text-slate-900 placeholder:text-slate-400"
              />
              <button
                onClick={handleSendMessage}
                className="px-6 py-3 bg-violet-600 text-white rounded-lg hover:bg-violet-700 transition-colors flex items-center gap-2"
              >
                <Send className="w-4 h-4" />
                <span>Send</span>
              </button>
            </div>
            <p className="text-slate-400 text-xs mt-2">
              This is a demo interface. Chat functionality will be implemented soon.
            </p>
          </div>
        </div>
      )}
    </div>
  );
}