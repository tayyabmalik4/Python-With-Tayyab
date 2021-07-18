# ///////////////////////////Request Module///////////////////////////
# /////////////basically it is use in the web browser/////////////////
# there are many kinds of request methods like get, post, put, delete and so onn
# /////////but in this toturail we use just get and post method
# //////////get method is use to show of the statment in the browser ---------------function name is(request.get(URL))
# //////////and post method is the backend or database link and store the value in the backend or database----------function name is (request.post(url, dictionary))
# ///////// therefore put means to eid the values and delete means to delete the values


# ///////////these are the status_codes which we help to many places
# Informational responses (100–199)
# Successful responses (200–299)
# Redirects (300–399)
# Client errors (400–499)
# Server errors (500–599)
# ///////////and also this is the link of the status_code website which is more detailed (https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)



# ////////if requests method has any error like no module found request than we import using pip (pip install requests)
import requests
# //////this is for get request
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)
print(x.status_code)

# /////////this code is for post reuest
# /////////first of all we put the url and than put data which we send it like email password and so on than we creat a variable and than store the values store in it
# url = "Build AI in Pakistan.com"
# data= {
#     "data1":"this is my dream",
#     "data2":"this is true dream and inshaAllah i will true it",
#     "data3":"i will go to germany to learn more and more AI and than build AI in pakistan"
# }
# r2=requests.post(url=url, data=data)


# ///////////these are also use functions in the help of requests and it is very helpful and useful in all the fields
# >>> requests.get('https://httpbin.org/get')
# >>> requests.post('https://httpbin.org/post', data={'key':'value'})
# >>> requests.put('https://httpbin.org/put', data={'key':'value'})
# >>> requests.delete('https://httpbin.org/delete')
# >>> requests.head('https://httpbin.org/get')
# >>> requests.patch('https://httpbin.org/patch', data={'key':'value'})
# >>> requests.options('https://httpbin.org/get')


