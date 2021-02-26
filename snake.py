# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 20:35:23 2020

@author: franc
"""
from time import sleep 
from cuesdk import CueSdk, CorsairLedId, CorsairLedPositions
from os import system, name 
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import random
import threading
import queue

import keyboard

from sys import exit



def get_available_leds():
    leds = list()
    device_count = sdk.get_device_count()
    for device_index in range(device_count):
        led_positions = sdk.get_led_positions_by_device_index(device_index)
        leds.append(led_positions)
    return leds


def clear(): 
  
    # for windows 
    if name == 'nt': 
        system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        system('clear') 

printgrid = lambda grid: [print(i) for i in grid]
nums = [[CorsairLedId.K_Escape, CorsairLedId.K_Mute, CorsairLedId.K_F1, CorsairLedId.K_F2, CorsairLedId.K_F3, CorsairLedId.K_F4, CorsairLedId.K_F5, CorsairLedId.K_F6, CorsairLedId.K_F7, CorsairLedId.K_F8, CorsairLedId.K_F9, CorsairLedId.K_F10, CorsairLedId.K_F11, CorsairLedId.K_F12, CorsairLedId.K_PrintScreen, CorsairLedId.K_ScrollLock, CorsairLedId.K_PauseBreak, CorsairLedId.K_Stop, CorsairLedId.K_ScanPreviousTrack, CorsairLedId.K_PlayPause, CorsairLedId.K_ScanNextTrack],
        [CorsairLedId.K_GraveAccentAndTilde, CorsairLedId.K_1, CorsairLedId.K_2, CorsairLedId.K_3, CorsairLedId.K_4, CorsairLedId.K_5, CorsairLedId.K_6, CorsairLedId.K_7, CorsairLedId.K_8, CorsairLedId.K_9, CorsairLedId.K_0, CorsairLedId.K_MinusAndUnderscore, CorsairLedId.K_EqualsAndPlus, CorsairLedId.K_Backspace, CorsairLedId.K_Insert, CorsairLedId.K_Home, CorsairLedId.K_PageUp, CorsairLedId.K_NumLock, CorsairLedId.K_KeypadSlash, CorsairLedId.K_KeypadAsterisk, CorsairLedId.K_KeypadMinus],
        [CorsairLedId.K_Tab, CorsairLedId.K_Q, CorsairLedId.K_W, CorsairLedId.K_E, CorsairLedId.K_R, CorsairLedId.K_T, CorsairLedId.K_Y, CorsairLedId.K_U, CorsairLedId.K_I, CorsairLedId.K_O, CorsairLedId.K_P, CorsairLedId.K_BracketLeft, CorsairLedId.K_BracketRight, CorsairLedId.K_Enter, CorsairLedId.K_Delete, CorsairLedId.K_End, CorsairLedId.K_PageDown, CorsairLedId.K_Keypad7, CorsairLedId.K_Keypad8, CorsairLedId.K_Keypad9, CorsairLedId.K_KeypadPlus],
        [CorsairLedId.K_CapsLock, CorsairLedId.K_A, CorsairLedId.K_S, CorsairLedId.K_D, CorsairLedId.K_F, CorsairLedId.K_G, CorsairLedId.K_H, CorsairLedId.K_J, CorsairLedId.K_K, CorsairLedId.K_L, CorsairLedId.K_SemicolonAndColon, CorsairLedId.K_ApostropheAndDoubleQuote, CorsairLedId.K_NonUsTilde, CorsairLedId.K_Mute, CorsairLedId.K_Mute, CorsairLedId.K_Mute, CorsairLedId.K_Mute, CorsairLedId.K_Keypad4, CorsairLedId.K_Keypad5, CorsairLedId.K_Keypad6, CorsairLedId.K_KeypadPlus],
        [CorsairLedId.K_LeftShift, CorsairLedId.K_NonUsBackslash, CorsairLedId.K_Z, CorsairLedId.K_X, CorsairLedId.K_C, CorsairLedId.K_V, CorsairLedId.K_B, CorsairLedId.K_N, CorsairLedId.K_M, CorsairLedId.K_CommaAndLessThan, CorsairLedId.K_PeriodAndBiggerThan, CorsairLedId.K_SlashAndQuestionMark, CorsairLedId.K_Mute,CorsairLedId.K_RightShift, CorsairLedId.K_Mute, CorsairLedId.K_UpArrow, CorsairLedId.K_Mute, CorsairLedId.K_Keypad1, CorsairLedId.K_Keypad2, CorsairLedId.K_Keypad3, CorsairLedId.K_KeypadEnter],
        [CorsairLedId.K_LeftCtrl, CorsairLedId.K_LeftGui, CorsairLedId.K_LeftAlt, CorsairLedId.K_Mute,CorsairLedId.K_Mute,CorsairLedId.K_Mute,CorsairLedId.K_Space, CorsairLedId.K_Mute,CorsairLedId.K_Mute,CorsairLedId.K_Mute,CorsairLedId.K_RightAlt, CorsairLedId.K_RightGui, CorsairLedId.K_Application, CorsairLedId.K_RightCtrl, CorsairLedId.K_LeftArrow, CorsairLedId.K_DownArrow, CorsairLedId.K_RightArrow, CorsairLedId.K_Keypad0, CorsairLedId.K_Mute, CorsairLedId.K_KeypadPeriodAndDelete, CorsairLedId.K_KeypadEnter]]

indices = [(255, 0, 0), (0, 255, 50), (50, 255, 0), (0, 0, 0)][::-1]
       
def printgame(board, all_leds):

    di = 0
    device_leds = all_leds[di]
    dic = {"X":" ", "A":"<", "D":">", "S":"v", "W":"^", "^":"O", "v":"O", "<":"O",">":"O", "a":"A"}
    dic2 = {"X":(0, 0, 0), "A":(50, 255, 0), "D":(50, 255, 0), "S":(50, 255, 0), "W":(50, 255, 0), "^":(0, 255, 50), "v":(0, 255, 50), "<":(0, 255, 50),">":(0, 255, 50), "a":(255, 0, 0)}
    out = ""
    for j in device_leds:
        device_leds[j] = (0, 0, 0)
    ghostCol = (0, 0, 0)
    for i in range(len(board)):
        out += "]"
        for j in range(len(board[i])):
            print(i,j)
            out += dic[board[i][j]] + " "
            device_leds[nums[i][j]] = dic2[board[i][j]]
            if nums[i][j] == CorsairLedId.K_Mute and indices.index(ghostCol) < indices.index( dic2[board[i][j]]):
                ghostCol = dic2[board[i][j]]
        out += "[\n"
    device_leds[CorsairLedId.K_Mute] = ghostCol
    device_leds[CorsairLedId.Oem1] = ghostCol
    device_leds[CorsairLedId.Oem2] = ghostCol
    sdk.set_led_colors_buffer_by_device_index(di, device_leds)
    sdk.set_led_colors_flush_buffer()
    print(out)
                
def keypress():
    while True:  
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed('up'):   
                return "W"
                break  
            elif keyboard.is_pressed('left'):  
                return "A"
                break  
            elif keyboard.is_pressed('down'):  
                return "S"
                break  
            elif keyboard.is_pressed('right'):  
                return "D"
                break  
            else:
                return "x"
                break
        except:
            break

class Snake:
    def __init__ (self):
        self.snake = [[0, 1, "D"]]
    def extend(self, direction):
        if direction.upper() == "W":
            self.snake.append([self.snake[-1][0], self.snake[-1][1] - 1, "W"])
        elif direction.upper() == "A":
            self.snake.append([self.snake[-1][0] - 1, self.snake[-1][1], "A"])
        elif direction.upper() == "S":
            self.snake.append([self.snake[-1][0], self.snake[-1][1] + 1, "S"])
        elif direction.upper() == "D":
            self.snake.append([self.snake[-1][0] + 1, self.snake[-1][1], "D"])
    def retract(self):
        self.snake = self.snake[1:]
             
class Board:  
    def __init__(self, size):
        self.board = [['X' for i in range(21)] for j in range(size)]
    def snakein(self, snake):
        "Puts a snake into the board"
        dictionary = {"A":">", "D":"<", "S":"^", "W":"v"}
        self.board[snake.snake[-1][1]][snake.snake[-1][0]] = dictionary[snake.snake[-1][2]]
        for i in range(len(snake.snake) - 1):
            self.board[snake.snake[i][1]][snake.snake[i][0]] = snake.snake[i][2]
            
    def applein(self):
        "Places an apple into the board as long as the snake isn't there"
        spaces = [(i, j) for i in range(len(self.board)) for j in range(len(self.board[0]))]
        spaces = list(filter(lambda pos: self.board[pos[0]][pos[1]] not in "WASD<>^v", spaces))
        if len(spaces) == 0:
            return True
        i, j = random.choice(spaces)
        self.board[i][j] = "a"
        return False
                
    def tailclear(self, snake):
        self.board[snake.snake[0][1]][snake.snake[0][0]] = "X"
                
def apple_test(snake, board):
    """Returns true if the head of the snake is in the same position as an apple,
    otherwise returns false. The head of the snake is the final element in the snake list.
    """
    return board.board[snake.snake[-1][1]][snake.snake[-1][0]] == "a"
    
    
def death_test(snake, board):
    """Retruns true if the snake head goes outside of the board, or if the snake head
    has the same position as any of the other coordinates in the snake object
    """
    if snake.snake[-1][0] >= len(board.board[0]) or snake.snake[-1][1] >= len(board.board) or snake.snake[-1][0] < 0 or snake.snake[-1][1] < 0:        
        return True
    else:
        for i in snake.snake[:-1]:
            if i[:-1] == snake.snake[-1][:-1]:                
                return True
    return False
            
def move_snake(snake, board):
    """Takes appletest and direction and chooses whether to extend or to move 
    the snake in a given direction
    """
    a = False  
    try:
        if apple_test(snake, board):
            a = True
        else:
            board.tailclear(snake)
            snake.retract()
    except:
      ...  
    return (death_test(snake, board), a)
        
        
"""
Insert snake, Insert apple, , print board, extend snake, test if snake eats apple if yes, extend, if no, , insert snake, insert apple
if snake ate an apple, counter +=1
"""     

def setup_keyboard():
    global sdk
    sdk = CueSdk()
    connected = sdk.connect()
    if not connected:
        err = sdk.get_last_error()
        print("Handshake failed: %s" % err)
        return

    
    colors = get_available_leds()
    
    return colors


   
def rungame():       
    board = Board(6)
    snake = Snake()   
    board.snakein(snake)
    clear()   
    all_leds = setup_keyboard()
    printgame(board.board, all_leds)    
    a = "D"
    b = "False"
    counter = -1
    input("Press Enter To Start")
    
    while a.upper() != "X": 
        
        if b:
            board.applein()
            counter += 1       
        clear()   
        printgame(board.board, all_leds)
        print("Score: " + str(counter))
        for i in range(6):
          if keypress() in "WASD":
            a = keypress()
          sleep(0.06)
        if a.upper() == "X":
            ...
        else:
            if keypress() in "WASD":
                 a = keypress()
            snake.extend(a)             
            dead, b = move_snake(snake, board)
            if dead:
                print("You Lose" + "\n" + "Score " + str(counter))
                file = open("Highscores.txt", "a")
                file.close()
                file = open("Highscores.txt")
                filelist = [int(i) for i in file]
                file.close()
                if len(filelist) == 0:
                    file = open("Highscores.txt", "a")                   
                    print("New High Score!")
                    file.write(str(counter) + "\n")
                    file.close()
                elif counter > filelist[-1]:
                    file = open("Highscores.txt", "a")                    
                    print("New High Score!")
                    file.write(str(counter)  + "\n")
                    file.close()
                file.close()
                if input("Press Enter to Play Again, X to exit ").upper() == "X":
                    exit()                   
                else:                    
                    rungame()                   
            if keypress() in "WASD":
                 a = keypress()    
            board.snakein(snake)
rungame()            







        



