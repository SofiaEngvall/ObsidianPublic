(chatgpt generated)

# AWS CLI v2 Full Command Reference

This document is auto-generated from AWS CLI v2 documentation.

---

## Global Utilities

### configure  
Manage AWS CLI configuration properties.  
- `set`: Set configuration options (profile, region, output) :contentReference[oaicite:2]{index=2}  
- `get`: View current configuration values (not documented but implied)  
- `list-profiles`: List all configured profiles :contentReference[oaicite:3]{index=3}  
- `import`: Import credentials/config from a file :contentReference[oaicite:4]{index=4}  

### help  
Display high-level help text.

---

## Storage

### s3  
High-level S3 commands:
- `ls`: List objects and buckets  
- `mb`: Make bucket  
- `rb`: Remove bucket  
- `cp`: Copy files to/from S3  
- `mv`: Move/rename files  
- `sync`: Sync directories and buckets  
- `rm`: Remove objects

### s3api  
Low-level S3 REST API operations:
- `create-bucket`: Create an S3 bucket  
- `delete-bucket`: Delete an S3 bucket  
- `list-objects`: List objects in a bucket  
- `put-object`: Upload an object  
- `get-object`: Download an object  
- `delete-object`: Delete an object

---
## Compute

### ec2  
Manage virtual machine instances, security groups, key pairs, and network resources.  
- `describe-instances`: Display information about EC2 instances  
- `run-instances`: Launch new EC2 instances  
- `start-instances`: Start stopped instances  
- `stop-instances`: Stop running instances  
- `terminate-instances`: Terminate EC2 instances  
- `describe-security-groups`: View security group details  
- `authorize-security-group-ingress`: Add inbound rule to a security group  
- `revoke-security-group-ingress`: Remove inbound rule from a security group  
- `create-key-pair`: Create a new SSH key pair  
- `delete-key-pair`: Delete an existing key pair  
- `describe-key-pairs`: List key pairs

### autoscaling  
Manage EC2 Auto Scaling groups and configurations.  
- `create-auto-scaling-group`: Create a scaling group  
- `update-auto-scaling-group`: Modify a scaling group  
- `delete-auto-scaling-group`: Remove a scaling group  
- `describe-auto-scaling-groups`: View scaling group details

---

## Containers

### ecs  
Manage Elastic Container Service clusters, tasks, and services.  
- `list-clusters`: List ECS clusters  
- `create-cluster`: Create a new ECS cluster  
- `describe-clusters`: Show ECS cluster details  
- `list-services`: List services in a cluster  
- `create-service`: Deploy a containerized service  
- `update-service`: Update running services  
- `delete-service`: Remove a service  
- `run-task`: Run a one-off task  
- `stop-task`: Stop a running task

### ecr  
Manage container image repositories in Amazon ECR.  
- `create-repository`: Create a new image repository  
- `delete-repository`: Delete an image repository  
- `list-images`: List images in a repository  
- `describe-images`: Show image metadata  
- `batch-get-image`: Retrieve image details  
- `delete-image`: Remove an image from a repo

---

## Identity & Access

### iam  
Manage users, groups, roles, and policies.  
- `create-user`: Create a new IAM user  
- `delete-user`: Remove an IAM user  
- `list-users`: List IAM users  
- `create-group`: Create a new IAM group  
- `add-user-to-group`: Add a user to a group  
- `remove-user-from-group`: Remove a user from a group  
- `list-groups`: List groups  
- `create-role`: Create a new IAM role  
- `delete-role`: Delete a role  
- `list-roles`: List all roles  
- `attach-user-policy`: Attach a policy to a user  
- `detach-user-policy`: Detach a policy from a user  
- `attach-group-policy`: Attach a policy to a group  
- `detach-group-policy`: Detach a policy from a group

### sts  
Access temporary credentials and caller identity.  
- `get-caller-identity`: Show identity for current credentials  
- `assume-role`: Assume an IAM role and return temporary creds  
- `get-session-token`: Request temporary credentials

---

## Serverless

### lambda  
Manage AWS Lambda functions for serverless compute.  
- `list-functions`: List deployed Lambda functions  
- `create-function`: Create a new Lambda function  
- `update-function-code`: Update the source code of a function  
- `invoke`: Run a Lambda function  
- `delete-function`: Remove a function

