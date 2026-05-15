terraform {
  required_providers {
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.23"
    }
  }
}

provider "kubernetes" {
  config_path    = "~/.kube/config"
  config_context = "minikube"
}

resource "kubernetes_namespace" "monitoring" {
  metadata { name = "monitoring" }
}

resource "kubernetes_namespace" "security" {
  metadata { name = "security" }
}

resource "kubernetes_namespace" "argocd" {
  metadata { name = "argocd" }
}
