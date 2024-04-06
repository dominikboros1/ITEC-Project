extends CharacterBody2D
@export var speed: float = 100
@export var accel: float = 10
var current_dir = "none"
var movement = 0

func _physics_process(_delta: float) -> void:
	var direction: Vector2 = Input.get_vector("left", "right", "up", "down")
	
	velocity.x = move_toward(velocity.x, speed * direction.x, accel)
	velocity.y = move_toward(velocity.y, speed * direction.y, accel)
	var anim = $AnimatedSprite2D
	
	if direction.x == 1:
		anim.flip_h = false
		movement = 1
		if movement == 1:
			anim.play("walk right")
		elif movement == 0:
			anim.play("idle_side")
		
	if direction.x == -1:
		anim.flip_h = false
		movement = 1
		if movement == 1:
			anim.play("walk left")
		elif movement == 0:
			anim.play("idle")
		
	if direction.y == 1:
		anim.flip_h = false
		movement = 1
		if movement == 1:
			anim.play("walk right")
		elif movement == 0:
			anim.play("idle")
		
	if direction.y == -1:
		movement = 1
		if movement == 1:
			anim.play("walk left")
		elif movement == 0:
			anim.play("idle")
	if direction.x == 0 && direction.y == 0:
		movement = 0
		if movement == 1:
			anim.play("walk right")
		elif movement == 0:
			anim.play("idle")
	#else:
		#anim.play("idle")
	move_and_slide()
