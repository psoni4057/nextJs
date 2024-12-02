// types.ts
export interface Rule {
    description: string;
    example: string;
    id: number;
}

export interface ComplianceRecord {
    Id: number;
    Date: string;
    Application: string;
    Model: string;
    ComplianceArea: string;
    Status: string;
    Comments: string;
}