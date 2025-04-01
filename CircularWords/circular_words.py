#!/usr/bin/env python3
# coding=utf-8

import inkex
from inkex.elements import Group, TextElement
import math

class CircularWords(inkex.EffectExtension):

    def add_arguments(self, pars):
        pars.add_argument("--text", type=str, default="1 2 Hallo Wereld", help="Woorden die in een cirkel moeten staan")
        pars.add_argument("--radius", type=float, default=100.0, help="Straal van de cirkel")
        pars.add_argument("--font_size", type=float, default=20.0, help="Lettergrootte")
        pars.add_argument("--direction", type=str, choices=['out', 'in'], default='out', help="Plaats tekst binnen of buiten de cirkel")
        pars.add_argument("--angle_offset", type=float, default=0.0, help="Beginhoek voor de tekst")
        pars.add_argument("--flip", type=inkex.Boolean, default=False, help="Spiegel de tekst")

    def effect(self):
        # Tekst ophalen en omzetten naar lijst van woorden
        words = self.options.text.split()  # Split op spaties
        radius = self.options.radius
        num_words = len(words)
        font_size = self.options.font_size
        direction = self.options.direction
        angle_offset = self.options.angle_offset - 90
        flip = self.options.flip

        # Hoekstap berekenen
        angle_step = 360 / num_words  # graden per woord

        # Groep maken om alles in te zetten
        group = Group()
        self.svg.get_current_layer().add(group)

        for i, word in enumerate(words):
            angle = (i * angle_step + angle_offset)  # hoeken aanpassen door de beginhoek
            angle_rad = math.radians(angle)  # omzetten naar radialen

            # Coördinaten berekenen
            if direction == 'out':
                x = (radius + font_size / 2) * math.cos(angle_rad)
                y = (radius + font_size / 2) * math.sin(angle_rad)
            else:
                x = (radius - font_size / 2) * math.cos(angle_rad)
                y = (radius - font_size / 2) * math.sin(angle_rad)

            # Tekstelement maken
            text_element = TextElement()
            text_element.text = word
            text_element.set("x", str(x))
            text_element.set("y", str(y))
            text_element.set("font-size", str(font_size))
            text_element.set("text-anchor", "middle")
            text_element.set("dominant-baseline", "central")

            # Roteer de tekst (naar buiten of naar binnen) en spiegel indien gewenst
            if flip:
                text_element.set("transform", f"rotate({angle + 90}, {x}, {y}) scale(-1,1)")
            else:
                text_element.set("transform", f"rotate({angle + 90}, {x}, {y})")

            # Toevoegen aan de groep
            group.add(text_element)

# Script starten
if __name__ == '__main__':
    CircularWords().run()
