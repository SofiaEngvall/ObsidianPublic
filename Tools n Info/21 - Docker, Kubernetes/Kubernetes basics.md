
Creation started when one executable on one machine couldn't do the job. Microservices started being used.

Imagine a docker container being bogged down so another needs to be added.
Container orchestration system. DevSecOps.

Availability and scalability - No single point of failure. No bottle necks.

Duplicating:
- application
- db component
- other stuff/reqs
Load balancing
Scale down again when demands go down

Kubernetes is very flexible - run on almost anything

Popularity gives high compatibility

### Architecture

**Container** - One application/executable per container.

**Pod** - One or more containers. What's needed for one application to run. The applications functions are split into different containers, like one for the db.. And these are gathered into one pod. The pod share storage and network resources, almost as it it's on one machine.

**Node** - can be a virtual or physical machine
   Master node - Also called the control plane. Manages the worker nodes and pods.
   - Kube API Server -  The front end. Scalable = several instances can be run.
   - Etcd - Key/value data storage. All the information about the cluster configuration.
   - Kube Scheduler - Executes and manages jobs, like making sure new pods are assigned to nodes. Monitors resource states of applications and worker nodes.
   - Kube controller manager - Runs control processes, like a node controller checking if nodes go down, and then telling the scheduler to start new ones.
   - Cloud control manager - Handles external communication with a cloud provider.
   Worker node - One or more pods. All the things a service needs to run.
   - Kubelet - Makes sure containers are running in pods and that these are up and healthy. Gets instructions from the control manager.
   - 

**Cluster** - One or more nodes. The highest level.



