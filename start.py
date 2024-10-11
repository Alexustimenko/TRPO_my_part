from logo_function import create_logo
from menu_switcher import transition_to_menu
from imports import Tk
def main():
    root = Tk()
    create_logo(root)
    root.mainloop()
if __name__ == "__main__":
    main()