<div align="center">
<img width="128" alt="Plugin icon - 4" src="https://user-images.githubusercontent.com/37497007/222099229-38659c41-e75f-4a0a-9227-84ee0b17bbfb.png">


<h1>BlaBl'API</h1>

<p> BlaBla'App backend docker python API </p>
 </div>


 
 ## :book: API Endpoint
 
 ### `api/message` `GET`
 retrieved the lastest message <br>
<details>
<summary>param</summary>
<br>
 param `nb` set the maximum message retrieved <br>
 parma `start` set setp ..????!? (ot get older message)<br>
</details>
 
 ### `api/message` `POST`

 allow to post a new message to the forum
 <details>
<summary>param</summary>
<br>
 param `pic` user profile pic in bytemap<br>
 param `nickname` user nickname<br>
 parma `message` message conntent to be posted limited to 256 words<br>
</details>

