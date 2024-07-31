extends Node2D

func _mbroom_button_down():
	get_tree().change_scene_to_file("res://Master Bedroom.tscn")


func _on_sbroom_button_down():
	get_tree().change_scene_to_file("res://Secondary Bedroom.tscn")


func _sec_cam_button_down():
	get_tree().change_scene_to_file("res://cam.tscn")


func _on_Lightings_button_down():
	get_tree().change_scene_to_file("res://Lights.tscn")
