# REST API for FSTR pereval.online website

The Federation for Sports Tourism in Russia maintains a database of mountain passes that receives tourist contributions. The FSTR group of experts verifies the information and saves it to the database.
This is an API solution for a mobile application, which can be used by tourists to submit mountain pass data and
send it to FSTR once they have internet access.

When tourists reach a mountain pass, they can take pictures and use the mobile application to submit the information.
Once a tourist clicks "Send", the mobile application calls submitData method, which accepts data in JSON format.

Example JSON data:
```json
{
  "beauty_title": "pass ",
  "title": "Some_title",
  "other_titles": "Some_titles",
  "connect": "",

  "add_time": "2021-09-22 14:23:45",
  "user": {"email": "ivanofff@mail.ru", 		
        "fam": "Ivonov",
		 "name": "Ivan",
		 "otc": "Ivanovich",
        "phone": "+7 123 45 67"}, 

   "coords":{
  "latitude": "54.3842",
  "longitude": "18.1525",
  "height": "1500"}


  "level": {"winter": "", 
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
  
   "images": [{"data":"<img1>", "title":"Something"}, {"data":"<img2>", "title":"Something"}]
}
```

The result of submission is status and status message. For example:
```json
{ "status": 200, "message": "OK"}
```
Once an object is submitted, it is assigned "new" status. FSTR experts change its status to "pending" meaning 
an expert is working on it, validate the new object, and then change the status either to "accepted" or "rejected". 

## API methods
#### GET /submitData/ method
Returns a list of all mountain passes.

#### POST /submitData/ method
Allows for a single mountain pass submission.

#### GET /submitData/{id}
Retrieves data for a particular mountain pass.

#### PATCH /submitData/{id}
Allows to change a mountain pass attribute values.
Returns a JSON response with 
- state: 1 for successful update and 0 for unsuccessful update
- message: explains why an update has failed

#### GET/submitData/?user__email=\<email>
Return a list of all objects that were sent to the system by the user with the specified email address
