import pygame
import cv2
from mutagen.mp3 import MP3

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (255, 255, 0)

# Fonts
font_paths = {
    'kreyol': 'assets/fonts/PIXEL LATIN.ttf',
    'francais': 'assets/fonts/PIXEL LATIN.ttf',
    'anglais': 'assets/fonts/PIXEL LATIN.ttf',
    'espagnol': 'assets/fonts/PIXEL LATIN.ttf',
    'allemand': 'assets/fonts/PIXEL LATIN.ttf',
    'japonais': 'assets/fonts/SevenFifteenMonoRounded-Regular.ttf',
    'chinois': 'assets/fonts/ipix_12pxchinese.ttf',
    'russe': 'assets/fonts/SevenFifteenMonoRounded-Regular.ttf',
    'coreen': 'assets/fonts/DungGeunMo.ttf',
    'hindi': 'assets/fonts/SevenFifteenMonoRounded-Regular.ttf',
    'indonesien': 'assets/fonts/PIXEL LATIN.ttf',
    'arabe': 'assets/fonts/SevenFifteenMonoRounded-Regular.ttf'
}

# Translations
translations = {
    'kreyol': {
        'play': 'Jwe',
        'settings': 'Paramèt',
        'credits': 'Kredi',
        'quit': 'Kite',
        'combat_mode': 'Mode Kombat',
        'adventure_mode': 'Mode Avantur',
        'sound': 'Son',
        'display': 'Ekspozisyon',
        'control': 'Kontwòl',
        'language': 'Lang',
        'back': 'Retounen'
    },
    'francais': {
        'play': 'Jouer',
        'settings': 'Paramètres',
        'credits': 'Crédits',
        'quit': 'Quitter',
        'combat_mode': 'Mode Combat',
        'adventure_mode': 'Mode Aventure',
        'sound': 'Son',
        'display': 'Affichage',
        'control': 'Contrôle',
        'language': 'Langue',
        'back': 'Retour'
    },
    'anglais': {
        'play': 'Play',
        'settings': 'Settings',
        'credits': 'Credits',
        'quit': 'Quit',
        'combat_mode': 'Combat Mode',
        'adventure_mode': 'Adventure Mode',
        'sound': 'Sound',
        'display': 'Display',
        'control': 'Control',
        'language': 'Language',
        'back': 'Back'
    },
    'espagnol': {
        'play': 'Jugar',
        'settings': 'Configuraciones',
        'credits': 'Créditos',
        'quit': 'Salir',
        'combat_mode': 'Modo Combate',
        'adventure_mode': 'Modo Aventura',
        'sound': 'Sonido',
        'display': 'Pantalla',
        'control': 'Control',
        'language': 'Idioma',
        'back': 'Atrás'
    },
    'allemand': {
        'play': 'Spielen',
        'settings': 'Einstellungen',
        'credits': 'Credits',
        'quit': 'Beenden',
        'combat_mode': 'Kampfmodus',
        'adventure_mode': 'Abenteuer-Modus',
        'sound': 'Ton',
        'display': 'Anzeige',
        'control': 'Steuerung',
        'language': 'Sprache',
        'back': 'Zurück'
    },
    'japonais': {
        'play': 'プレイ',
        'settings': '設定',
        'credits': 'クレジット',
        'quit': '終了',
        'combat_mode': '戦闘モード',
        'adventure_mode': '冒険モード',
        'sound': 'サウンド',
        'display': 'ディスプレイ',
        'control': 'コントロール',
        'language': '言語',
        'back': '戻る'
    },
    'chinois': {
        'play': '玩',
        'settings': '设置',
        'credits': '积分',
        'quit': '退出',
        'combat_mode': '战斗模式',
        'adventure_mode': '冒险模式',
        'sound': '声音',
        'display': '显示',
        'control': '控制',
        'language': '语言',
        'back': '返回'
    },
    'russe': {
        'play': 'Играть',
        'settings': 'Настройки',
        'credits': 'Кредиты',
        'quit': 'Выйти',
        'combat_mode': 'Режим Боя',
        'adventure_mode': 'Приключенческий Режим',
        'sound': 'Звук',
        'display': 'Дисплей',
        'control': 'Управление',
        'language': 'Язык',
        'back': 'Назад'
    },
    'coreen': {
        'play': '놀이',
        'settings': '설정',
        'credits': '크레딧',
        'quit': '종료',
        'combat_mode': '전투 모드',
        'adventure_mode': '모험 모드',
        'sound': '소리',
        'display': '디스플레이',
        'control': '제어',
        'language': '언어',
        'back': '뒤로'
    },
    'hindi': {
        'play': 'खेलें',
        'settings': 'समायोजन',
        'credits': 'क्रेडिट',
        'quit': 'बाहर जाएं',
        'combat_mode': 'लड़ाई मोड',
        'adventure_mode': 'साहसिक मोड',
        'sound': 'ध्वनि',
        'display': 'प्रदर्शन',
        'control': 'नियंत्रण',
        'language': 'भाषा',
        'back': 'वापस'
    },
    'indonesien': {
        'play': 'Bermain',
        'settings': 'Pengaturan',
        'credits': 'Kredit',
        'quit': 'Keluar',
        'combat_mode': 'Mode Pertarungan',
        'adventure_mode': 'Mode Petualangan',
        'sound': 'Suara',
        'display': 'Tampilan',
        'control': 'Kontrol',
        'language': 'Bahasa',
        'back': 'Kembali'
    },
    'arabe': {
        'play': 'لعب',
        'settings': 'الإعدادات',
        'credits': 'الائتمانات',
        'quit': 'ترك',
        'combat_mode': 'وضع القتال',
        'adventure_mode': 'وضع المغامرة',
        'sound': 'صوت',
        'display': 'عرض',
        'control': 'تحكم',
        'language': 'لغة',
        'back': 'عودة'
    }
}

