import pygame
import game_functions as gf

from settings import Settings
from people import People
from stars import Stars
from alien import Alien
from pygame.sprite import Group
from button import Button
from game_stats import GameStats
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pick the stars")

    people = People(ai_settings, screen)
    stars = Stars(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    play_button = Button(ai_settings, screen, "Play")

    while True:
        gf.check_events(ai_settings,stats, sb, people, alien, bullets, play_button)
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom >= ai_settings.screen_height:
                bullets.remove(bullet)
        if stats.game_active:
            people.update()
            gf.update_alien(alien)
            gf.update_stars(ai_settings, stats, sb, people, stars)
            if alien.rect.x % 120 == 0:
                gf.update_bullet(ai_settings, stats, screen, people, alien, bullets)

        gf.update_screen(ai_settings, stats, sb, screen, people, stars, alien, bullets, play_button)


run_game()