### apigateway  
Create and manage REST APIs using Amazon API Gateway.  
- `get-rest-apis`: List APIs  
- `create-rest-api`: Create a new REST API  
- `delete-rest-api`: Delete an API  
- `import-rest-api`: Import an API using OpenAPI definitions  
- `create-deployment`: Deploy a REST API

---

## Networking

### elbv2  
Manage Application Load Balancers and Network Load Balancers.  
- `create-load-balancer`: Create a new load balancer  
- `delete-load-balancer`: Delete a load balancer  
- `describe-load-balancers`: List load balancers  
- `create-target-group`: Define a group of targets  
- `register-targets`: Add targets to a group  
- `deregister-targets`: Remove targets from a group

### route53  
Manage DNS zones and records with Route 53.  
- `list-hosted-zones`: List all hosted zones  
- `create-hosted-zone`: Create a DNS zone  
- `delete-hosted-zone`: Delete a DNS zone  
- `change-resource-record-sets`: Add/edit/delete DNS records  
- `list-resource-record-sets`: View DNS records in a zone

---

## Monitoring & Logs

### logs  
Manage CloudWatch Logs groups and streams.  
- `create-log-group`: Create a log group  
- `describe-log-groups`: List log groups  
- `delete-log-group`: Remove a log group  
- `create-log-stream`: Create a stream in a group  
- `put-log-events`: Send log data  
- `describe-log-streams`: List streams in a group

### cloudwatch  
Collect and view metrics, set alarms.  
- `list-metrics`: Show available CloudWatch metrics  
- `get-metric-data`: Query multiple metrics at once  
- `put-metric-data`: Push custom metric values  
- `put-metric-alarm`: Create a CloudWatch alarm  
- `describe-alarms`: List existing alarms  
- `delete-alarms`: Remove alarms

---

## Databases

### rds  
Manage relational databases (MySQL, PostgreSQL, etc.).  
- `describe-db-instances`: List DB instances  
- `create-db-instance`: Launch a new DB instance  
- `delete-db-instance`: Delete a DB instance  
- `start-db-instance`: Start a stopped instance  
- `stop-db-instance`: Stop a running instance  
- `modify-db-instance`: Change DB config  
- `reboot-db-instance`: Restart a DB instance

### dynamodb  
Work with the managed NoSQL database service.  
- `list-tables`: Show all tables  
- `create-table`: Define a new table  
- `delete-table`: Remove a table  
- `put-item`: Add or overwrite an item  
- `get-item`: Retrieve an item by key  
- `scan`: Retrieve all items  
- `query`: Run indexed queries  
- `update-item`: Modify an existing item  
- `delete-item`: Remove an item

### redshift  
Manage data warehouses and clusters.  
- `describe-clusters`: List Redshift clusters  
- `create-cluster`: Launch a new cluster  
- `delete-cluster`: Remove a cluster  
- `reboot-cluster`: Restart a cluster  
- `modify-cluster`: Update cluster settings

---

## Messaging & Queuing

### sns  
Simple Notification Service: publish/subscribe messaging.  
- `list-topics`: View existing topics  
- `create-topic`: Make a new topic  
- `publish`: Send a message to a topic  
- `subscribe`: Add an endpoint to a topic  
- `unsubscribe`: Remove a subscription  
- `delete-topic`: Remove a topic

### sqs  
Simple Queue Service for decoupled message passing.  
- `list-queues`: Show available queues  
- `create-queue`: Define a new queue  
- `send-message`: Add a message to a queue  
- `receive-message`: Read from a queue  
- `delete-message`: Remove a message  
- `delete-queue`: Remove a queue  
- `purge-queue`: Clear all messages

---

## Analytics

### athena  
Query S3 data with SQL.  
- `start-query-execution`: Run a SQL query  
- `get-query-results`: Fetch results of a query  
- `list-query-executions`: View recent queries

### glue  
ETL service for structured/unstructured data.  
- `create-database`: Define a new Glue catalog DB  
- `create-table`: Register table metadata  
- `start-job-run`: Launch an ETL job  
- `get-job-run`: View ETL job status  
- `delete-table`: Remove a table from the catalog

