import random
import string
import pygame
import sys

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    pygame.init()
    screen_width, screen_height = 500, 300
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Password Generator")

    font = pygame.font.Font(None, 36)
    input_box = pygame.Rect(100, 100, 140, 32)
    generate_button = pygame.Rect(250, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    button_color = pygame.Color('green')
    button_text_color = pygame.Color('white')
    color = color_inactive
    active = False
    text = ''
    password = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

                if generate_button.collidepoint(event.pos):
                    try:
                        length = int(text)
                        password = generate_password(length)
                    except ValueError:
                        password = 'Invalid input'
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            length = int(text)
                            password = generate_password(length)
                        except ValueError:
                            password = 'Invalid input'
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        screen.fill((30, 30, 30))

        instruction_text = "Enter the length for your password:"
        instruction_surface = font.render(instruction_text, True, (255, 255, 255))
        instruction_rect = instruction_surface.get_rect(topleft=(100, 50))
        if instruction_rect.right > screen_width:
            instruction_rect.width = screen_width - instruction_rect.left
            instruction_surface = font.render(instruction_text, True, (255, 255, 255))
        screen.blit(instruction_surface, instruction_rect.topleft)

        txt_surface = font.render(text, True, color)
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        txt_rect = txt_surface.get_rect(topleft=(input_box.x + 5, input_box.y + 5))
        if txt_rect.right > screen_width:
            txt_rect.width = screen_width - txt_rect.left
            txt_surface = font.render(text, True, color)
        screen.blit(txt_surface, txt_rect.topleft)
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.draw.rect(screen, button_color, generate_button)
        button_text = font.render("Generate", True, button_text_color)
        button_rect = button_text.get_rect(center=generate_button.center)
        screen.blit(button_text, button_rect.topleft)

        password_surface = font.render(password, True, (255, 255, 255))
        password_rect = password_surface.get_rect(topleft=(100, 200))
        if password_rect.right > screen_width:
            password_rect.width = screen_width - password_rect.left
            password_surface = font.render(password, True, (255, 255, 255))
        screen.blit(password_surface, password_rect.topleft)

        pygame.display.flip()

if __name__ == "__main__":
    main()
