

import React from 'react';
import { ComplianceRecord } from "../../../types";

interface AuditReportProps {
  audits: ComplianceRecord[];
}

const AuditReport: React.FC<AuditReportProps> = ({ audits }) => {
  return (
    <div className="p-6 bg-white shadow-md rounded-lg">
      <h1 className="text-2xl font-semibold mb-4">Audit Report</h1>
      <table className="min-w-full bg-gray-100 border border-gray-300 rounded-lg">
        <thead>
          <tr className="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left">ID</th>
            <th className="py-3 px-6 text-left">Date</th>
            <th className="py-3 px-6 text-left">Application</th>
            <th className="py-3 px-6 text-left">Model</th>
            <th className="py-3 px-6 text-left">Compliance Area</th>
            <th className="py-3 px-6 text-left">Status</th>
            <th className="py-3 px-6 text-left">Comments</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {audits.map((audit) => (
            <tr key={audit.Id} className="border-b border-gray-200 hover:bg-gray-100">
              <td className="py-3 px-6">{audit.Id}</td>
              <td className="py-3 px-6">{audit.Date}</td>
              <td className="py-3 px-6">{audit.Application}</td>
              <td className="py-3 px-6">{audit.Model}</td>
              <td className="py-3 px-6">{audit.ComplianceArea}</td>
              <td className="py-3 px-6">{audit.Status}</td>
              <td className="py-3 px-6">{audit.Comments}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AuditReport;