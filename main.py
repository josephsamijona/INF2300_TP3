import intro
import menu
import battle

if __name__ == "__main__":
    while True:
        # Create an instance of the Game class from intro.py and run the intro sequence
        intro_game = intro.Game(1200, 600)
        selected_language = intro_game.run()
        
        # Once the intro sequence is complete, launch the main menu with the selected language
        game_menu = menu.GameMenu(selected_language)
        game_menu.run()
        
        # If Adventure mode is selected, launch it
        if game_menu.selected_mode == 'adventure':
            battle.run_adventure_mode()
