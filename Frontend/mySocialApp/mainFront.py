import flet
from flet import Page, Text, TextField, Checkbox, Column, Row, FloatingActionButton, icons, Icon, Image, Container, ElevatedButton
from dotenv import dotenv_values

environments = dotenv_values("../.env")


def main(page: Page):
    new_task = TextField(hint_text="Whats needs to be done?", expand=True)
    logo = Image(src=f"/logo.png", width=60, height=60)
    temp = Image(src=f"/logo.png", width=10, height=10)
    navBar = Container(
        Column(
            controls=[
                Row(
                    controls=[
                        logo,
                        Text(environments.get("APPNAME"), size=20),
                        ElevatedButton(text="Szukaj", color = "white", bgcolor = "TRANSPARENT", icon=temp),
                        ElevatedButton(text="Organizacje", color = "white", bgcolor = "TRANSPARENT"),
                        ElevatedButton(text="Zbiórki", color = "white", bgcolor = "TRANSPARENT"),
                        ElevatedButton(text="Zaloguj się", bgcolor = "green", color = "white"),
                    ],
                    alignment="center",
                ),
            ],
        ),
        padding=5,
        bgcolor="blue",
        height=100
    )

    page.padding=0
    page.horizontal_alignment = "center"
    page.add(navBar)



flet.app(port=8000,
         target=main,
         view=flet.WEB_BROWSER,
         assets_dir="resource")
