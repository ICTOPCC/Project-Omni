extends Node2D





func _on_button_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door1")


func _on_button_2_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door2")



func _on_button_3_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/lock1")



func _on_button_4_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door1")



func _on_button_5_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules")


func _on_button_6_button_down():
	get_tree().change_scene_to_file("res://cam.tscn")
