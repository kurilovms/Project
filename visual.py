import pygame

FIELD_COLOR = (0, 0, 255)
FIELD_ACTIVE_COLOR = (255, 0, 0)
BUTTON_FONT = ('Arial', 80)
FIELD_FONT = ('Arial', 30)
BUTTON_COLOR = (0, 255, 0)


class Button:
    def __init__(self, x=0, y=0, text='', w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.rect = pygame.Rect(0, 0, 0, 0)
    
    def draw(self):
        font = pygame.font.SysFont(*BUTTON_FONT)
        textsurface = font.render(self.text, False, (0, 0, 0))
        x, y = textsurface.get_size()
        surf = pygame.Surface(textsurface.get_size(), pygame.SRCALPHA)
        x = x // 2
        y = y // 2
        surfscaled = pygame.Surface(
                (x, y), pygame.SRCALPHA)
        surf.blit(textsurface, (0, 0))
        pygame.transform.smoothscale(
                surf, (x, y), surfscaled)
        screen = pygame.display.get_surface()
        self.rect = pygame.Rect(self.x-10, self.y-10, x+20, y+20)
        self.w = x + 20
        self.h = y + 20
        pygame.draw.rect(screen, BUTTON_COLOR, self.rect, 2)
        if self.check():
            pygame.draw.rect(screen, BUTTON_COLOR, self.rect)
        screen.blit(surfscaled, (self.x, self.y))

    def check(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

class InputBox:
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.active = False
        self.text = ''

    def event_handler(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.active = not self.active
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self):
        font = pygame.font.SysFont(*FIELD_FONT)
        textsurface = font.render(self.text, False, (0, 0, 0))
        x, y = textsurface.get_size()
        surf = pygame.Surface(textsurface.get_size(), pygame.SRCALPHA)
        x = x // 2
        y = y // 2
        surfscaled = pygame.Surface(
                (x, y), pygame.SRCALPHA)
        surf.blit(textsurface, (0, 0))
        pygame.transform.smoothscale(
                surf, (x, y), surfscaled)
        screen = pygame.display.get_surface()
        self.rect = pygame.Rect(self.x - 10, self.y - 10, max(self.length, x + 20), y + 20)
        
        pygame.draw.rect(screen, FIELD_COLOR, self.rect, 2)
        if self.active:
            pygame.draw.rect(screen, FIELD_ACTIVE_COLOR, self.rect, 2)
        screen.blit(surfscaled, (self.x, self.y))

