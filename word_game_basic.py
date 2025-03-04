import pygame
import random
import time
import csv

width = 600
height = 400
Display = pygame.display.set_mode((width, height))
pygame.display.set_caption("단어 맞추기 게임")
pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont("malgungothic", 30)

def load_words(filename):
    with open(filename, "r") as f:
        words = [line.strip() for line in f]
    return words

def random_words(words, num_words):
    return random.sample(words, num_words)

words = load_words("data/word.txt")
target_words = random_words(words, 10) 
user_inputs = [""] * 10
current_word_index = 0
correct_count = 0
game_finish = False
input_active = True
start_time = time.time()
time_limit = 5
word_positions = [None] * 10

game_running = True
while game_running:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN and not game_finish and input_active:
            if event.key == pygame.K_RETURN:
                if user_inputs[current_word_index] == target_words[current_word_index]:
                    correct_count += 1
                    pygame.mixer.music.load('assets/good.wav')
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.load("assets/bad.wav")
                    pygame.mixer.music.play()
                current_word_index += 1
                if current_word_index >= 10:
                    game_finish = True
                    input_active = False
                else:
                    start_time = time.time()
            elif event.key == pygame.K_BACKSPACE:
                user_inputs[current_word_index] = user_inputs[current_word_index][:-1]
            elif event.unicode.isalpha() or event.unicode.isprintable():
                user_inputs[current_word_index] += event.unicode

    Display.fill((255, 255, 255))

    if current_word_index < 10:
        if current_time - start_time > time_limit:
            pygame.mixer.music.load("assets/bad.wav")
            pygame.mixer.music.play()
            current_word_index += 1
            if current_word_index >= 10:
                game_finish = True
                input_active = False
            else:
                start_time = time.time()
        else:
            if word_positions[current_word_index] is None:
                random_x = random.randint(100, 400)
                random_y = random.randint(50, 300)
                word_positions[current_word_index] = (random_x, random_y)

            text = font.render(f"{target_words[current_word_index]}", True, (0, 0, 0))
            Display.blit(text, word_positions[current_word_index])

            input_text = font.render(f"정답 {current_word_index + 1}: {user_inputs[current_word_index]}", True, (0, 0, 0))
            input_rect = input_text.get_rect(center=(width // 2, height * 9 // 10))
            Display.blit(input_text, input_rect)

    if game_finish:
        end_time = time.time()
        game_time = end_time - start_time
        result_text = font.render(f"맞춘 개수: {correct_count} / 10", True, (0, 0, 0))
        Display.blit(result_text, (200, 350))
        if correct_count >= 7:
            final_result_text = font.render("합격입니다!", True, (0, 0, 0))
        else:
            final_result_text = font.render("불합격입니다!", True, (0, 0, 0))
        final_result_rect = final_result_text.get_rect(center=(width // 2, height // 2))
        Display.blit(final_result_text, final_result_rect)

        with open('word_game_score.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['게임 시간', '맞춘 개수'])
            writer.writerow([game_time, correct_count])

    pygame.display.flip()

pygame.quit()