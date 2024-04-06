extends CharacterBody2D
@export var speed: float = 100
@export var accel: float = 10

func _physics_process(_delta: float) -> void:
	var direction: Vector2 = Input.get_vector("left", "right", "up", "down")
	
	velocity.x = move_toward(velocity.x, speed * direction.x, accel)
	velocity.y = move_toward(velocity.y, speed * direction.y, accel)
	var anim = $AnimatedSprite2D
	
	if direction.x == 1:
		anim.flip_h = false
		anim.play("walk right")
		
	if direction.x == -1:
		anim.flip_h = false
		anim.play("walk left")
		
	if direction.y == 1:
		anim.flip_h = true
		anim.play("walk_right")
		
	if direction.y == -1:
		anim.flip_h = true
		anim.play("walk_left")
	move_and_slide()
