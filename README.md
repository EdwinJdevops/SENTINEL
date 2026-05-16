# SENTINEL — Kubernetes Security Scanning Platform

A production-grade security observability platform built on Kubernetes, combining vulnerability scanning, runtime threat detection, and compliance auditing into a unified risk pipeline.

---

## What This Does

SENTINEL continuously scans a Kubernetes cluster across three security dimensions:

| Layer | Tool | Result |
|---|---|---|
| Container CVE scanning | Trivy | 0 CVEs on nginx:latest |
| MITRE ATT&CK compliance | Kubescape | 80/100 — 10 controls flagged |
| Runtime threat detection | Falco | Syscall-level anomaly alerts |
| Metrics + Visualization | Prometheus + Grafana | Full observability dashboard |
| GitOps delivery | ArgoCD + GitHub Actions | Automated, auditable deploys |
| Infrastructure as Code | Terraform | Declarative namespace provisioning |

---

## Architecture

```mermaid
graph TD
    GH[GitHub Actions CI/CD] --> ARGO[ArgoCD]
    ARGO --> K8S[Minikube Cluster]
    K8S --> SEC[Security Namespace]
    K8S --> MON[Monitoring Namespace]
    SEC --> TRIVY[Trivy Scanner]
    SEC --> KUBESCAPE[Kubescape]
    SEC --> FALCO[Falco Runtime]
    MON --> PROM[Prometheus]
    MON --> GRAF[Grafana]
    TRIVY --> AGG[Python Aggregator]
    KUBESCAPE --> AGG
    FALCO --> AGG
    AGG --> PROM
Security Findings
Kubescape — MITRE ATT&CK Framework
Overall Score: 80/100
10 failed controls across 101 resources
Critical flags: Anonymous Kubelet access, TLS enforcement
Medium flags: Secret encryption at rest, Audit logging, CoreDNS poisoning vectors
Trivy — CVE Scan
Target: nginx:latest
Total CVEs: 0 — clean image baseline confirmed
JSON report: scan-results/trivy-report.json
Infrastructure — Terraform
Namespaces provisioned declaratively via Terraform Kubernetes provider:
resource "kubernetes_namespace" "monitoring" {
  metadata { name = "monitoring" }
}
resource "kubernetes_namespace" "security" {
  metadata { name = "security" }
}
resource "kubernetes_namespace" "argocd" {
  metadata { name = "argocd" }
}

cd terraform
terraform init
terraform plan
terraform apply

Stack
Kubernetes: Minikube
Security: Trivy, Kubescape, Falco
Observability: Prometheus, Grafana
GitOps: ArgoCD, GitHub Actions
IaC: Terraform (Kubernetes provider)
Aggregation: Python 3 (unified risk report parser)
Local Setup

# RAM fix required each session
minikube delete
systemctl restart docker
minikube start --driver=docker --force --memory=2200 --cpus=2

# Grafana access
kubectl port-forward -n monitoring svc/prometheus-grafana 3000:80

Scan Results
# Run CVE summary
python3 scan-results/summarize.py

# Re-run Kubescape
kubescape scan framework mitre --format json --output scan-results/kubescape-report.json

Repo Structure
SENTINEL/
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── scan-results/
│   ├── trivy-report.json
│   ├── kubescape-report.json
│   └── summarize.py
└── README.md
Built by Edwin Jonathan — 17-year-old self-taught DevOps Engineer from Lagos, Nigeria. No degree, no shortcuts — just real infrastructure, real pipelines, and real results.
🔗 GitHub: github.com/EdwinJdevops
✍️ Hashnode: edwinjonathand-devops.hashnode.dev
💼 Open to remote DevOps/Cloud roles globally
