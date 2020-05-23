from main import Main

class TestCs:
    def setup(self):
        main = Main()
        main.click_first_link().title()