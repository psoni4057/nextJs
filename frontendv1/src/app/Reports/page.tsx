
import AuditReport from "../components/AuditReport";

export default function Home() {
  
    const sampleAudits = [
        { Id: 1, Date: '2024-01-01', Application: 'App A', Model: 'Model X', ComplianceArea: 'Area 51', Status: 'Passed', Comments: 'All checks passed' },
        { Id: 2, Date: '2024-01-02', Application: 'App B', Model: 'Model Y', ComplianceArea: 'Area 52', Status: 'Failed', Comments: 'Minor issues found' },
        { Id: 3, Date: '2024-01-03', Application: 'App C', Model: 'Model Z', ComplianceArea: 'Area 53', Status: 'Passed', Comments: 'No issues' },
        // Add more audit entries as needed
      ];
  return (
    <div >
    
  

    <AuditReport audits={sampleAudits} />
    </div>
  );
}