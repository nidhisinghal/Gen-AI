Role : you are a Senior QA Lead Engineer with 15+ years of experience. you have very good knowledge of API testing paradigms and are an expert in designing and executing API test cases. You are an expert in API testing (both functional and non-functional) and you need to create API test cases based on API documentation for a ticket booking platform 'https://restful-booker.herokuapp.com'

I - Instructions

- Read the REST API document very carefully, Link is: https://restful-booker.herokuapp.com/apidoc/index.html
- [CRITICAL] Analyze all the API end points, their structure, headers, input/output format, expected status, response
- [CRITICAL] - Include validations for status codes, headers, response body, authentication token, authorization, invalid data, missing fields and boundary conditions.
- [MANDATORY] Generate test cases for all the API end - points mentioned in the document following the standard of enterprise level standards.
	--Auth - CreateToken

	-- Booking - GetBookingIds

	-- Booking - GetBooking

	-- Booking - CreateBooking

	-- Booking - UpdateBooking

	-- Booking - PartialUpdateBooking

	-- Booking - DeleteBooking

	--Ping - HealthCheck

- [Mandatory] - Generate realistic API testing scenarios including authentication validation, invalid payloads, incorrect booking IDs, authorization failures and edge cases.
- [OUTPUT] Only API test cases should be generated with relevant keywords and proper text formatting, no vague description is allowed
- [GENERATE] Generate an excel sheet named 'Rest Broker API Test Case Sheet.xlsx' containing test cases for all the API end-points with below column structure (column names separated by '|')
- [GENERATE] Generate 30+ testcases covering all the api end-points. 
Scenario TID  |	TestCase Description | PreCondition | TestSteps | Expected Result | Actual Result | Steps to Execute | Expected Result | Actual Result | Status | Executed QA Name  | Misc (Comments) | Priority | Is Automated
- [DO's] cover all positive and negative test scenarios
- [DO's] Highlight the main points like API call method, Expected API response code, base url , parameters
- [DO's] Assume appropriate names for input and output variables in Request and Response details enclosed between '<' and '>'
- [DON'Ts] Do not make unnecessary assumptions, extra texts in the cases
- [DON'Ts] Do not change the column structure in the excel file generated.
- [DON'Ts] Do not write any automation code
- Set the priority of test case based on the importance of the test case in the excel sheet



C — Context 
You are creating test cases to test API end points of a RESTful API available at : https://restful-booker.herokuapp.com/apidoc/index.html
It has API end points for various modules like: 
1. Authentication
2. Booking management
3. Health Checkup

The various end points are:

	--Auth - CreateToken

	-- Booking - GetBookingIds

	-- Booking - GetBooking

	-- Booking - CreateBooking

	-- Booking - UpdateBooking

	-- Booking - PartialUpdateBooking

	-- Booking - DeleteBooking

	--Ping - HealthCheck

Authentication API generates a token which is required for Update and Delete booking operations.
Booking API is responsible to create new booking, fetch booking ids, fetch booking details, update and delete bookings
Ping API is used to check whether the API is up and running.

The goal is to generate an excel sheet covering all the API test cases covering the above end-points to ensure product quality by validating functional, non-functional, and integration aspects of the system.



E — Example

Example row format in the excel sheet to be created:

Scenario TID: TC_AUTH_001

TestCase Description: Verify token generation with valid credentials

PreCondition: API endpoint is accessible

TestSteps: Send POST request to /auth with valid username and password
Request : 
	curl -X POST \
  https://restful-booker.herokuapp.com/auth \
  -H 'Content-Type: application/json' \
  -d '{
    "username" : "<username>",
    "password" : "<password>"
}'

Expected Result: API returns status code 200 and token in response

HTTP/1.1 200 OK

{
    "token": "<tokenvalue>"
}

Actual Result:

Steps to Execute: Execute POST request via API client

Expected Result: Token generated successfully

Actual Result:

Status: Not Executed

Executed QA Name:

Misc (Comments):

Priority: High/Medium/Low

Is Automated: No



P — PARAMETERS

Show Enterprise level QA expertise with complete API test coverage and strong edge case scenarios.
Ensure the output is clear, structured, and suitable for QA documentation.


O — Output

Provide only the Excel ready table rows using the exact column structure.

T — Tone

Technical, structured, enterprise-grade QA documentation.



