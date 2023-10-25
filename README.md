# delivery5-MAPEK
Build MAPE-K conatiner for Kubernetes using existing components of K8s ecosystem.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- Python 3.x installed
- Docker (if containerizing the script)
- Access to a Kubernetes cluster
- Prometheus set up to collect custom metrics
- Dependencies listed in `requirements.txt`

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/your-project.git
```

2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

3. Configure environment variables to customize the behavior of the script. You can set the following environment variables:

* PROMETHEUS_URL: The URL for your Prometheus server.
* K8S_NAMESPACE: The Kubernetes namespace where your deployment is located.
* DEPLOYMENT_NAME: The name of the Kubernetes deployment you want to scale.

Example:

```bash
export PROMETHEUS_URL="http://your-prometheus-url"
export K8S_NAMESPACE="your-namespace"
export DEPLOYMENT_NAME="your-deployment"
```

4. Run the Python script:

```bash
python payment_MAPEK.py
```

The script will query custom metrics from Prometheus, evaluate the scaling logic, and scale the specified Kubernetes deployment if necessary.

### Docker Support
You can also containerize the script for use in a Docker container. A Dockerfile is included in the repository. To build the Docker image:

```bash
docker build -t my-python-app .
```

To run the container:
```bash
docker run -e PROMETHEUS_URL="http://your-prometheus-url" -e K8S_NAMESPACE="your-namespace" -e DEPLOYMENT_NAME="your-deployment" my-python-app
```
## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome. Please fork the repository and create a pull request with your changes.

## Acknowledgments
Mention any external libraries or tools used in your project.
Credit any authors or projects that inspired your work.
