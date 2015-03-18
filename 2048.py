import pygame
import random
from pygame.locals import *
from sys import exit


class NumRect(pygame.Surface):
	def __init__(self,num):
		pygame.Surface.__init__(self,(80,80))
		if num == 0:
			pygame.draw.rect(self,pygame.Color(255,255,255), pygame.Rect((2,2),(76,76)))
		elif num == 2:
			text='2'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(255,255,55), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )
		elif num == 4:
			text='4'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(255,155,55), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )
		elif num == 8:
			text='8'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(255,155,155), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )
		elif num == 16:
			text='16'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(255,55,155), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 32:
			text='32'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(155,55,155), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 64:
			text='64'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(55,55,155), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 128:
			text='128'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(55,55,55), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 256:
			text='256'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(55,55,255), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 512:
			text='512'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(55,255,55), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 1024:
			text='1024'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(255,55,55), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )

		elif num == 2048:
			text='2048'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(255,55,0), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )
		elif num == 4096:
			text='4096'
			self.font = pygame.font.SysFont("arial", 35);
			pygame.draw.rect(self,pygame.Color(55,55,0), pygame.Rect((2,2),(76,76)))
			w,h = self.font.size(text)
			self.blit( self.font.render(text, True, (0, 0, 0)), ((80-w)/2, (80-h)/2) )
class GameRects:
	def __init__(self):
		self.num_arr=[
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,2,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]
			]
	def click(self, direct, step):
		print(direct, step)
		if step == 1:
			self.move(direct)
		if step == 2:
			self.join(direct)
		if step == 3:
			self.append()
	def move(self, direct):
		if direct == 'l':
			for i in range(5):
				j = 0
				k = 0
				for j in range(5):
					if self.num_arr[i][j] !=0:
						k = j
				ii = 0
				while ii<k:
					if self.num_arr[i][ii] == 0:
						del self.num_arr[i][ii]
						self.num_arr[i].append(0)
						k = k -1
					else:
						ii = ii+1
		if direct == 'r':
			for i in range(5):
				j = 0
				k = 0
				for j in range(1,6):
					if self.num_arr[i][-j] !=0:
						k = 4-j
				ii = 4
				print(k)
				while ii>=k:
					if self.num_arr[i][ii] == 0:
						del self.num_arr[i][ii]
						self.num_arr[i].insert(0,0)
						k = k +1
					else:
						ii = ii-1
		if direct == 'u':
			for i in range(5):
				k = 0
				for j in range(5):
					if self.num_arr[j][i] !=0:
						tmp = self.num_arr[j][i]
						self.num_arr[j][i]=0
						self.num_arr[k][i]=tmp
						k=k+1

		if direct == 'd':
			for i in range(5):
				k = 1
				for j in range(1,6):
					if self.num_arr[-j][i] !=0:
						tmp = self.num_arr[-j][i]
						self.num_arr[-j][i]=0
						self.num_arr[-k][i]=tmp
						k=k+1

	def join(self, direct):
		tmp_line = [0,0,0,0,0]
		if direct == 'l':
			for i in range(5):
				k = 0
				j = 0
				while k<4:
					if self.num_arr[i][k] == self.num_arr[i][k+1]:
						tmp_line[j] = self.num_arr[i][k]*2
						k = k + 2
					else:
						tmp_line[j] = self.num_arr[i][k]
						k = k + 1
					j = j+1
				for ii in range(5):
					self.num_arr[i][ii] = tmp_line[ii]

		if direct == 'r':
			for i in range(5):
				for j in range(1,5):
					if self.num_arr[i][-j] == self.num_arr[i][-(j+1)]:
						self.num_arr[i][-j] = self.num_arr[i][-j]*2
						del self.num_arr[i][-(j+1)]
						self.num_arr[i].insert(0,0)

		if direct == 'u':
			for i in range(5):
				for j in range(4):
					if self.num_arr[j][i] == self.num_arr[j+1][i]:
						self.num_arr[j][i] = self.num_arr[j][i]*2
						for k in range(j+1,4):
							self.num_arr[k][i]=self.num_arr[k+1][i]
						self.num_arr[4][i] = 0

		if direct == 'd':
			for i in range(5):
				for j in range(1,5):
					if self.num_arr[-j][i] == self.num_arr[-(j+1)][i]:
						self.num_arr[-j][i] = self.num_arr[-j][i]*2
						for k in range(j+1,5):
							print(k)
							self.num_arr[-k][i]=self.num_arr[-(k+1)][i]
						self.num_arr[0][i] = 0
	def append(self):
		blank_num = 0
		for i in range(5):
			for j in range(5):
				if self.num_arr[i][j]==0:
					blank_num=blank_num+1
		if blank_num == 0:
			return False

		fill_num = random.randint(1, blank_num)
		double =  random.randint(1, 2)

		for i in range(5):
			for j in range(5):
				if self.num_arr[i][j]==0:
					fill_num = fill_num -1
					if fill_num == 0:
						self.num_arr[i][j] = 2*double
						return True


class Screen:
	def __init__(self):
		self.game_rects = GameRects()
	def run(self):
		pygame.init()
		screen = pygame.display.set_mode((480, 480), 0, 32)
		pygame.display.set_caption("2048")


		while True:
			game_area=pygame.Surface((400,400))

			game_rects = self.game_rects


			event = pygame.event.wait()
			key = '0'
			if event.type == QUIT:
				exit()
			if event.type == KEYDOWN:
				if event.key == K_UP:
					key = 'u'
				if event.key == K_DOWN:
					key = 'd'
				if event.key == K_LEFT:
					key = 'l'
				if event.key == K_RIGHT:
					key = 'r'


			for step in range(1,4):
				if key != '0':
					game_rects.click(key,step) 
				for i in range(5):
					for j in range(5):	
						num_rect = NumRect(game_rects.num_arr[i][j])
						game_area.blit(num_rect,(80*j,80*i))

				screen.blit(game_area,(40,40))
				pygame.display.update()

screen = Screen()
screen.run()