# Language options
language_options = [
    'kreyol', 'francais', 'anglais', 'espagnol', 'allemand',
    'japonais', 'chinois', 'russe', 'coreen', 'hindi', 'indonesien', 'arabe'
]

# Load flags and resize to 75x75 pixels
flags = {
    'kreyol': pygame.transform.scale(pygame.image.load('assets/images/flags/Haiti.png'), (75, 75)),
    'francais': pygame.transform.scale(pygame.image.load('assets/images/flags/france.png'), (75, 75)),
    'anglais': pygame.transform.scale(pygame.image.load('assets/images/flags/usa.png'), (75, 75)),
    'espagnol': pygame.transform.scale(pygame.image.load('assets/images/flags/spain.png'), (75, 75)),
    'allemand': pygame.transform.scale(pygame.image.load('assets/images/flags/germany.png'), (75, 75)),
    'japonais': pygame.transform.scale(pygame.image.load('assets/images/flags/japan.png'), (75, 75)),
    'chinois': pygame.transform.scale(pygame.image.load('assets/images/flags/chine.png'), (75, 75)),
    'russe': pygame.transform.scale(pygame.image.load('assets/images/flags/Russie.png'), (75, 75)),
    'coreen': pygame.transform.scale(pygame.image.load('assets/images/flags/south_korea.png'), (75, 75)),
    'hindi': pygame.transform.scale(pygame.image.load('assets/images/flags/inde.png'), (75, 75)),
    'indonesien': pygame.transform.scale(pygame.image.load('assets/images/flags/indonesie.png'), (75, 75)),
    'arabe': pygame.transform.scale(pygame.image.load('assets/images/flags/emirate.png'), (75, 75))
}

# Load logo and resize to 250x250 pixels
logo = pygame.image.load('assets/images/logo_nobg_etherna.png')
logo = pygame.transform.scale(logo, (150, 150))