### opensearch  
Search and analytics engine (formerly Elasticsearch).  
- `list-domain-names`: Show search domains  
- `create-domain`: Launch an OpenSearch domain  
- `describe-domain`: View domain settings  
- `delete-domain`: Remove a search domain

---

## Management & Governance

### cloudformation  
Define and deploy infrastructure as code.  
- `create-stack`: Launch resources from a template  
- `update-stack`: Modify an existing stack  
- `delete-stack`: Remove a stack  
- `describe-stacks`: View stack details  
- `list-stacks`: Show stack history  
- `wait`: Block until a stack reaches a status (e.g. `stack-create-complete`)

### organizations  
Manage multi-account AWS setups.  
- `list-accounts`: List member accounts  
- `create-account`: Add a new AWS account  
- `invite-account-to-organization`: Bring external account into the org  
- `remove-account-from-organization`: Detach a member account

### budgets  
Define spending limits and alerts.  
- `create-budget`: Set a new budget  
- `describe-budget`: View budget details  
- `update-budget`: Modify an existing budget  
- `delete-budget`: Remove a budget

---

## Security & Compliance

### kms  
Key Management Service for encryption keys.  
- `list-keys`: Show KMS keys  
- `create-key`: Generate a new key  
- `enable-key`: Reactivate a key  
- `disable-key`: Disable use of a key  
- `schedule-key-deletion`: Schedule permanent deletion  
- `encrypt`: Encrypt data  
- `decrypt`: Decrypt data

### acm  
Manage SSL/TLS certificates.  
- `list-certificates`: View all managed certs  
- `request-certificate`: Request a new public cert  
- `describe-certificate`: View cert metadata  
- `delete-certificate`: Remove a cert  
- `export-certificate`: Retrieve a private key (for eligible certs)

### cloudtrail  
Audit API calls and account activity.  
- `create-trail`: Start tracking AWS events  
- `start-logging`: Begin logging events  
- `stop-logging`: Pause logging  
- `lookup-events`: Search logs  
- `delete-trail`: Remove an audit trail

---

## Backup & Archive

### backup  
Centralized backup across services.  
- `create-backup-plan`: Define backup rules  
- `start-backup-job`: Trigger backup manually  
- `list-backup-plans`: View available plans  
- `list-recovery-points-by-backup-vault`: View saved backups  
- `restore-backup`: Start a restore job

### glacier  
Long-term archival storage.  
- `create-vault`: Create a cold-storage vault  
- `upload-archive`: Store a file  
- `initiate-job`: Begin a restore or inventory task  
- `get-job-output`: Download data  
- `delete-vault`: Remove a vault

---

## DevOps & Tools

### codecommit  
Managed Git repositories.  
- `list-repositories`: Show repositories  
- `create-repository`: Add a new repo  
- `get-repository`: View repo metadata  
- `delete-repository`: Remove a repo

### codebuild  
Run builds in managed containers.  
- `list-projects`: View build projects  
- `start-build`: Begin a build  
- `stop-build`: Cancel a build  
- `batch-get-builds`: Retrieve build details  
- `create-project`: Define a new build config

### codedeploy  
Automate code deployments.  
- `create-application`: Define a deployable app  
- `create-deployment`: Launch a deployment  
- `get-deployment`: View deployment status  
- `stop-deployment`: Cancel an in-progress deployment

### codepipeline  
Automate CI/CD pipelines.  
- `list-pipelines`: Show configured pipelines  
- `get-pipeline`: View pipeline config  
- `start-pipeline-execution`: Trigger a run  
- `delete-pipeline`: Remove a pipeline

---

## Specialized Services

### location  
Maps, tracking, and geolocation APIs.  
- `create-map`: Define a new map  
- `list-maps`: Show available maps  
- `describe-map`: View map details  
- `delete-map`: Remove a map  
- `search-place-index-for-text`: Geocode a location string

### groundstation  
Satellite communications service.  
- `list-dataflow-endpoint-groups`: View endpoint groups  
- `create-mission-profile`: Define satellite pass configs  
- `reserve-contact`: Schedule a satellite link  
- `cancel-contact`: Cancel a reserved session


