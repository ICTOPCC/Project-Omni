extends Node2D


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func _on_check_button_toggled(toggled_on):
	if toggled_on:
		Link.http.request(Link.url+"/led6_high")
	else:
		Link.http.request(Link.url+"/led6_low")
