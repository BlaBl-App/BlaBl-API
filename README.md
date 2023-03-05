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

### `api/forums` `POST`

allow to add a new forum to the forum list

 <details>
<summary>param</summary>
<br>
 param `name` forum name<br>
 param `description` forum description<br>
</details>

### `api/forums` `GET`

retrieved the list of forums object :

```py
{"id": int, "name": str, "description": str}
```

no params

### `api/forums` `DELETE`

allow to delete a forum from the forum list

 <details>
<summary>param</summary>
<br>
 param `id` forum id<br>
</details>

## Setup

You need to have docker installed

after cloning the projet, in the root of th project run `docker build -t blapi . `<br>
once do you can start the docker with `docker rm blapi1 & docker run -it -p 5555:5555 --name blapi1 blapi`

test command `curl http://tchoutchou.ovh:5555/api/message -d nickname=bob -d pic= -d message="hi my name is bob"`
and `curl http://tchoutchou.ovh:5555/api/message`

## Testing

To run the tests, simply run `python3 -m tests` in the root of the project
