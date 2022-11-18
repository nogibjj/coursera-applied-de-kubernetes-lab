## Kubernetes examples

### Lab Minikube (based on official tutorial on https://kubernetes.io)

1.  Launch GitHub Codespace
2.  Run `minikube start` to start cluster
3.  Run `minikube dashboard --url` to view dashboard in a new terminal
4.  Hover over link and "follow link"
5.  Create a deployment:  `kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080`
6. View deployment: `kubectl get deployments`
7. View pods:  `kubectl get pods`
8. Create service and expose it: `kubectl expose deployment hello-node --type=LoadBalancer --port=8080`
9. View services:  `kubectl get services`
10. Curl the url shown, for example: `curl http://192.168.49.2:31839` or change to your URL.
11. Cleanup
```bash
kubectl delete service hello-node
kubectl delete deployment hello-node
minikube stop
````

## Task 2: Deploy with Kubernetes FastAPI app

1.  Push container to DockerHub (Optional): i.e. 
`docker build -t <hub-user>/<repo-name>[:<tag>]` and `docker push <hub-user>/<repo-name>:<tag>`
Example of a pushed FastAPI container here:  https://hub.docker.com/repository/docker/noahgift/fastapi-kube
2. `minikube start`
3. `minikube dashboard --url`
4. Hover over link and "follow link"
5. Create a deployment: `kubectl create deployment hello-fastapi --image=registry.hub.docker.com/noahgift/fastapi-kube`
6. View deployment: `kubectl get deployments`
7. Create service and expose it: `kubectl expose deployment hello-fastapi --type=LoadBalancer --port=8080`
8. View services:  `kubectl get service hello-fastapi`
9.  `minikube service hello-fastapi --url`
10. Curl web service: i.e. `curl http://192.168.49.2:31224`
11.  Cleanup
12. Cleanup
```bash
kubectl delete service hello-fastapi
kubectl delete deployment hello-fastapi
minikube stop
````

## Notes below

# fastapi-from-zero
A repository to demonstrate FastAPI

/docs get to swagger

![fastapi](https://user-images.githubusercontent.com/58792/192342466-e043cce7-c4f4-4811-9d0c-68fb884daadf.png)



## Docker

`docker build .`
`docker image ls` #find image
`docker run -p 127.0.0.1:8080:8080 93fa55efa692` <replace with your image>

### Cloud9 + ECR + App Runner

  ![continuous-delivery](https://user-images.githubusercontent.com/58792/192845522-09207ae8-0dfb-4d31-b0a3-d396765d0db7.png)


* Clone repo into Cloud9 (pick a machine with decent size CPU and RAM if possible, but students should use micro)
* Add ssh keys to GitHub
* [resize to bigger disk](https://gist.github.com/wongcyrus/a4e726b961260395efa7811cab0b4516)
* Create virtualenv and add to bashrc and source
`python3 -m venv ~/.venv && echo 'source ~/.venv/bin/activate' >> ~/.bashrc && source ~/.bashrc`
* cd into checkout and run `make install`
* Preview running FastAPI app after running:  python main.py

<img width="1835" alt="Screen Shot 2022-09-28 at 12 32 52 PM" src="https://user-images.githubusercontent.com/58792/192836641-cd7ef757-4a4b-4722-bb17-d88980f4e9d4.png">

 * Create ECR repository by right-click in Cloud9
 
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 34 44 PM" src="https://user-images.githubusercontent.com/58792/192837619-b4ebd0fc-d464-4c06-a382-0a25c6028579.png">

* Navigate to ECR repo created <cdfastapi> or whatever you named it and follow "push" instructions
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 36 45 PM" src="https://user-images.githubusercontent.com/58792/192838151-ca89bdc1-bb99-40dc-ace1-f059e07ba5f6.png">

* Navigate to AWS App Runner and Setup Continuous Delivery using ECR
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 41 21 PM" src="https://user-images.githubusercontent.com/58792/192839558-7f1f0e55-7f5b-4af6-99f1-66d0512a41d6.png">

* Setup AWS Code Build to push container after each build (which triggers auto-deploy)  
  
  <img width="1835" alt="Screen Shot 2022-09-28 at 12 50 19 PM" src="https://user-images.githubusercontent.com/58792/192843483-e0a48ae6-95c1-4758-8928-40c33939cb9f.png">

  
See following [buildspec.yml](https://github.com/nogibjj/fastapi-from-zero/blob/main/buildspec.yml)
and [Makefile](https://github.com/nogibjj/fastapi-from-zero/blob/main/Makefile)
  
## References

* [FastAPI Docker docs](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
* [Hello minikube](https://kubernetes.io/docs/tutorials/hello-minikube/)
* [Reference](https://kubernetes.io/blog/2019/07/23/get-started-with-kubernetes-using-python/)