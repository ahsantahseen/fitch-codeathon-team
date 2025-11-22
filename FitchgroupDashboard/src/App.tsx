import { ClientScoreCard } from "./components/ClientScoreCard";
import { IndustryComparisonTable } from "./components/IndustryComparisonTable";
import { AISuggestions } from "./components/AISuggestions";
import { EmissionsCharts } from "./components/EmissionsCharts";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-blue-50 to-slate-100">
      {/* Header */}
      <div className="bg-white border-b border-slate-200 shadow-sm">
        <div className="max-w-[1600px] mx-auto px-8 py-6">
          <h1 className="text-slate-900">
            Welcome{" "}
            <span style={{ fontFamily: "Times New Roman, serif" }}>
              <span style={{ color: "#8B0000" }}>Fitch</span>
              <span style={{ color: "#374151" }}>Group</span>
            </span>
          </h1>
          <p className="text-slate-600 mt-1">
            Sustainability Analytics Dashboard
          </p>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-[1600px] mx-auto px-8 py-8">
        {/* Top Section - Client Score & Industry Comparison */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
          <div className="lg:col-span-1">
            <ClientScoreCard />
          </div>
          <div className="lg:col-span-2">
            <IndustryComparisonTable />
          </div>
        </div>

        {/* Middle Section - AI Suggestions */}
        <div className="mb-6">
          <AISuggestions />
        </div>

        {/* Bottom Section - Charts */}
        <div>
          <EmissionsCharts />
        </div>
      </div>
    </div>
  );
}