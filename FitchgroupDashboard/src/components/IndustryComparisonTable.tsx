import { Building2, ArrowUpDown } from "lucide-react";

interface CompanyData {
  name: string;
  score: number;
  scope1: number;
  scope2: number;
  revenue: number;
  trend: "up" | "down" | "stable";
}

export function IndustryComparisonTable() {
  const companies: CompanyData[] = [
    { name: "Acme Manufacturing Corp", score: 3.4, scope1: 12500, scope2: 8200, revenue: 450, trend: "down" },
    { name: "Industrial Solutions Ltd", score: 2.8, scope1: 9800, scope2: 6500, revenue: 380, trend: "down" },
    { name: "Global Manufacturers Inc", score: 3.1, scope1: 15200, scope2: 9800, revenue: 520, trend: "stable" },
    { name: "Advanced Production Co", score: 3.6, scope1: 18500, scope2: 11200, revenue: 610, trend: "up" },
    { name: "Prime Manufacturing", score: 3.9, scope1: 22100, scope2: 14500, revenue: 720, trend: "up" },
    { name: "Efficient Industries", score: 2.5, scope1: 7200, scope2: 4800, revenue: 310, trend: "down" },
  ];

  return (
    <div className="bg-white rounded-xl shadow-sm border border-slate-200 h-full">
      <div className="p-6 border-b border-slate-100">
        <div className="flex items-center gap-2">
          <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-slate-500 to-slate-600 flex items-center justify-center">
            <Building2 className="w-5 h-5 text-white" />
          </div>
          <div>
            <h2 className="text-slate-900">Industry Comparison</h2>
            <p className="text-slate-500 text-sm">Manufacturing Sector (NACE C)</p>
          </div>
        </div>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full">
          <thead>
            <tr className="border-b border-slate-100">
              <th className="text-left px-6 py-3 text-slate-600 text-sm">
                <div className="flex items-center gap-1">
                  Company
                  <ArrowUpDown className="w-3 h-3" />
                </div>
              </th>
              <th className="text-right px-6 py-3 text-slate-600 text-sm">
                <div className="flex items-center justify-end gap-1">
                  Score
                  <ArrowUpDown className="w-3 h-3" />
                </div>
              </th>
              <th className="text-right px-6 py-3 text-slate-600 text-sm">
                <div className="flex items-center justify-end gap-1">
                  Scope 1 (tCO₂e)
                  <ArrowUpDown className="w-3 h-3" />
                </div>
              </th>
              <th className="text-right px-6 py-3 text-slate-600 text-sm">
                <div className="flex items-center justify-end gap-1">
                  Scope 2 (tCO₂e)
                  <ArrowUpDown className="w-3 h-3" />
                </div>
              </th>
              <th className="text-right px-6 py-3 text-slate-600 text-sm">
                <div className="flex items-center justify-end gap-1">
                  Revenue (M)
                  <ArrowUpDown className="w-3 h-3" />
                </div>
              </th>
              <th className="text-center px-6 py-3 text-slate-600 text-sm">Trend</th>
            </tr>
          </thead>
          <tbody>
            {companies.map((company, index) => {
              const isCurrentCompany = company.name === "Acme Manufacturing Corp";
              return (
                <tr
                  key={index}
                  className={`border-b border-slate-50 transition-colors hover:bg-slate-50 ${
                    isCurrentCompany ? "bg-blue-50" : ""
                  }`}
                >
                  <td className="px-6 py-4">
                    <div className="flex items-center gap-2">
                      <span className="text-slate-900">
                        {company.name}
                      </span>
                      {isCurrentCompany && (
                        <span className="px-2 py-0.5 bg-blue-600 text-white text-xs rounded">
                          You
                        </span>
                      )}
                    </div>
                  </td>
                  <td className="px-6 py-4 text-right">
                    <span
                      className={`inline-flex items-center justify-center w-12 h-7 rounded ${
                        company.score <= 2.5
                          ? "bg-emerald-100 text-emerald-700"
                          : company.score <= 3.5
                          ? "bg-yellow-100 text-yellow-700"
                          : "bg-red-100 text-red-700"
                      }`}
                    >
                      {company.score.toFixed(1)}
                    </span>
                  </td>
                  <td className="px-6 py-4 text-right text-slate-900">
                    {company.scope1.toLocaleString()}
                  </td>
                  <td className="px-6 py-4 text-right text-slate-900">
                    {company.scope2.toLocaleString()}
                  </td>
                  <td className="px-6 py-4 text-right text-slate-900">
                    ${company.revenue}M
                  </td>
                  <td className="px-6 py-4">
                    <div className="flex justify-center">
                      {company.trend === "down" && (
                        <div className="flex items-center gap-1 text-emerald-600">
                          <div className="w-6 h-6 rounded bg-emerald-100 flex items-center justify-center">
                            <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                            </svg>
                          </div>
                        </div>
                      )}
                      {company.trend === "up" && (
                        <div className="flex items-center gap-1 text-red-600">
                          <div className="w-6 h-6 rounded bg-red-100 flex items-center justify-center">
                            <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 10l7-7m0 0l7 7m-7-7v18" />
                            </svg>
                          </div>
                        </div>
                      )}
                      {company.trend === "stable" && (
                        <div className="flex items-center gap-1 text-slate-600">
                          <div className="w-6 h-6 rounded bg-slate-100 flex items-center justify-center">
                            <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 12h14" />
                            </svg>
                          </div>
                        </div>
                      )}
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
