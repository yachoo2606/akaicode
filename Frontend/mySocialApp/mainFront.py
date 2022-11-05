from math import pi

import flet
from flet import Page, Text, TextField, Column, Row, Image, Container, alignment, ElevatedButton, VerticalDivider
from dotenv import dotenv_values
from flet.transform import Rotate
from flet.types import BoxShape

environments = dotenv_values("../.env")


def makeNavBar(page: Page):
    logo = Image(src=f"/logo.png", width=60, height=60)
    navBar = Container(
        Row(
            controls=[
                Row(
                    controls=[
                        Row(
                            controls=[
                                logo,
                                Text(environments.get("APPNAME"), size=20)
                            ],
                            alignment="start"
                        ),
                        Row(
                            controls=[
                                ElevatedButton(text="Szukaj", color="white", bgcolor="TRANSPARENT"),
                                VerticalDivider(width=1, color="white"),
                                ElevatedButton(text="Organizacje", color="white", bgcolor="TRANSPARENT"),
                                VerticalDivider(width=1, color="white"),
                                ElevatedButton(text="Zbiórki", color="white", bgcolor="TRANSPARENT"),
                                VerticalDivider(width=1, color="white"),
                                ElevatedButton(text="Zaloguj się", bgcolor="green", color="white")
                            ],
                            alignment="center"
                        )
                    ],
                ),
            ],
        ),
        padding=5,
        image_src=f"/navBackground.png",
        image_fit="fitWidth",
        height=80,
    )
    page.add(navBar)
    return page


def makeFooter(page: Page):
    logo = Image(src=f"/logo.png", width=60, height=60)
    footer = Container(
        Column(
            controls=[
                Row(
                    controls=[
                        logo,
                        Text(environments.get("APPNAME"), size=20),
                    ],
                ),
            ],
        ),
        padding=5,
        image_src=f"/footerBackground.png",
        image_fit="fitWidth",
        height=150,
        alignment=alignment.bottom_center,
    )
    page.add(footer)
    return page


def main(page: Page):
    new_task = TextField(hint_text="Whats needs to be done?", expand=True)
    page = makeNavBar(page)
    page.add(Text("Hello world"))
    page = makeFooter(page)

    page.padding = 0
    page.horizontal_alignment = "center"


flet.app(port=8000,
         target=main,
         view=flet.WEB_BROWSER,
         assets_dir="resource")
