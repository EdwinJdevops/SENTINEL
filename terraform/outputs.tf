output "monitoring_namespace" {
  value = kubernetes_namespace.monitoring.metadata[0].name
}

output "security_namespace" {
  value = kubernetes_namespace.security.metadata[0].name
}

output "argocd_namespace" {
  value = kubernetes_namespace.argocd.metadata[0].name
}
