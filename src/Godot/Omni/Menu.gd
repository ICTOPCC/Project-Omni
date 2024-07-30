extends Node2D

var req = "http://192.168.31.80:1942/omni_modules/servo1/lock1"
var password = "2157"

func _ready():
	$Panel2/LineEdit.position.x += 4000


func _on_button_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door1")


func _on_button_2_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door2")



func _on_button_3_button_down():
	$Panel.position.x += 4000
	$Panel2/LineEdit.position.x -= 4000
	req = "http://192.168.31.80:1942/omni_modules/servo1/lock1"
	
	



func _on_button_4_button_down():
	$Panel.position.x += 4000
	$Panel2/LineEdit.position.x -= 4000
	req = "http://192.168.31.80:1942/omni_modules/servo1/lock2"
	



func _on_button_5_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules")


func _on_button_6_button_down():
	get_tree().change_scene_to_file("res://cam.tscn")


func _on_line_edit_text_submitted(new_text):
	if new_text == password:
		$Panel2/LineEdit.clear()
		$Panel.position.x -= 4000
		$Panel2/LineEdit.position.x += 4000
		Link.http.request(req)
	else:
		$Panel2/LineEdit.clear()


func _mbroom_button_down():
	get_tree().change_scene_to_file("res://Master Bedroom.tscn")


func _on_sbroom_button_down():
	get_tree().change_scene_to_file("res://Secondary Bedroom.tscn")


func _sec_cam_button_down():
	get_tree().change_scene_to_file("res://Security Cam.tscn")
