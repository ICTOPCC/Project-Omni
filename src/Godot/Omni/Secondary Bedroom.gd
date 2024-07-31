extends Node2D


func _on_toogle_door_down():
	Link.http.request(Link.url+"/omni_modules/servo1/door2")


func _on_lock_button_down():
	Link.req = 2
	get_tree().change_scene_to_file("res://Password.tscn")
