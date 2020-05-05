# iterapi-web
Deployed on heroku  
This is a [iterapi](https://github.com/SubhrajitPrusty/iterapi) , REST port to make http requests and fetch data for the student portal of ITER  
  
endpoints FOR POST :  
  
* /attendence/
* /result/
* /info/
  
Example request  

POST `https://iterapi-web.herokuapp.com/result/` with json body as:   
  
`{
	"user_id": "1941018330",
	"password": "mybadmybad",
	"sem": 1
}`  
  
Request to other endpoints can be made using the same json body with or without mentioning semester.  


