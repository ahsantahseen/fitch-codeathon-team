import { TrendingDown, TrendingUp, Award } from "lucide-react";

export function ClientScoreCard() {
  const clientScore = 3.4;
  const clientPercentile = 62;
  const previousScore = 3.7;
  const scoreChange = clientScore - previousScore;
  const isImproving = scoreChange < 0; // Lower score is better (1-5 scale)

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 h-full">
      <div className="flex items-center gap-2 mb-6">
        <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-500 to-blue-600 flex items-center justify-center">
          <Award className="w-5 h-5 text-white" />
        </div>
        <div>
          <h2 className="text-slate-900">Client Overview</h2>
          <p className="text-slate-500 text-sm">Acme Manufacturing Corp</p>
        </div>
      </div>

      {/* Overall Score */}
      <div className="mb-6">
        <div className="flex items-baseline justify-between mb-2">
          <span className="text-slate-600 text-sm">Overall Sustainability Score</span>
          <div className="flex items-center gap-1">
            {isImproving ? (
              <TrendingDown className="w-4 h-4 text-emerald-600" />
            ) : (
              <TrendingUp className="w-4 h-4 text-amber-600" />
            )}
            <span className={`text-sm ${isImproving ? "text-emerald-600" : "text-amber-600"}`}>
              {Math.abs(scoreChange).toFixed(1)}
            </span>
          </div>
        </div>
        <div className="flex items-end gap-2">
          <span className="text-slate-900" style={{ fontSize: '2.5rem', lineHeight: '1' }}>
            {clientScore.toFixed(1)}
          </span>
          <span className="text-slate-400 mb-1">/ 5.0</span>
        </div>
        <div className="mt-3 h-2 bg-slate-100 rounded-full overflow-hidden">
          <div
            className="h-full bg-gradient-to-r from-emerald-500 via-yellow-500 to-red-500 rounded-full transition-all duration-500"
            style={{ width: `${(clientScore / 5) * 100}%` }}
          />
        </div>
        <div className="flex justify-between mt-1 text-xs text-slate-400">
          <span>Excellent (1.0)</span>
          <span>Poor (5.0)</span>
        </div>
      </div>

      {/* Percentile */}
      <div className="mb-6">
        <span className="text-slate-600 text-sm">Industry Percentile</span>
        <div className="flex items-end gap-2 mt-2">
          <span className="text-slate-900" style={{ fontSize: '2rem', lineHeight: '1' }}>
            {clientPercentile}
            <span className="text-slate-400">th</span>
          </span>
        </div>
        <p className="text-slate-500 text-sm mt-2">
          Better than {clientPercentile}% of companies in your sector
        </p>
      </div>

      {/* Score Breakdown */}
      <div className="space-y-3 pt-6 border-t border-slate-100">
        <div>
          <div className="flex justify-between text-sm mb-1">
            <span className="text-slate-600">Environmental</span>
            <span className="text-slate-900">3.2</span>
          </div>
          <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
            <div className="h-full bg-emerald-500 rounded-full" style={{ width: '64%' }} />
          </div>
        </div>
        <div>
          <div className="flex justify-between text-sm mb-1">
            <span className="text-slate-600">Social</span>
            <span className="text-slate-900">3.5</span>
          </div>
          <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
            <div className="h-full bg-blue-500 rounded-full" style={{ width: '70%' }} />
          </div>
        </div>
        <div>
          <div className="flex justify-between text-sm mb-1">
            <span className="text-slate-600">Governance</span>
            <span className="text-slate-900">3.6</span>
          </div>
          <div className="h-1.5 bg-slate-100 rounded-full overflow-hidden">
            <div className="h-full bg-purple-500 rounded-full" style={{ width: '72%' }} />
          </div>
        </div>
      </div>
    </div>
  );
}
