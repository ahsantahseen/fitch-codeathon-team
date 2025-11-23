import { Sparkles, Lightbulb, CheckCircle2, AlertCircle, MessageSquare, Send, Loader2 } from "lucide-react";
import { useState, useEffect } from "react";
import { useDashboard } from "../context/DashboardContext";
export function TrainedModelDescription() {

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200">
      <div className="p-6 border-b border-slate-100">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-violet-500 to-purple-600 flex items-center justify-center">
              <Sparkles className="w-5 h-5 text-white" />
            </div>
            <div>
              <h2 className="text-slate-900">Our Custom Model</h2>
              <p className="text-slate-500 text-sm">Designing our model</p>
            </div>
          </div>
          <div className="flex items-center gap-2 px-3 py-1.5 bg-violet-50 border border-violet-200 rounded-lg">
            <AlertCircle className="w-4 h-4 text-violet-600" />
            <span className="text-violet-700 text-sm">Action Required</span>
          </div>
        </div>
      </div>
      <p className="px-2.5 py-1 border rounded text-lg">
        INSERT MODEL DESCRIPTION
      </p>
    </div>
  );
}