# Load creator images and resize to 150x150 pixels
creator1_image = pygame.transform.scale(pygame.image.load('assets/images/samuel.png'), (64, 64))
creator2_image = pygame.transform.scale(pygame.image.load('assets/images/jonathan.png'), (64, 64))

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Classes
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = WHITE
        self.hovered = False

    def draw(self, surface, font):
        if self.hovered:
            self.color = HIGHLIGHT_COLOR
        else:
            self.color = WHITE
        pygame.draw.rect(surface, self.color, self.rect)
        draw_text(self.text, font, BLACK, surface, self.rect.centerx, self.rect.centery)

    def is_hovered(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
            return True
        else:
            self.hovered = False
            return False

class FlagButton:
    def __init__(self, flag, text, x, y):
        self.flag = flag
        self.text = text
        self.rect = pygame.Rect(x, y, 75, 75)
        self.hovered = False

    def draw(self, surface, font):
        surface.blit(self.flag, self.rect.topleft)
        draw_text(self.text, font, WHITE, surface, self.rect.centerx, self.rect.bottom + 20)

    def is_hovered(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.hovered = True
            return True
        else:
            self.hovered = False
            return False

class Menu:
    def __init__(self, options, x, y, font):
        self.options = options
        self.buttons = [Button(text, x, y + i * 60, 300, 50) for i, text in enumerate(options)]
        self.font = font

    def draw(self, surface):
        for button in self.buttons:
            button.draw(surface, self.font)

    def get_hovered_button(self, mouse_pos):
        for button in self.buttons:
            if button.is_hovered(mouse_pos):
                return button
        return None

class FlagMenu:
    def __init__(self, options, x, y, font):
        self.options = options
        self.flags = []
        for i, lang in enumerate(options):
            flag_x = x + (i % 6) * 100  # Adjust spacing between flags
            flag_y = y + (i // 6) * 150  # Adjust spacing between rows
            self.flags.append(FlagButton(flags[lang], lang.capitalize(), flag_x, flag_y))
        self.font = font
        self.back_button = Button(translations[current_language]['back'], x + 150, y + 300, 300, 50)

    def draw(self, surface):
        for flag in self.flags:
            flag.draw(surface, self.font)
        self.back_button.draw(surface, self.font)

    def get_hovered_button(self, mouse_pos):
        if self.back_button.is_hovered(mouse_pos):
            return self.back_button
        for flag in self.flags:
            if flag.is_hovered(mouse_pos):
                return flag
        return None

    def update_language(self):
        self.back_button.text = translations[current_language]['back']

class CreditMenu:
    def __init__(self, font):
        self.font = font
        self.text = """
🥋 Jeu de Combat - INF2300 Infographie 🥋

Introduction
Bienvenue dans notre projet de jeu de combat, créé avec passion pour l'apprentissage et l'excellence. 
Inspiré par Coder Space et Coding With Russ, nous avons mis tout notre cœur dans ce jeu. 
Préparez-vous à des combats épiques ! 🎮

Inspiration
Inspiré par :
- Coder Space (YouTube : Coder Space, GitHub : Stanislav Petrov)
- Coding With Russ (YouTube : Coding With Russ, GitHub : Russ)

Merci pour le partage de connaissances. Vous êtes des rock stars du code ! 🤘

Utilisation des Assets
Tous les assets proviennent de itch.io et sont gratuits. Merci à la communauté d'itch.io ! 🎨

Licence
Projet sous licence MIT. Utilisez, modifiez et partagez librement. Partagez la connaissance libre ! 📚✨

Contact
Pour questions et suggestions :
- 📧 isteah.josephsamuel@gmail.com – JOSEPH Samuel Jonathan
- 📧 isteah.jpierrelouis03@gmail.com – JONATHAN Pierre Louis

Informations du Cours
- Cours : INF2300 Infographie
- Session : Été 2024
- Travail No. : 3
- Groupe : JOSEPH Samuel Jonathan, JONATHAN Pierre Louis
- Soumis à : Dre. Franjieh El Khoury
- Date : 21 juin 2024

Fonctionnalités du Jeu
- 🎬 Introduction Vidéo captivante
- 🕹️ Menu Principal animé
- 🥊 Modes de Combat variés
- 🎶 Paramètres ajustables
- 👨‍💻 Crédits du projet

Remerciements
Merci à nos professeurs, collègues, amis, et à vous pour votre soutien. Coder, c'est comme combattre – stratégie, détermination, et café ! ☕👨‍💻👩‍💻
"""
        self.lines = self.text.strip().split('\n')
        self.scroll_y = HEIGHT
        self.back_button = Button(translations[current_language]['back'], WIDTH // 2 - 150, HEIGHT - 100, 300, 50)

    def draw(self, surface):
        y_offset = self.scroll_y
        for line in self.lines:
            draw_text(line.strip(), self.font, WHITE, surface, WIDTH // 2, y_offset)
            y_offset += 30

        surface.blit(creator1_image, (WIDTH // 2 - 150, 50))
        surface.blit(creator2_image, (WIDTH // 2 + 50, 50))

        draw_text("JOSEPH Samuel Jonathan", self.font, WHITE, surface, WIDTH // 2 - 125, 120)
        draw_text("JONATHAN Pierre Louis", self.font, WHITE, surface, WIDTH // 2 + 125, 120)

        self.back_button.draw(surface, self.font)

    def update(self):
        self.scroll_y -= 1
        if self.scroll_y < -len(self.lines) * 30:
            self.scroll_y = HEIGHT

    def get_hovered_button(self, mouse_pos):
        if self.back_button.is_hovered(mouse_pos):
            return self.back_button
        return None

    def update_language(self):
        self.back_button.text = translations[current_language]['back']

class GameMenu:
    def __init__(self, selected_language):
        global current_language  # Ensure we can modify the global variable
        current_language = selected_language  # Set the language selected in intro.py

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)  # Rendre la fenêtre redimensionnable
        self.clock = pygame.time.Clock()
        self.running = True
        self.selected_mode = None

        self.main_menu = Menu([
            translations[current_language]['play'],
            translations[current_language]['settings'],
            translations[current_language]['credits'],
            translations[current_language]['quit']
        ], WIDTH // 2 - 150, HEIGHT // 2 - 60, pygame.font.Font(font_paths[current_language], 30))

        self.play_menu = Menu([
            translations[current_language]['combat_mode'],
            translations[current_language]['adventure_mode'],
            translations[current_language]['back']
        ], WIDTH // 2 - 150, HEIGHT // 2 - 60, pygame.font.Font(font_paths[current_language], 30))

        self.settings_menu = Menu([
            translations[current_language]['sound'],
            translations[current_language]['display'],
            translations[current_language]['control'],
            translations[current_language]['language'],
            translations[current_language]['back']
        ], WIDTH // 2 - 150, HEIGHT // 2 - 60, pygame.font.Font(font_paths[current_language], 30))

        self.language_menu = FlagMenu(language_options, WIDTH // 2 - 300, HEIGHT // 2 - 150, pygame.font.Font(font_paths[current_language], 20))
        self.credit_menu = CreditMenu(pygame.font.Font(font_paths[current_language], 20))

        self.current_menu = self.main_menu

        self.load_resources()

    def load_resources(self):
        self.click_sound = pygame.mixer.Sound("assets/song/click.wav")
        self.hover_sound = pygame.mixer.Sound("assets/song/hover.wav")
        self.background_music = "assets/song/LEMMiNO - Cipher (BGM).mp3"
        self.videos = {
            'main_menu': cv2.VideoCapture('assets/video/background/DALL·E 2024-06-20 17.53.56 ...s sword raised hi_animation.mp4'),
            'play_menu': cv2.VideoCapture('assets/video/background/3_background.mp4'),
            'settings_menu': cv2.VideoCapture('assets/video/background/2_background.mp4'),
            'language_menu': cv2.VideoCapture('assets/video/background/forest.mp4'),
            'credit_menu': cv2.VideoCapture('assets/video/background/flower.mp4')
        }
        self.current_video = self.videos['main_menu']
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.play(-1)  # Loop the music

    def play_hover_sound(self):
        self.hover_sound.play()

    def play_click_sound(self):
        self.click_sound.play()

    def run(self):
        global current_language  # Ensure we can modify the global variable
        while self.running:
            ret, frame = self.current_video.read()
            if not ret:
                self.current_video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = self.current_video.read()

            frame = cv2.resize(frame, (self.screen.get_width(), self.screen.get_height()))  # Redimensionner la vidéo
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.transpose(frame)
            frame = cv2.flip(frame, 0)
            surface = pygame.surfarray.make_surface(frame)
            self.screen.blit(surface, (0, 0))

            if self.current_menu == self.main_menu:
                self.screen.blit(logo, (self.screen.get_width() // 2 - logo.get_width() // 2, 50))

            mouse_pos = pygame.mouse.get_pos()
            hovered_button = self.current_menu.get_hovered_button(mouse_pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                elif event.type == pygame.MOUSEBUTTONDOWN and hovered_button:
                    self.play_click_sound()
                    if isinstance(self.current_menu, Menu):
                        if self.current_menu == self.main_menu:
                            if hovered_button.text == translations[current_language]['play']:
                                self.current_menu = self.play_menu
                                self.current_video = self.videos['play_menu']
                            elif hovered_button.text == translations[current_language]['settings']:
                                self.current_menu = self.settings_menu
                                self.current_video = self.videos['settings_menu']
                            elif hovered_button.text == translations[current_language]['credits']:
                                self.current_menu = self.credit_menu
                                self.current_video = self.videos['credit_menu']
                            elif hovered_button.text == translations[current_language]['quit']:
                                self.running = False
                        elif self.current_menu == self.play_menu:
                            if hovered_button.text == translations[current_language]['adventure_mode']:
                                self.selected_mode = 'adventure'
                                self.running = False
                            elif hovered_button.text == translations[current_language]['back']:
                                self.current_menu = self.main_menu
                                self.current_video = self.videos['main_menu']
                        elif self.current_menu == self.settings_menu:
                            if hovered_button.text == translations[current_language]['language']:
                                self.current_menu = self.language_menu
                                self.current_video = self.videos['language_menu']
                            elif hovered_button.text == translations[current_language]['back']:
                                self.current_menu = self.main_menu
                                self.current_video = self.videos['main_menu']
                    elif isinstance(self.current_menu, FlagMenu):
                        if hovered_button.text == translations[current_language]['back']:
                            self.current_menu = self.settings_menu
                            self.current_video = self.videos['settings_menu']
                        else:
                            current_language = language_options[language_options.index(hovered_button.text.lower())]
                            self.update_menus()
                            self.current_menu = self.settings_menu
                            self.current_video = self.videos['settings_menu']
                    elif isinstance(self.current_menu, CreditMenu):
                        if hovered_button.text == translations[current_language]['back']:
                            self.current_menu = self.main_menu
                            self.current_video = self.videos['main_menu']

            if hovered_button and not hovered_button.hovered:
                self.play_hover_sound()

            self.current_menu.draw(self.screen)
            if isinstance(self.current_menu, CreditMenu):
                self.current_menu.update()
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()

    def update_menus(self):
        self.main_menu = Menu([
            translations[current_language]['play'],
            translations[current_language]['settings'],
            translations[current_language]['credits'],
            translations[current_language]['quit']
        ], WIDTH // 2 - 150, HEIGHT // 2 - 60, pygame.font.Font(font_paths[current_language], 30))

        self.play_menu = Menu([
            translations[current_language]['combat_mode'],
            translations[current_language]['adventure_mode'],
            translations[current_language]['back']
        ], WIDTH // 2 - 150, HEIGHT // 2 - 60, pygame.font.Font(font_paths[current_language], 30))

        self.settings_menu = Menu([
            translations[current_language]['sound'],
            translations[current_language]['display'],
            translations[current_language]['control'],
            translations[current_language]['language'],
            translations[current_language]['back']
        ], WIDTH // 2 - 150, HEIGHT // 2 - 60, pygame.font.Font(font_paths[current_language], 30))

        self.language_menu = FlagMenu(language_options, WIDTH // 2 - 300, HEIGHT // 2 - 150, pygame.font.Font(font_paths[current_language], 20))
        self.credit_menu = CreditMenu(pygame.font.Font(font_paths[current_language], 20))

        self.language_menu.update_language()
        self.credit_menu.update_language()

if __name__ == "__main__":
    game_menu = GameMenu('francais')  # Default language
    game_menu.run()
