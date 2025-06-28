
on kali you can run `sudo apt install awscli` to get an older version of aws cli
```sh
┌──(kali㉿proxli)-[/usr/bin]
└─$ sudo apt install awscli
awscli is already the newest version (2.23.6-1).
awscli set to manually installed.
...
```
meaning awscli is installed by default on full kali

to get a current version, follow the instructions below or at:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### Install
```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### Update

Find install location for the --bin-dir option
```sh
┌──(kali㉿proxli)-[~]
└─$ which aws          
/usr/bin/aws
```

use the default
```sh
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update
```

or just this to make is select it's default path
```sh
┌──(kali㉿proxli)-[~]
└─$ sudo ./aws/install --update
```

you can always rename the old file and the new one will be the default (assuming it's in the path too)
```sh
┌──(kali㉿proxli)-[/usr/local/bin]
└─$ ls -la aws*                  
lrwxrwxrwx 1 root root 37 Jun 23 16:48 aws -> /usr/local/aws-cli/v2/current/bin/aws
lrwxrwxrwx 1 root root 47 Jun 23 16:48 aws_completer -> /usr/local/aws-cli/v2/current/bin/aws_completer

┌──(kali㉿proxli)-[/usr/local/bin]
└─$ which aws
/usr/bin/aws
```

```sh
┌──(kali㉿proxli)-[/usr/bin]
└─$ ls -la aws*
-rwxr-xr-x 1 root root 815 Jan 25 07:02 aws

┌──(kali㉿proxli)-[/usr/bin]
└─$ sudo mv aws oldaws
[sudo] password for kali:

┌──(kali㉿proxli)-[/usr/bin]
└─$ aws --version
aws-cli/2.27.40 Python/3.13.4 Linux/6.12.25-amd64 exe/x86_64.kali.2025

