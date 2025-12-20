import tkinter as tk


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Buttons")
        self.resizable(width=False, height=False)

        number_of_rows = 8
        number_of_columns = 8

        for y in range(number_of_rows):
            for x in range(number_of_columns):
                button = tk.Button(self, text=f"{x}, {y}")
                button.config(command=lambda button=button: Application.on_button_click(button))
                button.grid(column=x, row=y)

    @staticmethod
    def on_button_click(button):
        button.config(bg="green")
        print(f"You clicked on {button['text']}")


def main():

    application = Application()
    application.mainloop()

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())