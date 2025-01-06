from flet import Text, app, Page


def main(page: Page):
    page.add(Text("Hello"))


app(main, assets_dir="assets")
