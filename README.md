# AWS Overview

## What is AWS?

Amazon Web Services (AWS) is the world's leading cloud computing platform provided by Amazon. It offers hundreds of cloud services that allow organizations to build, deploy, and manage applications without owning physical infrastructure.

AWS follows a **pay-as-you-go** pricing model, allowing users to pay only for the resources they consume.

---
# Cloud Computing Service Models

Cloud services are generally divided into three categories:

## Infrastructure as a Service (IaaS)

Provides virtualized infrastructure such as virtual machines, networking, storage, and operating systems.

The customer is responsible for managing:
- Operating System
- Applications
- Runtime
- Data

The cloud provider manages:
- Physical servers
- Networking
- Storage
- Virtualization

**Examples**
- Amazon EC2
- Amazon VPC
- Amazon EBS
- Microsoft Azure VM
- Google Compute Engine

**When to use**
- Need full control over servers.
- Deploy custom applications.
- Build cloud infrastructure.

---
## Platform as a Service (PaaS)

Provides a managed platform for developing and deploying applications without managing servers.

The cloud provider manages:
- Infrastructure
- Operating System
- Runtime
- Middleware

The customer only manages:
- Application code
- Data

**Examples**
- AWS Elastic Beanstalk
- Google App Engine
- Azure App Service

**When to use**
- Focus on application development.
- Reduce operational overhead.

---
## Software as a Service (SaaS)

Provides complete software over the Internet.

Users simply use the application without managing any infrastructure.

**Examples**
- Google Workspace
- Microsoft 365
- Salesforce
- Dropbox

**When to use**
- Need ready-to-use software.
- No infrastructure management required.

---
# AWS Global Infrastructure

AWS operates a global infrastructure consisting of Regions, Availability Zones, and Edge Locations.

## Region

A Region is a **physical geographic location** where AWS operates multiple data centers.

Each Region is completely isolated from others.

**Examples**
- ap-southeast-1 (Singapore)
- ap-southeast-2 (Sydney)
- us-east-1 (N. Virginia)

### When to use

Choose the Region based on:

- Lowest latency
- Data residency requirements
- Service availability
- Cost optimization

For most applications, choose the Region closest to your users.

---
## Availability Zone (AZ)

An Availability Zone (AZ) is one or more physically separate data centers inside a Region.

Each Region contains multiple AZs connected by high-speed, low-latency networking.

Example:

```
Singapore Region
├── ap-southeast-1a
├── ap-southeast-1b
└── ap-southeast-1c
```

### Why use multiple AZs?

Deploying resources across multiple AZs improves:

- High Availability (HA)
- Fault Tolerance
- Disaster Recovery

If one AZ becomes unavailable, applications in another AZ can continue serving users.

---
## Edge Location

Edge Locations are AWS Points of Presence (PoPs) distributed worldwide.

They are mainly used by **Amazon CloudFront** and other edge services to cache content closer to end users.

### Benefits

- Lower latency
- Faster content delivery
- Reduced bandwidth usage
- Better global user experience

---
# Common AWS Service Categories

AWS provides hundreds of services. The most common categories include:

## Compute & Containers

Provide computing resources for applications.

Examples:
- Amazon EC2
- Elastic Beanstalk
- Amazon ECS
- Amazon EKS
- AWS Fargate

---
## Storage

Store files, block storage, and shared file systems.

Examples:
- Amazon S3
- Amazon EBS
- Amazon EFS
- AWS Storage Gateway

---
## Networking & Content Delivery

Provide networking and traffic management.

Examples:
- Amazon VPC
- Amazon Route 53
- Elastic Load Balancer (ELB)
- Amazon CloudFront

---
## Database

Managed database services.

Examples:
- Amazon RDS
- Amazon Aurora
- Amazon DynamoDB

---
## Security & Identity

Identity management and security services.

Examples:
- AWS IAM
- AWS KMS
- Amazon Cognito

---
## Monitoring & Management

Monitor resources and manage AWS environments.

Examples:
- Amazon CloudWatch
- AWS Config
- AWS CloudTrail

---
## Messaging & Application Integration

Communication between applications.

Examples:
- Amazon SNS
- Amazon SES
- Amazon SQS

---
## Deployment & Developer Tools

Support software development and CI/CD.

Examples:
- AWS Cloud9
- AWS CodeCommit
- AWS CodeBuild
- AWS CodeDeploy
- AWS CodePipeline
- AWS CDK
- AWS X-Ray

---
## Migration

Help migrate workloads to AWS.

Examples:
- AWS DMS
- AWS SMS

---
## Big Data & Analytics

Analyze large datasets.

Examples:
- Amazon Redshift
- Amazon QuickSight

---
## Artificial Intelligence & Machine Learning

Build AI and ML applications.

Examples:
- Amazon SageMaker
- Amazon Bedrock
- Amazon Rekognition
- Amazon Comprehend

---
# Key Takeaways

- AWS is the leading cloud computing platform.
- Cloud services are divided into **IaaS, PaaS, and SaaS**.
- A **Region** contains multiple **Availability Zones (AZs)**.
- Use multiple AZs to achieve **High Availability (HA)**.
- **Edge Locations** cache content closer to users for lower latency.
- AWS services are grouped into categories such as Compute, Storage, Networking, Database, Security, Monitoring, Analytics, and AI.

---
