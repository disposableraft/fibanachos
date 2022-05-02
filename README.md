In this example I build a small web app using Flask, Redis and Kubernetes. The app displays pages of emojis based on the Fibinacci sequence. For example, navigating to http://localhost:8000/10 will display 55 emojis. Each emoji is either a tree or a mushroom, depending on whether its index is a prime number.

It's assumed that minikube and kubectl are installed.

## Instructions

Start Minikube and confirm that it's running.

```shell
$ minikube start
$ minikube status
```

Build the `web:0.0.1` docker image inside minikube.

```shell
$ minikube image build -t web:0.0.1 .
```

Apply our deployments and service.

```shell
$ kubectl apply -f web-service.yaml,redis-deployment.yaml,web-deployment.yaml,redis-service.yaml,redis-config.yaml
```

Confirm services.

```shell
$ kubectl get services
```

Confirm the deployments.

```shell
$ kubectl get deployments
```

Confirm that pods are running.

```shell
$ kubectl get pods
```

If all is green, then forward the port.

```shell
$ kubectl port-forward service/web 8000 
```

