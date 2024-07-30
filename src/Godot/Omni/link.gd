extends Node
@onready var http:HTTPRequest = HTTPRequest.new()
var image_url:HTTPRequest = HTTPRequest.new()
@export var json:JSON
var export_img:ImageTexture
func _ready():
	add_child(image_url)
	add_child(http)
	http.request_completed.connect(_http_request_completed)
	image_url.request_completed.connect(_image_loaded)
	var error = image_url.request("http://192.168.31.80:1942/video")
	if error == OK:
		print("should be fine....")
	else:
		print(error)
	http.request("http://192.168.31.80:1942/omni_modules")
	

func _http_request_completed(result, response_code, headers, body):
	json = JSON.new()
	json.parse(body.get_string_from_utf8())
	print(json.data)

func _image_loaded(result, response_code, headers, body):
	var image:Image = Image.new()
	image.load_jpg_from_buffer(body)
	var texture:ImageTexture = ImageTexture.create_from_image(image)
	export_img = texture
	image_url.request("http://127.0.0.1:2157/video")
