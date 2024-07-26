extends Node2D





func _on_button_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door1")


func _on_button_2_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door2")



func _on_button_3_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/lock1")



func _on_button_4_button_down():
	Link.http.request("http://192.168.31.80:1942/omni_modules/servo1/door1")

