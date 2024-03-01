
# Welcome to your CDK Python project create an s3 bucket with AWS CDK!

This is a blank project for CDK development with Python.

### *step1* :

 1. Install AWS CLI and configure

### *step2* : 

 2. nvm installer

In your terminal, run the nvm installer like this:

```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# or

wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
```


#Update your profile configuration

The installation process from step 1 should also automatically add the nvm configuration to your profile. If you're using zsh, that would be `~/.zshrc`. If you're using bash, that would be `~/.bash_profile`...or some other profile.

If it doesn't automatically add nvm configuration, you can add it yourself to your profile file:

```bash
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

#Reload the shell configuration

```bash
nvm -v
```

You can install Node versions like this:

```bash
nvm install latest
```

This command will install the last version of Node:

```bash
nvm install vX.Y.Z
```

This will install the `X.Y.Z` Node version.

And if you want to use a specific version at any point, you can run the following in your terminal:

```bash
nvm use vA.B.C
```

NVM makes it easier to manage multiple versions of Node.js across different projects that require different versions.

### *step3* :

Install aws-cdk package using the below command.

```bash
npm install -g aws-cdk`
```

To see whether the CDK is installed, run the below command.

```bash
cdk --version
```

### *step4* :

Create an s3 bucket

AWS S3 (AWS Simple Storage Service) is an [object storage](https://en.wikipedia.org/wiki/Object_storage) service by AWS. We can create buckets in S3 where we can store data and files.

Let’s write code for creating an s3 bucket.

- Create a new folder for our project.

```bash
mkdir medium-awscdk
```

- Go to the project folder we just created and then create a CDK project in that folder.

```bash
cd medium-awscdk
```

```bash
cdk init app --language python`
```

Run the following commands to create and activate the virtual environment. We will be installing the required python modules in this virtual environment.

```bash
python3 -m venv .venv 
```

```bash
source .venv/bin/activate
```


Let’s install the needed dependencies using the requirements.txt by running the below command.

```bash
pip install -r requirements.txt
```


### *step5* :

 Create an S3 bucket


Go to the folder and open the file with the prefix ‘_stack’. (Here, it’s _medium_awscdk_stack.py_)

![[Pasted image 20240301153646.png]]

We need the ‘aws_s3’ module to create an s3 bucket, so we import it from aws_cdk.

```python
from aws_cdk import (  
    Stack,  
    aws_s3 as s3  
)
```

The cloud formation stack is defined in the python Class. (here, the class name is ‘MediumAwscdkStack’)

```python
class MediumAwscdkStack(Stack):  
  
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:  
        super().__init__(scope, construct_id, **kwargs)
```
We can define the AWS resources we wanted to create in the init method of the class.

In the init method, add the following code where we define an s3 bucket using `s3.Bucket(...)`.

```python
s3.Bucket(  
  self,   
  id="bucket123",   
  bucket_name="BUCKET_NAME" # Provide a bucket name here  
)
```

We need to provide an _id_ for each resource we create in CDK. (Here, I give the id as ‘bucket123’. This is a required parameter.

You can also name your bucket with the _bucket_name_ parameter. It is an optional parameter. (Here, I name the bucket ‘_sharmi-bucket123_’).  
Note that the bucket name should be globally unique.

#The final code looks like this:

```python
from aws_cdk import (
    Stack,
    aws_s3 as s3
)
from constructs import Construct

class MediumAwscdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        s3.Bucket(
            self, 
            id="bucket123", 
            bucket_name="sharmi-bucket123"
        )
```


### *step6* : 

Our code is now ready to be deployed.



```bash
(.venv)
      cdk ls
```

The command `cdk ls` is used to display the list of stacks we have configured in the project. If there’s any syntactical error in the code, this command won't display the stacks and throws the error.


We have only created one stack in our project. (Here, _MediumAwscdkStack_) We can have multiple stacks with different purposes.

Now, the next step is to convert our code to a CloudFormation template which could be deployed to the AWS Cloud. The below command helps here with this.

```zsh
cdk synth
```

***The above command also displays an overview of the resources that would be created when we deploy the code. We can check the resources and their properties here, before deploying.***


The next step is to deploy this stack to the AWS Cloud. But to accomplish this, we need the necessary resources (**CDK toolkit)** deployed to the cloud formation service. This process is called bootstrapping. (More details [here](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)).

Run the below command to deploy the CDK Toolkit to CloudFormation.

```zsh
cdk bootstrap
```

***_Note:_ The above command does not have to be executed before each deployment. Once the toolkit is deployed to CloudFormation, you can deploy as many stacks as you want.***



##### We are now ready to deploy our stack which creates an s3 bucket.

Run the command `cdk deploy` to deploy.

```zsh
cdk deploy
```

The command executes without errors if the stack is deployed successfully.

Let’s visit the AWS Console to check whether our stack is deployed. In the AWS Console, go to the _CloudFormation_ service.

On the CloudFormation page, we can see our stack being deployed. (You would also find the [CDK Toolkit stack](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) which was also deployed as a stack when we ran the `cdk bootstrap` command).


Click on the stack we created (here, _MediumAwscdkStack_). And go to the resources tab to view all the resources deployed by the stack.


n this way, we can code our infrastructure using AWS CDK and deploy it in the AWS cloud.

To destroy all the resources in the stack, the below command is used.

```szh
cdk destroy
```

The `cdk destroy` command deletes the stack (_MediumAwscdkStack_) from the AWS along with any resources created by this stack.

So, the stack will be removed from CloudFormation. But, if you go to the S3 service, you will still see the bucket that was created.

It’s because the S3 buckets have the _removal policy_ as _retain_ by default_._ You can provide the _removal policy_ as _destroy_ for the s3 bucket if you want the bucket to be deleted when the corresponding stack is deleted.

```python
from aws_cdk import (  
    Stack,  
    aws_s3 as s3,  
    RemovalPolicy    # <-Import RemovalPolicy from aws_cdk  
)  
  
# ...  
# ...  
  
      s3.Bucket(  
        self,   
        id="bucket123",   
        bucket_name="sharmi-bucket123",  
        removal_policy=RemovalPolicy.DESTROY # <-Add the parameter  
      )
```

### _Note:_

Some properties of S3 and other resources cannot be modified after creation. So, if we are trying to make any change in the resource’s settings, a new resource will be created with the revised properties and the old one will be deleted. (For S3 buckets, a new bucket will be created with the new settings and the old bucket will be removed). But, when the removal policy is `_retain_`, the old resource will be retained and **not deleted**. It is the default option to avoid any loss of data in case the s3 bucket properties are modified accidentally.


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk destroy`     command deletes the stack
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation


I hope this article helped you!

Sincerely, Alexander.
