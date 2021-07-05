# elem-peach
Peachy time summer is eh? 🍑🍑

# Objective
Present a solution for [Exercise](docs/exercise.pdf)

## Building the App Docker image
```
cd <repo_directory>/rickandmorty
docker build -t rickandmorty .
```

## Running the App locally
```
docker run -p 5000:5000 rickandmorty
```
## App Functionality
1. To get all the live Humans from Earth  
Access the link **`http://localhost:5000/find-live-humans`** in a browser, or use CURL command
```
    curl http://localhost:5000/find-live-humans
```

2. To display the Live Humans from the csv file:  
Access the link **`http://localhost:5000/csv`** in a browser, or use CURL command
```
    curl http://localhost:5000/csv
```

3. To check the application is healthy and running:  
Access the link **`http://localhost:5000/healthcheck`** in a browser, or use CURL command
```
    curl http://localhost:5000/healthcheck
```

## Deploy App to Kubernetes
```
cd <REPOSITORY_ROOT>
kubectl apply -f yamls
kubectl port-forward service/rickandmorty 5000
```
Then you can access the application on `localhost:5000`
