# AWS API Gateway Interview Questions and Answers

## 1. What is AWS API Gateway?

**Question:**
What is AWS API Gateway?

**Answer:**
AWS API Gateway is a fully managed service that allows developers to create, publish, maintain, monitor, and secure APIs at any scale. It supports RESTful APIs and WebSocket APIs and acts as a "front door" for applications to access data, business logic, or functionality from backend services, such as workloads running on AWS Lambda, EC2, or other web services.

## 2. Explain the difference between REST APIs and WebSocket APIs in API Gateway.

**Question:**
Explain the difference between REST APIs and WebSocket APIs in API Gateway.

**Answer:**
- **REST APIs:** These are stateless APIs that follow the REST architecture, primarily used for CRUD operations. They support standard HTTP methods like GET, POST, PUT, DELETE, etc.
- **WebSocket APIs:** These are stateful, full-duplex communication channels over a single, long-lived connection. They are used for real-time applications like chat apps, live updates, etc. 

## 3. How do you secure an API in API Gateway?

**Question:**
How do you secure an API in API Gateway?

**Answer:**
There are several ways to secure an API in API Gateway:
- **IAM Roles and Policies:** Use AWS Identity and Access Management (IAM) to control access to your APIs.
- **API Keys:** Require API keys for access and manage them using usage plans.
- **Lambda Authorizers:** Implement custom authorization logic using AWS Lambda functions.
- **Cognito User Pools:** Use Amazon Cognito to manage user authentication and authorization.
- **Resource Policies:** Define resource policies to restrict access based on IP addresses, VPC endpoints, etc.
- **TLS/SSL:** Enforce HTTPS to secure data in transit.

## 4. What is a usage plan in API Gateway?

**Question:**
What is a usage plan in API Gateway?

**Answer:**
A usage plan in API Gateway allows you to manage who can access your APIs and how much they can use them. It specifies throttling limits and quota limits. Throttling limits control the rate of requests per second, while quota limits restrict the number of requests over a specified period (day, week, month). Usage plans can be associated with API keys to enforce limits on a per-client basis.

## 5. What are the different types of endpoints in API Gateway?

**Question:**
What are the different types of endpoints in API Gateway?

**Answer:**
API Gateway supports three types of endpoints:
- **Edge-Optimized Endpoints:** These are best for geographically distributed clients. Requests are routed to the nearest CloudFront edge location, then to the API Gateway.
- **Regional Endpoints:** These are intended for clients within the same AWS region. They are not cached at edge locations.
- **Private Endpoints:** These are accessible only from within a VPC using an interface VPC endpoint (powered by AWS PrivateLink).

## 6. How do you create a custom domain name in API Gateway?

**Question:**
How do you create a custom domain name in API Gateway?

**Answer:**
To create a custom domain name in API Gateway:
1. **Provision an ACM Certificate:** Request an SSL/TLS certificate using AWS Certificate Manager (ACM) for your custom domain.
2. **Create the Custom Domain Name:** In the API Gateway console, go to Custom Domain Names and create a new custom domain name, associating it with the ACM certificate.
3. **Map the Custom Domain Name:** Map the custom domain name to your API Gateway API stages using base path mappings.
4. **Update DNS Settings:** Update your DNS provider to point your custom domain to the API Gateway endpoint. This usually involves creating a CNAME record.

## 7. What are integration types in API Gateway?

**Question:**
What are integration types in API Gateway?

**Answer:**
API Gateway supports several integration types:
- **HTTP/HTTP_PROXY:** Integrates with HTTP/HTTPS endpoints. HTTP_PROXY allows you to route requests directly to the backend service.
- **AWS Service/AWS_PROXY:** Integrates with AWS services like Lambda, DynamoDB, etc. AWS_PROXY simplifies integrating Lambda functions by passing through the request.
- **MOCK:** Returns a response without calling any backend service. Useful for testing.
- **VPC Link:** Connects API Gateway to backend services within a VPC using VPC links.

## 8. How do you handle CORS in API Gateway?

**Question:**
How do you handle CORS in API Gateway?

**Answer:**
To handle CORS (Cross-Origin Resource Sharing) in API Gateway:
1. **Enable CORS in Method Response:** In the API Gateway console, select the API method, go to the Method Response, and add an HTTP 200 status response.
2. **Add CORS Headers in Integration Response:** In the Integration Response, map the necessary CORS headers (`Access-Control-Allow-Origin`, `Access-Control-Allow-Methods`, `Access-Control-Allow-Headers`, etc.) to the Method Response.
3. **Deploy the API:** Redeploy the API for the changes to take effect.

## 9. Explain the lifecycle of a request in API Gateway.

**Question:**
Explain the lifecycle of a request in API Gateway.

**Answer:**
The lifecycle of a request in API Gateway involves the following steps:
1. **Client Request:** A client makes an HTTP request to an API Gateway endpoint.
2. **API Gateway Frontend:** API Gateway processes the request, validating the request against defined API keys, usage plans, and resource policies.
3. **Method Request:** API Gateway checks the request method (GET, POST, etc.) and validates request parameters.
4. **Integration Request:** API Gateway transforms the request if needed and sends it to the backend integration (HTTP endpoint, Lambda function, etc.).
5. **Backend Processing:** The backend service processes the request and returns a response.
6. **Integration Response:** API Gateway transforms the backend response if necessary.
7. **Method Response:** API Gateway maps the integration response to the method response.
8. **Client Response:** The final response is sent back to the client.

## 10. What is API Gateway caching, and how do you configure it?

**Question:**
What is API Gateway caching, and how do you configure it?

**Answer:**
API Gateway caching stores endpoint responses in a cache for a specified time to reduce the number of requests sent to your backend and improve performance. To configure caching:
1. **Enable Caching:** In the API Gateway console, enable caching for a specific stage.
2. **Configure Cache Settings:** Set the TTL (Time to Live) for cache entries and configure cache capacity.
3. **Configure Cache Key Parameters:** Specify request parameters to be used as cache keys to determine the uniqueness of cache entries.
4. **Deploy the API:** Deploy the API changes to apply the caching configuration.
