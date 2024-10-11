from menu_window_creation import create_menu

def transition_to_menu(root):
    root.after(1000,lambda: create_menu(root))