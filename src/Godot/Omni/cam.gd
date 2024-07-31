extends Node2D

func _ready():
	print("came")

func _physics_process(delta):
	$TextureRect.texture = Link.export_img

func _on_button_button_down():
	get_tree().change_scene_to_file("res://Menu.tscn")
