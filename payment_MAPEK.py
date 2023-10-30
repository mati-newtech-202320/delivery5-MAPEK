import os
import time
import random

from kubernetes import client, config
import requests
from prometheus_api_client import PrometheusConnect

# Retrieve environment variables or set default values
prometheus_url = os.environ.get('PROMETHEUS_URL', 'https://prometheus-k8s-openshift-monitoring.apps.rosa-bmwnq.bjni.p1.openshiftapps.com')
k8s_namespace = os.environ.get('K8S_NAMESPACE', 'juank1400-dev')
deployment_name = os.environ.get('DEPLOYMENT_NAME', 'python-basic')
threshold = os.environ.get('THRESHOLD', '0.000505')

def get_custom_metric_value():

    # Crea una instancia de PrometheusConnect
    prometheus = PrometheusConnect(url=prometheus_url)

    # Realiza una consulta de ejemplo
    query = "sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{namespace='{"+k8s_namespace+"}'}) by (pod)"
    result = prometheus.custom_query(query)

    # Make an HTTP request to the Prometheus API using the environment variable
    # response = requests.get(prometheus_url+"/api/v1/query?query=sum(node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate{namespace='{"+k8s_namespace+"}'}) by (pod)")
    # data = response.json()

    return float(result['data']['result'][0]['value'][1])  # Extract the metric value

def scale_deployment(namespace, deployment_name, replicas):
    try:
        # Load Kubernetes configuration
        config.load_incluster_config()

        api_instance = client.AppsV1Api()
        deployment = api_instance.read_namespaced_deployment(
            name=deployment_name,
            namespace=namespace
        )

        # Update the number of replicas
        deployment.spec.replicas = deployment.spec.replicas + replicas

        # Apply the changes
        api_instance.replace_namespaced_deployment(
            name=deployment_name,
            namespace=namespace,
            body=deployment
        )
        print(f"Deployment '{deployment_name}' scaled to {replicas} replicas.")
    except Exception as e:
        print(f"Error: {str(e)}")

def mapek(k8s_namespace, deployment_name):
    while True:
        # custom_metric_value = get_custom_metric_value()
        custom_metric_value = 0.00045 + 0.0001*float(random.randrange(1, 100, 1))

        # Define scaling logic based on custom metric value
        if custom_metric_value > float(threshold):
            desired_replicas = 1 

            # Scale the deployment based on the custom metric
            scale_deployment(k8s_namespace, deployment_name, desired_replicas)
        else:
            if custom_metric_value < float(threshold)*1.01:
                desired_replicas = -1 

                # Scale the deployment based on the custom metric
                scale_deployment(k8s_namespace, deployment_name, desired_replicas)
            else:
                print(f"Don't configuration changes required.")
        time.sleep(30)


if __name__ == "__main__":
    mapek(k8s_namespace, deployment_name)