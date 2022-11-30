
# Requitty

requitty is a command console program which is responsible for providing solutions to different day-to-day problems, seeking to efficiently create commands which facilitate the repetitive tasks of the developer.




## Usage/Examples

```cmd
requitty -r get -u https://api.com

```
```cmd
response with a status 200
```

## Screenshots

![App Screenshot](https://user-images.githubusercontent.com/111100025/204715278-4164d199-4872-461a-af95-5350ca116647.png)



## Commands

### Request

```cmd
  requitty -r http-method -u url
```

| Parameter | arg     | Description                |
| :-------- | :------- | :------------------------- |
| `--request` | `-r` | **Required** http method **GET** |
| `--url` | `-u` | **Required** Direction from request or path |

#### Options

```cmd
  requitty -r http-method -u url [options]
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `--verbose`      | `bool` | **optional**. show the response of the request |
| `--save`      | `string` | **optional**. save the response in json file |


## Deployment


```cmd
git clone https://github.com/daliondev/requitty.git
```


```cmd
cd .\requitty\
```

```cmd
pip install -r requirements.txt
```
