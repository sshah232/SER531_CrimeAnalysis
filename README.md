# SER531_CrimeAnalysis

AWS Instance:
The instance is made on AWS which consists of AWS Linux-2 AMI, t2.micro with SSH, HTTP and HTTPS services enabled. This instance has a public key which is stored in the AWS folder named as new_dev.pem. This instance has Jena Fuseki and Java already installed in it. 

Steps for running the AWS instance. 
1) Open the terminal and write the command: ssh -i new_dev.pem ec2-user@ec2-18-216-173-36.us-east-2.compute.amazonaws.com
   The instance IP might be different when you will try to run it as the Free Tier of AWS doesn't keep the instance running for ever and kills it after some time. So, once I restart the instance, a new IP DNS would be assigned which can be replaced in place of "ec2-18-216-173-36.us-east-2.compute.amazonaws.com". Also, make sure appropriate permissions are given to the directory in which the public key is present. Run the cmd as administrator or write chmod 400 <<Directory_NAME>>. 
2) Once the Linux session is started, write the following commands:
    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
    cd apache-jena-fuseki-4.10.0
    ./fuseki-server
3) This will start the server on 3030 port. The URL will be similar to http://ec2-18-216-173-36.us-east-2.compute.amazonaws.com:3030/#/. (replace the DNS according to the instance). This has New_DS which contains the triples of our data. We have also attached the owl file with the instances/individuals loaded in it. Now, this url will be used to parse the SPARQL queries, get the triples and show the data. 