┌──(kali㉿proxli)-[/usr/bin]
└─$ oldaws --version
aws-cli/2.23.6 Python/3.13.3 Linux/6.12.25-amd64 source/x86_64.kali.2025
```

### Adding autocomplete to zsh

(is you use bash, `complete -C '/usr/local/bin/aws_completer' aws` should have been added to your .bashrc by the installation)

for zsh users, edit .zshrc in your home directory

find the lines
```sh
autoload -Uz compinit
compinit -d ~/.cache/zcompdump
```

after the lines starting with zstyle, add these lines:
```sh
#Loads Zsh compatibility for Bash-style completion scripts
autoload bashcompinit && bashcompinit
#Tells the shell to use the `aws_completer` binary to generate tab completions for the `aws` command (Bash-style)
complete -C "/usr/local/bin/aws_completer" aws
```

After restarting zsh, we can autocomplete by pressing tab.
```sh
┌──(kali㉿proxli)-[~]
└─$ aws <tab here>
accessanalyzer                       keyspaces                          
account                              kinesis                            
acm                                  kinesisanalytics                   
acm-pca                              kinesisanalyticsv2                 
aiops                                kinesisvideo                       
amp                                  kinesis-video-archived-media       
amplify                              kinesis-video-media                
amplifybackend                       kinesis-video-signaling            
amplifyuibuilder                     kinesis-video-webrtc-storage       
apigateway                           kms                                
apigatewaymanagementapi              lakeformation                      
apigatewayv2                         lambda                             
appconfig                            launch-wizard                      
appconfigdata                        lex-models                         
appfabric                            lex-runtime                        
appflow                              lexv2-models                       
appintegrations                      lexv2-runtime                      
application-autoscaling              license-manager                    
applicationcostprofiler              license-manager-linux-subscriptions
application-insights                 license-manager-user-subscriptions 
application-signals                  lightsail                          
appmesh                              location                           
apprunner                            logs                               
appstream                            lookoutequipment                   
appsync                              lookoutmetrics                     
apptest                              lookoutvision                      
arc-zonal-shift                      m2                                 
artifact                             machinelearning                    
athena                               macie2                             
auditmanager                         mailmanager                        
autoscaling                          managedblockchain                  
autoscaling-plans                    managedblockchain-query            
b2bi                                 marketplace-agreement              
backup                               marketplace-catalog                
backup-gateway                       marketplacecommerceanalytics       
backupsearch                         marketplace-deployment             
batch                                marketplace-entitlement            
bcm-data-exports                     marketplace-reporting              
bcm-pricing-calculator               mediaconnect                       
bedrock                              mediaconvert                       
bedrock-agent                        medialive                          
bedrock-agent-runtime                mediapackage                       
bedrock-data-automation              mediapackagev2                     
bedrock-data-automation-runtime      mediapackage-vod                   
bedrock-runtime                      mediastore                         
billing                              mediastore-data                    
billingconductor                     mediatailor                        
braket                               medical-imaging                    
budgets                              memorydb                           
ce                                   meteringmarketplace                
chatbot                              mgh                                
chime                                mgn                                
chime-sdk-identity                   migrationhub-config                
chime-sdk-media-pipelines            migrationhuborchestrator           
chime-sdk-meetings                   migration-hub-refactor-spaces      
chime-sdk-messaging                  migrationhubstrategy               
chime-sdk-voice                      mpa                                
cleanrooms                           mq                                 
cleanroomsml                         mturk                              
cli-dev                              mwaa                               
cloud9                               neptune                            
cloudcontrol                         neptunedata                        
clouddirectory                       neptune-graph                      
cloudformation                       network-firewall                   
cloudfront                           networkflowmonitor                 
cloudfront-keyvaluestore             networkmanager                     
cloudhsm                             networkmonitor                     
cloudhsmv2                           notifications                      
cloudsearch                          notificationscontacts              
cloudsearchdomain                    oam                                
cloudtrail                           observabilityadmin                 
cloudtrail-data                      omics                              
cloudwatch                           opensearch                         
codeartifact                         opensearchserverless               
codebuild                            opsworks                           
codecatalyst                         opsworks-cm                        
codecommit                           opsworkscm                         
codeconnections                      organizations                      
codeguruprofiler                     osis                               
codeguru-reviewer                    outposts                           
codeguru-security                    panorama                           
codepipeline                         partnercentral-selling             
codestar-connections                 payment-cryptography               
codestar-notifications               payment-cryptography-data          
cognito-identity                     pca-connector-ad                   
cognito-idp                          pca-connector-scep                 
cognito-sync                         pcs                                
comprehend                           personalize                        
comprehendmedical                    personalize-events                 
compute-optimizer                    personalize-runtime                
configservice                        pi                                 
configure                            pinpoint                           
connect                              pinpoint-email                     
connectcampaigns                     pinpoint-sms-voice                 
connectcampaignsv2                   pinpoint-sms-voice-v2              
connectcases                         pipes                              
connect-contact-lens                 polly                              
connectparticipant                   pricing                            
controlcatalog                       proton                             
controltower                         qapps                              
cost-optimization-hub                qbusiness                          
cur                                  qconnect                           
customer-profiles                    qldb                               
databrew                             qldb-session                       
dataexchange                         quicksight                         
datapipeline                         ram                                
datasync                             rbin                               
datazone                             rds                                
dax                                  rds-data                           
ddb                                  redshift                           
deadline                             redshift-data                      
deploy                               redshift-serverless                
detective                            rekognition                        
devicefarm                           repostspace                        
devops-guru                          resiliencehub                      
directconnect                        resource-explorer-2                
discovery                            resource-groups                    
dlm                                  resourcegroupstaggingapi           
dms                                  robomaker                          
docdb                                rolesanywhere                      
docdb-elastic                        route53                            
drs                                  route53domains                     
ds                                   route53profiles                    
ds-data                              route53-recovery-cluster           
dsql                                 route53-recovery-control-config    
dynamodb                             route53-recovery-readiness         
dynamodbstreams                      route53resolver                    
ebs                                  rum                                
ec2                                  s3                                 
ec2-instance-connect                 s3api                              
ecr                                  s3control                          
ecr-public                           s3outposts                         
ecs                                  s3tables                           
efs                                  sagemaker                          
eks                                  sagemaker-a2i-runtime              
eks-auth                             sagemaker-edge                     
elasticache                          sagemaker-featurestore-runtime     
elasticbeanstalk                     sagemaker-geospatial               
elastictranscoder                    sagemaker-metrics                  
elb                                  sagemaker-runtime                  
elbv2                                savingsplans                       
emr                                  scheduler                          
emr-containers                       schemas                            
emr-serverless                       sdb                                
entityresolution                     secretsmanager                     
es                                   securityhub                        
events                               security-ir                        
evidently                            securitylake                       
evs                                  serverlessrepo                     
finspace                             servicecatalog                     
finspace-data                        servicecatalog-appregistry         
firehose                             servicediscovery                   
fis                                  service-quotas                     
fms                                  ses                                
forecast                             sesv2                              
forecastquery                        shield                             
frauddetector                        signer                             
freetier                             simspaceweaver                     
fsx                                  sms                                
gamelift                             snowball                           
gameliftstreams                      snow-device-management             
geo-maps                             sns                                
geo-places                           socialmessaging                    
geo-routes                           sqs                                
glacier                              ssm                                
globalaccelerator                    ssm-contacts                       
glue                                 ssm-guiconnect                     
grafana                              ssm-incidents                      
greengrass                           ssm-quicksetup                     
greengrassv2                         ssm-sap                            
groundstation                        sso                                
guardduty                            sso-admin                          
health                               sso-oidc                           
healthlake                           stepfunctions                      
history                              storagegateway                     
iam                                  sts                                
identitystore                        supplychain                        
imagebuilder                         support                            
importexport                         support-app                        
inspector                            swf                                
inspector2                           synthetics                         
inspector-scan                       taxsettings                        
internetmonitor                      textract                           
invoicing                            timestream-influxdb                
iot                                  timestream-query                   
iotanalytics                         timestream-write                   
iot-data                             tnb                                
iotdeviceadvisor                     transcribe                         
iotevents                            transfer                           
iotevents-data                       translate                          
iotfleethub                          trustedadvisor                     
iotfleetwise                         verifiedpermissions                
iot-jobs-data                        voice-id                           
iot-managed-integrations             vpc-lattice                        
iotsecuretunneling                   waf                                
iotsitewise                          waf-regional                       
iotthingsgraph                       wafv2                              
iottwinmaker                         wellarchitected                    
iotwireless                          wisdom                             
ivs                                  workdocs                           
ivschat                              workmail                           
ivs-realtime                         workmailmessageflow                
kafka                                workspaces                         
kafkaconnect                         workspaces-thin-client             
kendra                               workspaces-web                     
kendra-ranking                       xray 
```

---

### Help

Here are the most common `<command>`s used with the AWS CLI:

| `<command>`      | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| `s3`             | Interact with Amazon S3 (e.g., upload/download files).       |
| `ec2`            | Manage EC2 instances, security groups, key pairs, etc.       |
| `iam`            | Manage IAM users, roles, policies, and credentials.          |
| `sts`            | Security Token Service, often used for temporary creds.      |
| `cloudformation` | Deploy and manage CloudFormation stacks.                     |
| `ecr`            | Amazon Elastic Container Registry – manage Docker images.    |
| `ecs`            | Elastic Container Service – run and manage containers.       |
| `lambda`         | Manage AWS Lambda functions.                                 |
| `logs`           | Interact with CloudWatch Logs.                               |
| `configure`      | Set or view CLI configuration (access keys, region, format). |

---
*Chatgpt summarization*

##### 🌐 General & Global Utilities

```sh
aws configure
    set          # set configuration options (profile, region, output)
    get          # view current configuration
    list-profiles # list all profiles in config
    import       # import credentials/config from file

aws help        # shows top-level commands (services)
aws <command> help     # shows subcommands for a service
aws <command> <subcommand> help  # shows detailed options
```

##### 📂 Storage

```sh
aws s3         # high-level S3 commands for buckets & objects
    ls
    mb
    rb
    cp
    mv
    sync
    rm

aws s3api      # low-level S3 REST API operations
    create-bucket
    delete-bucket
    list-objects
    put-object
    get-object
    delete-object
    ...
```
