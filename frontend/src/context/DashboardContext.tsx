// src/context/DashboardContext.tsx
import { createContext, useState, useContext, ReactNode, useEffect, React} from "react";

interface CompanyRecord {
  entity_id: number;
  country_code: string;
  country_name: string;
  region_code: string;
  region_name: string;
  revenue: number;
  overall_score: number;
  environmental_score: number;
  social_score: number;
  governance_score: number;
  target_scope_1: number;
  target_scope_2: number;
}

interface DashboardContextType {
  entityIds: number[];
  currentEntityId: number | null;
  currentRecord: CompanyRecord;
  comparisonRecords: CompanyRecord[];
  setCurrentEntityId: (id: number) => void;
  loading: boolean;
  loadingComparisons: boolean;
}

const dummyRecord: CompanyRecord = {
  entity_id: 0,
  country_code: "",
  country_name: "",
  region_code: "",
  region_name: "",
  revenue: 0,
  overall_score: 0,
  environmental_score: 0,
  social_score: 0,
  governance_score: 0,
  target_scope_1: 0,
  target_scope_2: 0,
};

const DashboardContext = createContext<DashboardContextType>({
  entityIds: [],
  currentEntityId: null,
  currentRecord: dummyRecord,
  comparisonRecords: [],
  setCurrentEntityId: () => {},
  loading: true,
  loadingComparisons: true,
});

export const DashboardProvider = ({ children }: { children: ReactNode }) => {
  const [entityIds, setEntityIds] = useState<number[]>([]);
  const [currentEntityId, setCurrentEntityId] = useState<number | null>(null);
  const [currentRecord, setCurrentRecord] = useState<CompanyRecord>(dummyRecord);
  const [comparisonRecords, setComparisonRecords] = useState<CompanyRecord[]>([]);
  const [loading, setLoading] = useState(true);
  const [loadingComparisons, setLoadingComparisons] = useState(true);

  // Fetch entity IDs
  useEffect(() => {
    fetch("http://localhost:8000/entity_ids")
      .then((res) => res.json())
      .then((data) => {
        setEntityIds(data.entity_ids);
        setCurrentEntityId(data.entity_ids[0] || null);
      })
      .catch(console.error);
  }, []);

  // Fetch current record whenever entity changes
  useEffect(() => {
    if (!currentEntityId) return;

    setLoading(true);
    fetch(`http://localhost:8000/company/${currentEntityId}`)
      .then((res) => res.json())
      .then((data) => {
        setCurrentRecord(data);
        setLoading(false);
      })
      .catch((err) => {
        console.error(err);
        setLoading(false);
      });
  }, [currentEntityId]);

  // Fetch comparison records whenever entity changes
  useEffect(() => {
    if (!currentEntityId) return;

    setLoadingComparisons(true);
    fetch(`http://localhost:8000/comparisons/${currentEntityId}`)
      .then((res) => res.json())
      .then((data) => {
        setComparisonRecords(data.comparisons);
        setLoadingComparisons(false);
      })
      .catch((err) => {
        console.error("Error fetching comparisons:", err);
        setLoadingComparisons(false);
      });
  }, [currentEntityId]);

  return (
    <DashboardContext.Provider
      value={{
        entityIds,
        currentEntityId,
        currentRecord,
        comparisonRecords,
        setCurrentEntityId,
        loading,
        loadingComparisons,
      }}
    >
      {children}
    </DashboardContext.Provider>
  );
};

// Custom hook for easy access
export const useDashboard = () => useContext(DashboardContext);
