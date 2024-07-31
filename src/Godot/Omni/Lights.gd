extends Node2D


func _on_check_button_toggled(toggled_on):
	if toggled_on:
		Link.http.request(Link.url+"/led1_high")
	else:
		Link.http.request(Link.url+"/led1_low")

func _on_check_button_toggled1(toggled_on):
	if toggled_on:
		Link.http.request(Link.url+"/led2_high")
	else:
		Link.http.request(Link.url+"/led2_low")

func _on_check_button_toggled2(toggled_on):
	if toggled_on:
		Link.http.request(Link.url+"/led3_high")
	else:
		Link.http.request(Link.url+"/led3_low")

func _on_check_button_toggled3(toggled_on):
	if toggled_on:
		Link.http.request(Link.url+"/led4_high")
	else:
		Link.http.request(Link.url+"/led4_low")

func _on_check_button_toggled4(toggled_on):
	if toggled_on:
		Link.http.request(Link.url+"/led5_high")
	else:
		Link.http.request(Link.url+"/led5_low")
