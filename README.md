# iterapi-web

This is [iterapi](https://github.com/SubhrajitPrusty/iterapi) , REST port.  

run using `python manage.py runserver'  
endpoints FOR POST :  
  
  `
/attendence/
/result/
/info/
`
  
Example request  

POST `http://127.0.0.1:8000/result/` with json body as  
`{
	"user_id": "1941018330",
	"password": "mybadmybad",
	"sem": 1
}`

