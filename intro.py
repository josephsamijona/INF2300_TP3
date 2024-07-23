import pygame
import sys
import cv2
from mutagen.mp3 import MP3

class Game:
    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption("Animation d'Ouverture et Menu de Choix de Langue")
        self.background_color = (156, 177, 188)  # Converti de HEX #9cb1bc à RGB
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

    def run(self):
        self.play_opening_animation()
        selected_language = self.show_language_selection_menu()
        if selected_language:
            self.play_intro_video(selected_language)
        return selected_language  # Retourner la langue sélectionnée

    def play_opening_animation(self):
        animation = OpeningAnimation(self.screen, self.background_color)
        animation.play()

    def show_language_selection_menu(self):
        menu = LanguageSelectionMenu(self.screen, self.background_color, self.WHITE, self.BLACK)
        return menu.show()

    def play_intro_video(self, language_key):
        trailer = TrailerPlayer(self.screen, self.width, self.height)
        trailer.play(language_key)


class OpeningAnimation:
    def __init__(self, screen, background_color):
        self.screen = screen
        self.background_color = background_color
        self.logo = pygame.image.load('assets/images/BUSKO_INTERACTIVE.png')
        original_rect = self.logo.get_rect()
        scale_factor = 0.8
        new_size = (int(original_rect.width * scale_factor), int(original_rect.height * scale_factor))
        self.logo = pygame.transform.scale(self.logo, new_size)
        self.logo_rect = self.logo.get_rect(center=(screen.get_width() // 2, screen.get_height() + 30))
        self.sound_effect = pygame.mixer.Sound('assets/song/SkywardHero_UI (1).wav')
        self.logo_speed = -10
        self.rotation_speed = 5
        self.current_angle = 0
        self.moving_down = True
        self.rotating = False
        self.played_sound = False

    def play(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

            if self.moving_down:
                self.logo_rect.y += self.logo_speed
                if self.logo_rect.centery <= self.screen.get_height() // 2:
                    self.moving_down = False
                    self.rotating = True
                    if not self.played_sound:
                        self.sound_effect.play()
                        self.played_sound = True

            if self.rotating:
                self.current_angle += self.rotation_speed
                if self.current_angle >= 360:
                    self.current_angle = 0
                    self.rotating = False
                    running = False

            self.screen.fill(self.background_color)
            rotated_logo = pygame.transform.rotate(self.logo, self.current_angle)
            new_rect = rotated_logo.get_rect(center=self.logo_rect.center)
            self.screen.blit(rotated_logo, new_rect)
            pygame.display.flip()
            pygame.time.Clock().tick(60)


class LanguageSelectionMenu:
    def __init__(self, screen, background_color, white, black):
        self.screen = screen
        self.background_color = background_color
        self.WHITE = white
        self.BLACK = black
        self.title_font = pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 40)
        self.hover_sound = pygame.mixer.Sound("assets/song/Unholy UI - Souls (14).wav")
        self.click_sound = pygame.mixer.Sound("assets/song/Unholy UI - Souls (10).wav")
        self.flags = {
            "kreyol": ("Kreyòl", pygame.image.load("assets/images/flags/Haiti.png")),
            "francais": ("Français", pygame.image.load("assets/images/flags/france.png")),
            "anglais": ("English", pygame.image.load("assets/images/flags/usa.png")),
            "espagnol": ("Español", pygame.image.load("assets/images/flags/spain.png")),
            "russe": ("Русский", pygame.image.load("assets/images/flags/russie.png")),
            "chinois": ("中文", pygame.image.load("assets/images/flags/chine.png")),
            "coréen": ("한국어", pygame.image.load("assets/images/flags/south_korea.png")),
            "japonais": ("日本語", pygame.image.load("assets/images/flags/japan.png")),
            "hindi": ("हिन्दी", pygame.image.load("assets/images/flags/inde.png")),
            "allemand": ("Deutsch", pygame.image.load("assets/images/flags/germany.png")),
            "indonésien": ("Bahasa Indonesia", pygame.image.load("assets/images/flags/indonesie.png")),
            "arabe": ("العربية", pygame.image.load("assets/images/flags/emirate.png"))
        }
        self.flags = {lang: (name, pygame.transform.scale(img, (100, 100))) for lang, (name, img) in self.flags.items()}
        self.fonts = {
            "kreyol": pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 20),
            "francais": pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 20),
            "anglais": pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 20),
            "espagnol": pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 20),
            "russe": pygame.font.Font("assets/fonts/SevenFifteenMonoRounded-Regular.ttf", 20),
            "chinois": pygame.font.Font("assets/fonts/ipix_12pxchinese.ttf", 20),
            "coréen": pygame.font.Font("assets/fonts/DungGeunMo.ttf", 20),
            "japonais": pygame.font.Font("assets/fonts/SevenFifteenMonoRounded-Regular.ttf", 20),
            "hindi": pygame.font.Font("assets/fonts/SevenFifteenMonoRounded-Regular.ttf", 20),
            "allemand": pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 20),
            "indonésien": pygame.font.Font("assets/fonts/PIXEL LATIN.ttf", 20),
            "arabe": pygame.font.Font("assets/fonts/SevenFifteenMonoRounded-Regular.ttf", 20)
        }
        self.margin_x, self.margin_y = 60, 45  # Marges augmentées
        self.button_width, self.button_height = 100, 100

    def calculate_button_positions(self, screen_width, screen_height):
        start_x = (screen_width - (3 * self.button_width + 2 * self.margin_x)) // 2
        start_y = (screen_height - (4 * self.button_height + 3 * self.margin_y)) // 2
        positions = [(start_x + (i % 3) * (self.button_width + self.margin_x), start_y + (i // 3) * (self.button_height + self.margin_y)) for i in range(len(self.flags))]
        return positions

    def show(self):
        selected_language = None
        running = True
        while running:
            self.screen.fill(self.background_color)
            
            # Obtenir la taille actuelle de l'écran
            current_width, current_height = self.screen.get_size()
            button_positions = self.calculate_button_positions(current_width, current_height)
            
            # Afficher le titre
            title_surface = self.title_font.render("Choisissez votre langue", True, self.WHITE)
            title_rect = title_surface.get_rect(center=(current_width // 2, 50))
            self.screen.blit(title_surface, title_rect)

            # Gestion des événements
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i, (lang, pos) in enumerate(zip(self.flags.keys(), button_positions)):
                        if self.flags[lang][1].get_rect(topleft=pos).collidepoint(mouse_pos):
                            self.click_sound.play()
                            selected_language = lang
                            running = False

            # Dessiner les boutons et les noms des langues
            for i, (lang, pos) in enumerate(zip(self.flags.keys(), button_positions)):
                name, img = self.flags[lang]
                img_rect = img.get_rect(topleft=pos)
                self.screen.blit(img, img_rect)
                
                # Afficher le nom de la langue en dessous du drapeau
                font = self.fonts[lang]
                text_surface = font.render(name, True, self.BLACK)
                text_rect = text_surface.get_rect(center=(img_rect.centerx, img_rect.bottom + 30))  # Ajusté pour tenir compte de la marge_y augmentée
                self.screen.blit(text_surface, text_rect)
                
                if img_rect.collidepoint(mouse_pos):
                    self.hover_sound.play()
                    pygame.draw.rect(self.screen, self.WHITE, img_rect, 2)
            
            pygame.display.flip()
            pygame.time.Clock().tick(30)
        
        return selected_language


class TrailerPlayer:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height

    def play(self, language_key):
        video_file = 'assets/video/0718 (1).mp4'
        audio_files = {
            'kreyol': 'assets/song/dube/epic_kreyol_dub.mp3',
            'francais': 'assets/song/dube/version_fr.mp3',
            'anglais': 'assets/song/dube/version_eng.mp3',
            'espagnol': 'assets/song/dube/version_es.mp3',
            'allemand': 'assets/song/dube/version_german.mp3',
            'chinois': 'assets/song/dube/version_chinese.mp3',
            'hindi': 'assets/song/dube/version_hindi.mp3',
            'japonais': 'assets/song/dube/version_jap.mp3',
            'indonésien': 'assets/song/dube/version_indo.mp3',
            'arabe': 'assets/song/dube/version_arab.mp3',
            'russe': 'assets/song/dube/version_russe.mp3',
            'coréen': 'assets/song/dube/version_kr.mp3'
        }

        # Load the video
        cap = cv2.VideoCapture(video_file)
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps == 0:
            fps = 30  # Set a default value for fps if it's zero
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_duration = frame_count / fps

        # Get the duration of the audio file
        audio_duration = MP3(audio_files[language_key]).info.length

        # Calculate the total duration needed for the video
        total_duration = max(video_duration, audio_duration)

        # Function to play audio
        def play_audio(language_key, start_time):
            if language_key in audio_files:
                pygame.mixer.music.load(audio_files[language_key])
                pygame.mixer.music.play(start=start_time)
                # Print feedback for language change
                print(f"Language changed to {language_key} at {start_time:.2f} seconds")

        # Play the audio for the selected language
        play_audio(language_key, 0.0)

        # Main loop to play the video
        running = True
        frame_number = 0
        last_frame = None
        while running and cap.isOpened():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.width, self.height = self.screen.get_size()

            # Read the next frame
            ret, frame = cap.read()
            if not ret:
                break

            frame_number += 1
            current_time = frame_number / fps

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame_rgb = cv2.resize(frame_rgb, (self.width, self.height))  # Resize the frame to fit the screen
            frame_rgb = cv2.transpose(frame_rgb)
            frame_rgb = cv2.flip(frame_rgb, 0)
            surface = pygame.surfarray.make_surface(frame_rgb)
            self.screen.blit(surface, (0, 0))
            pygame.display.flip()

            last_frame = surface  # Store the last frame

            pygame.time.delay(int(1000 / fps))

        # If the audio is longer than the video, display the last frame for the remaining audio duration
        remaining_duration = total_duration - video_duration
        if remaining_duration > 0:
            remaining_frames = int(remaining_duration * fps)
            for _ in range(remaining_frames):
                self.screen.blit(last_frame, (0, 0))
                pygame.display.flip()
                pygame.time.delay(int(1000 / fps))

        # Release resources
        cap.release()


if __name__ == "__main__":
    game = Game(1200, 600)
    game.run()
