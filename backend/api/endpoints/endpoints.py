
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from backend.core.config import ConfigRules

app = FastAPI()
configrules = ConfigRules.create_config()

class Rule(BaseModel):
    rules: str
    example: str

@app.post("/configrules/")
async def create_rule(rule: Rule):
    configrules.insert_rule(rule.rules, rule.example)
    return {"message": "Rule created successfully"}

@app.get("/configrules/")
async def get_all_rules():
    rules = configrules.get_all_rules()
    return {"rules": [{"id": rule[0], "rules": rule[1], "example": rule[2]} for rule in rules]}

@app.get("/configrules/{rule_name}")
async def get_rule(rule_name: str):
    rows = configrules.get_rule_by_name(rule_name)
    if not rows:
        raise HTTPException(status_code=404, detail=f"No rule found with name {rule_name}")
    return {"rules": [{"id": row[0], "rules": row[1], "example": row[2]} for row in rows]}

@app.delete("/configrules/{rule_name}")
async def delete_rule(rule_name: str):
    rows = configrules.get_rule_by_name(rule_name)
    if not rows:
        raise HTTPException(status_code=404, detail=f"No rule found with name {rule_name}")
    configrules.delete_rule(rule_name)
    return {"message": f"Rule {rule_name} deleted successfully"}

@app.get("/configrules/id/{rule_id}")
async def get_rule_by_id(rule_id: int):
    row = configrules.get_rule_by_name(rule_id)
    if row:
        return {"id": row[0], "rules": row[1], "example": row[2]}
    else:
        raise HTTPException(status_code=404, detail=f"No rule found with ID {rule_id}")

@app.put("/configrules/{rule_name}")
async def update_rule(rule_name: str, rule_update: Rule):
    updated = configrules.update_rule(rule_update.rules, rule_update.example)
    if updated:
        return {"message": f"Rule '{rule_update.rules}' updated successfully!"}
    else:
        raise HTTPException(status_code=404, detail=f"Rule '{rule_update.rules}' not found.")