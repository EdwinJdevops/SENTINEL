import json
from datetime import datetime

def parse_trivy(path):
    with open(path) as f:
        data = json.load(f)
    counts = {"CRITICAL":0,"HIGH":0,"MEDIUM":0,"LOW":0}
    for result in data.get("Results", []):
        for v in result.get("Vulnerabilities") or []:
            sev = v.get("Severity","LOW")
            counts[sev] = counts.get(sev,0) + 1
    return counts

def parse_kubescape(path):
    with open(path) as f:
        data = json.load(f)
    score = data.get("complianceScore", "N/A")
    return {"compliance_score": score}

def generate_report():
    trivy = parse_trivy("/tmp/trivy-results.json")
    kubescape = parse_kubescape("/tmp/kubescape-results.json")
    report = {
        "timestamp": datetime.utcnow().isoformat(),
        "trivy": trivy,
        "kubescape": kubescape,
        "risk_level": "CRITICAL" if trivy["CRITICAL"] > 0 else "HIGH" if trivy["HIGH"] > 5 else "MEDIUM"
    }
    print(json.dumps(report, indent=2))
    with open("/tmp/sentinel-report.json","w") as f:
        json.dump(report, f, indent=2)

generate_report()
