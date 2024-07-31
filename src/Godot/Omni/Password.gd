extends Node2D

var password = "2157"



func _on_line_edit_text_submitted(new_text):
	if new_text == password:
		if Link.req == 1:
			Link.http.request(Link.url+"/omni_modules/servo1/lock1")
			get_tree().change_scene_to_file("res://Master Bedroom.tscn")
			print("lock1")
		elif Link.req == 2:
			Link.http.request(Link.url+"/omni_modules/servo1/lock2")
			get_tree().change_scene_to_file("res://Secondary Bedroom.tscn")
			print("lock2")
	else:
		$Panel/LineEdit.clear()
