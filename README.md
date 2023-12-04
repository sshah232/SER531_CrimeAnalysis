# SER531_CrimeAnalysis

This project consists of making an ontology for the Crime data, creating triples using Cellfie, hosting the triples onto a cloud service(AWS in our case), querying the ontology using SPARQL and finally using this data to make graphs and bar charts for visualizing the crime happening in the nearby area and making the public aware and safe from the incidents.

Project Members:
Yugma Patel, 
Shubham Shah, 
Samit Shah, 
Swathi Revanasiddappa 

# AWS Instance:
The instance is made on AWS which consists of AWS Linux-2 AMI, t2.micro with SSH, HTTP and HTTPS services enabled. This instance has a public key which is stored in the AWS folder named as new_dev.pem. This instance has Jena Fuseki and Java already installed in it. We are currently using the Free Tier of AWS which kills the process after some amount of time and thus we cannot publish the triples forever and we had to host it again.

Steps for running the AWS instance. 
1) Open the terminal and write the command: ssh -i new_dev.pem ec2-user@ec2-18-216-173-36.us-east-2.compute.amazonaws.com
   The instance IP might be different when you will try to run it as the Free Tier of AWS doesn't keep the instance running for ever and kills it after some time. So, once I restart the instance, a new IP DNS would be assigned which can be replaced in place of "ec2-18-216-173-36.us-east-2.compute.amazonaws.com". Also, make sure appropriate permissions are given to the directory in which the public key is present. Run the cmd as administrator or write chmod 400 <<Directory_NAME>>.
   
2) Once the Linux session is started, write the following commands:
    export JAVA_HOME=/usr/lib/jvm/java-11-openjdk
    cd apache-jena-fuseki-4.10.0
    ./fuseki-server
   
3) This will start the server on 3030 port. The URL will be similar to http://ec2-18-216-173-36.us-east-2.compute.amazonaws.com:3030/#/. (replace the DNS according to the instance). This has New_DS which contains the triples of our data. We have also attached the .owl file(in the Ontologies folder) with the instances/individuals loaded in it. Now, this url will be used to parse the SPARQL queries, get the triples and show the data. 


# How to run the webapp

1) Install all the necessary libraries so that you do not get any import errors!
2) Navigate to "app.py" file and run the file using the command:
    python app.py
3) This will start the server on 8000 port. The URL will be similar to http://127.0.0.1:8000

The web app might not show data when you run the app.py as the AWS instance might not be running at that time. For this you can contact ypatel42@asu.edu via Email or Slack so that he can start the instance and then the output will be seen perfectly. 

Note: The suggestions put forth by Prof. Bansal were carefully considered, and after thoughtful deliberation, our team opted not to implement distinct and separate classes for Gender and Descent. This decision was made in light of our specific use case, where we felt that creating unique classes for these attributes might be unnecessary and could potentially introduce redundancy. As a result, we chose to retain Gender and Descent within the data properties, believing that this approach aligned better with the objectives of our project. We appreciate Prof. Bansal's insights and contributions to the discussion, and we value the collaborative exchange of ideas in refining our approach.
