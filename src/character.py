# Base class for all characters
class Character():
    box_collider = None
    draw_rect = None
    animations = None
    health = 0
    stamina = 0
    attack_speed = 0
    move_speed = 0
    dodge_speed = 0
    
# Returns instantiated character
def init_character(box_collider, draw_rect, animations, health,
                    stamina, attack_speed, move_speed, dodge_speed):
    new_character = Character()
    new_character.box_collider = box_collider
    new_character.draw_rect = draw_rect
    new_character.animations = animations
    new_character.health = health
    new_character.stamina = stamina
    new_character.attack_speed = attack_speed
    new_character.move_speed = move_speed
    new_character.dodge_speed = dodge_speed
    return new_character