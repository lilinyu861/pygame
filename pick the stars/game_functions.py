import sys
import pygame
from bullets import Bullets


def check_events(ai_settings, stats, sb, people, alien, bullets, play_button):
    # 响应按键和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                people.moving_left = True
            elif event.key == pygame.K_RIGHT:
                people.moving_right = True
            elif event.key == pygame.K_UP:
                people.moving_up = True
            elif event.key == pygame.K_DOWN:
                people.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                people.moving_left = False
            elif event.key == pygame.K_RIGHT:
                people.moving_right = False
            elif event.key == pygame.K_UP:
                people.moving_up = False
            elif event.key == pygame.K_DOWN:
                people.moving_down = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, sb, people, alien, bullets, play_button, mouse_x, mouse_y)


def check_play_button(ai_settings, stats, sb, people, alien, bullets, play_button, mouse_x, mouse_y):
    # 游戏开始按钮
        if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
            stats.reset_stats()
            sb.prep_score()
            ai_settings.initialize_dynamic_settings()
            stats.game_active = True
            # 隐藏光标
            # pygame.mouse.set_visible(False)
            # 清空列表
            bullets.empty()
            alien.left_alien()
            people.center_people()


def update_screen(ai_settings, stats, sb, screen, people, stars, alien, bullets, play_button):
    # 更新屏幕画面
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # if alien.rect.x % 100 == 0:
        # update_bullet(ai_settings, screen, people, alien, bullets)

    people.blitme()
    stars.blitme()
    alien.blitme()
    # 显示得分
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_stars(ai_settings, stats, sb, people, stars):
    # 更新星星位置
    if pygame.sprite.collide_mask(people, stars):
        stats.score += ai_settings.star_points
        sb.prep_score()
        print("+10")
        stars.update()


def update_alien(alien):
    # 更新外星飞船的位置
    alien.check_edge()
    alien.update()


def update_bullet(ai_settings, stats, screen, people, alien, bullets):
    # 更新外星飞船发射子弹
    new_bullet = Bullets(ai_settings, screen, alien)
    bullets.add(new_bullet)
    for bullet in bullets.copy():
        if bullet.rect.bottom >= ai_settings.screen_height:
            bullets.remove(bullet)
    check_bullet_people_collision(stats, people, alien, bullets)


def check_bullet_people_collision(stats, people, alien, bullets):
    if pygame.sprite.spritecollide(people, bullets, True) or pygame.sprite.collide_circle(alien, people):
        stats.game_active = False


