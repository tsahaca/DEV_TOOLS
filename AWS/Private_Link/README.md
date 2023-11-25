# Private Link | VPC Endpoint Service | VPC Endpoint

Suppose there is a website xyz.com that I am hosting in a bunch of Ec2 instances, exposed to the outside world thru a Network load balancer. Now, a client who has his/her own AWS account, wants to access this xyz.com from an Ec2 running in their aws account.

One approach is to go thru the Internet. However the client wants to avoid the internet route. He/she wants to use the AWS backbone to reach xyz.com. The technology that enables that, is AWS Private link. (note that if you search for Private Link in the AWS services, there will be none. You will get "End point services" as the closest hit)

So, this is how to route traffic through the AWS backbone:

I, the owner of xyz.com, will create a VPC End Point Service (NOTE the keyword Service here) The VPC End point service will point to my Network load balancer. I will then give my VPC End point service name to the client.
The client will create a VPC End Point (NOTE.. this is different from #1). While creating it, the client will specify the VPC End Point Service name (from #1) that he got from me.
I can choose to be prompted to accept the connection from the client to my VPC End point service. As soon as I accept it, then the client can reach xyz.com from his/her EC2 instance. There is no Internet, no direct connect or VPN.. this simply works; and its secure. And which technology enabled it.. AWS Private link !!!
PRIVATE LINK IS THE ONLY TECHNOLOGY THAT ALLOWS 2 VPCS TO CONNECT THAT HAVE OVERLAPPING CIDR RANGES.
