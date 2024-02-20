# aws_nginx

This project is a automation deployed with GITHUB/GITLAB pipelines to create load balanced simple nginx hosted on AWS CloudFormation -> AWS CodeDeploy ->  Instance Amazon EC2


Application is written in main.py and uses a simple GET request to simulate the output.
![image](https://github.com/georgegohsh/aws_nginx/assets/73984288/668fc6ee-316e-42f7-a19a-e49cfeaa2822)


Subnets of /24 of 192.168.0.0 are created in the cloudformation/template.yaml file for AWS EC2 to intepret

![image](https://github.com/georgegohsh/aws_nginx/assets/73984288/52d71ff7-eda4-454b-bdbc-8b9e54e868b8)


SSH Key created in SSH Folder generated from CloudFormation on AWS CLI

![image](https://github.com/georgegohsh/aws_nginx/assets/73984288/1f7518ea-3dce-4eec-8944-d3301f116a67)


AWS Cloud Formation
![image](https://github.com/georgegohsh/aws_nginx/assets/73984288/cd6e0846-021e-4493-b516-5c4bfc2e2039)


AWS CodeDeploy Integrated with Github account
![image](https://github.com/georgegohsh/aws_nginx/assets/73984288/19cbef26-9d5c-4c84-8741-ba3deb66276c)



