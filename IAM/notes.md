# AWS Identity and Access Management (IAM)

## 1. What is IAM?

AWS Identity and Access Management (IAM) is a service used to control **authentication and authorization** in AWS.

IAM determines:

> **Who can access AWS and what actions they are allowed to perform.**

The main IAM components are:

* **User** – represents a person or application.
* **Group** – a collection of IAM users.
* **Role** – an AWS identity with temporary permissions that can be assumed.
* **Policy / Permission** – defines allowed or denied actions.

IAM is a **global service** and is not tied to a specific AWS Region.

---
## 2. When should I use IAM?

IAM is used whenever access to AWS resources needs to be controlled.

Common scenarios:

* Give developers access to specific AWS services.
* Allow an EC2 instance to access S3.
* Create different permissions for DevOps, Developers, and Admins.
* Provide temporary permissions to AWS services.
* Apply the Principle of Least Privilege.

---
## 3. Common Use Cases

* Allow an EC2 instance to read files from S3.
* Give developers access to EC2 but not IAM.
* Create an Admin group for administrators.
* Allow Lambda to write logs to CloudWatch.
* Provide temporary access using IAM Roles.
* Restrict access to specific AWS resources.

---
# IAM Policy

An IAM Policy is a JSON document that defines permissions.

A policy answers:

> **Who or what can perform which actions on which AWS resources?**

A policy can contain multiple `Statement` blocks.

Example:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```
## Policy Elements

### Effect

Defines whether the action is allowed or denied.

```text
Allow
Deny
```

An **Explicit Deny always overrides Allow**.

---
### Action

Defines which AWS API actions can be performed.

Example:

```text
s3:GetObject
ec2:StartInstances
ec2:StopInstances
```

---
### Resource

Defines which AWS resources the policy applies to.

Resources are usually identified using an **ARN (Amazon Resource Name)**.

Example:

```text
arn:aws:s3:::my-bucket/*
```

---
### Condition

Optional conditions that determine when the policy is applied.

Examples:

* Source IP address
* MFA authentication
* Request time
* Resource tags

---
# Types of IAM Policies

## Inline Policy

A policy embedded directly into a specific:

* User
* Group
* Role

Characteristics:

* Exists only with that IAM identity.
* Cannot be reused.
* Deleted when the identity is deleted.

Use Inline Policies for specific one-to-one permission requirements.

---
## Managed Policy

A standalone policy that can be attached to multiple:

* Users
* Groups
* Roles

Characteristics:

* Reusable.
* Easier to manage.
* Can be attached to multiple IAM identities.

Managed Policies include:

* AWS Managed Policies
* Customer Managed Policies

For most environments, **Managed Policies are preferred**.

---
# IAM User

An IAM User represents a person or application that needs long-term access to AWS.

By default, a new IAM User has **no permissions**.

Permissions must be granted through:

* IAM Policy
* IAM Group

An IAM User can have:

* AWS Management Console access
* Access Key
* Secret Access Key

Access Keys are commonly used with:

* AWS CLI
* AWS SDK
* Automation tools

Example:

```bash
aws configure
```

---
# IAM Group

An IAM Group is a collection of IAM Users.

Groups are used to manage permissions for multiple users.

Example:

```text
Developers Group
├── User A
├── User B
└── User C
```

Attach a policy to the group:

```text
Developers Group
        │
        ▼
EC2ReadOnly Policy
```

All users in the group receive the permissions.

## Important Rules

* A Group can contain multiple Users.
* A User can belong to multiple Groups.
* A User does not need to belong to a Group.
* Groups cannot contain other Groups.
* A Group may exist without any Users.

---
# IAM Role

An IAM Role is an AWS identity that provides **temporary permissions**.

Unlike IAM Users, Roles do not have long-term credentials such as permanent Access Keys.

A Role must be **assumed** by:

* AWS Services
* IAM Users
* Applications
* Other AWS Accounts

Example:

```text
EC2 Instance
      │
      ▼
Assume IAM Role
      │
      ▼
Temporary Credentials
      │
      ▼
Access S3
```

IAM Roles are commonly used for service-to-service communication.

---
# IAM Role for EC2

An EC2 instance should use an IAM Role when accessing other AWS services.

Example:

```text
EC2
 │
 │ IAM Role
 ▼
Amazon S3
```

The Role contains a policy such as:

```text
s3:GetObject
```

The EC2 instance can then access S3 without storing an Access Key or Secret Access Key on the server.

Example:

```bash
aws s3 ls
```

AWS automatically provides temporary credentials to the EC2 instance.

This is more secure than:

```text
Access Key
Secret Access Key
```

stored directly on the server.

---
# IAM Best Practices

* Do not use the AWS Root User for daily operations.
* Enable MFA for the Root User and IAM Users.
* Follow the **Principle of Least Privilege**.
* Grant only the permissions required for a task.
* Use IAM Groups to manage permissions for multiple Users.
* Prefer IAM Roles instead of long-term Access Keys.
* Never share IAM Users.
* Never share Access Keys or Secret Access Keys.
* Rotate credentials when necessary.
* Remove unused IAM Users, Roles, and Access Keys.

---
# Common Mistakes

* Giving `AdministratorAccess` to every user.
* Storing Access Keys directly in source code.
* Uploading credentials to GitHub.
* Using the Root User for daily tasks.
* Sharing one IAM User between multiple people.
* Using Access Keys on EC2 instead of IAM Roles.

---
# Key Takeaways

* IAM controls authentication and authorization in AWS.
* IAM Users represent identities with long-term access.
* IAM Groups simplify permission management for multiple Users.
* IAM Roles provide temporary permissions.
* IAM Policies define allowed or denied AWS actions.
* Explicit Deny always overrides Allow.
* New IAM Users have no permissions by default.
* Use IAM Roles for AWS service-to-service access.
* Always follow the Principle of Least Privilege.
