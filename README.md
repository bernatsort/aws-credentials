# How to configure AWS temporary credentials

## Federated identity
[https://docs.aws.amazon.com/cli/latest/userguide/security-iam.html]

As a best practice, require human users, including users that require administrator access, to use federation with an identity provider to access AWS services by using temporary credentials.

A federated identity is a user from your enterprise user directory, a web identity provider, the AWS Directory Service, the Identity Center directory, or any user that accesses AWS services by using credentials provided through an identity source. When federated identities access AWS accounts, they assume roles, and the roles provide temporary credentials.

For centralized access management, we recommend that you use AWS IAM Identity Center. You can create users and groups in IAM Identity Center, or you can connect and synchronize to a set of users and groups in your own identity source for use across all your AWS accounts and applications. For information about IAM Identity Center, see What is IAM Identity Center? in the AWS IAM Identity Center User Guide.


## IAM users and groups
[https://docs.aws.amazon.com/cli/latest/userguide/security-iam.html]

An IAM user is an identity within your AWS account that has specific permissions for a single person or application. Where possible, we recommend relying on temporary credentials instead of creating IAM users who have long-term credentials such as passwords and access keys. 
However, if you have specific use cases that require long-term credentials with IAM users, we recommend that you rotate access keys. For more information, see Rotate access keys regularly for use cases that require long-term credentials in the IAM User Guide (Update access keys when needed for use cases that require long-term credentials: [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials]).


## Configuring credentials
[https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html] 
Boto3 will look in several locations when searching for credentials. The mechanism in which Boto3 looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which Boto3 searches for credentials is:

1. Passing credentials as parameters in the boto.client() method

2. Passing credentials as parameters when creating a Session object

3. Environment variables

4. Shared credential file (~/.aws/credentials)

5. AWS config file (~/.aws/config)

6. Assume Role provider

7. Boto2 config file (/etc/boto.cfg and ~/.boto)

8. nstance metadata service on an Amazon EC2 instance that has an IAM role configured.

Each of those locations is discussed in more detail below.



Temporary credentials obtained by using the root user credentials have a maximum duration of 3600 seconds (1 hour). 

Automated Systems: CI/CD pipelines, like Jenkins, benefit from temporary credentials because they can securely obtain and use short-lived credentials for the duration of the build process. 
