#WATER FILLING PROGRAM WITH OUT OVERFLOW
from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import sys
from numpy import*
t=0
dt=1
e=0
de=1
x=-8
y=0
def init():
	glClearColor(1.0,1.0,1.0,1.0)
	gluOrtho2D(-100,100,-100,100)
def idle():
	glutPostRedisplay()
def i():
	glClear(GL_COLOR_BUFFER_BIT)
	#bucket
	glColor3f(1.0,0,0.0)
	glBegin(GL_LINES)
	glVertex2f(-10,0)
	glVertex2f(10,0)
	glVertex2f(10,0)
	glVertex2f(10,20)
	glVertex2f(-10,0)
	glVertex2f(-10,20)
	glEnd()
	wtr()
	glFlush()
def wtr():
	global dt,t,e,de,x,y
	t=t+.1*dt
	r=0
	e=e+.001*de
	#pipe
	glPointSize(8.0)
	glColor3f(1.0,0.9,0.0)
	glBegin(GL_POINTS)
	glVertex2f(-8,52)
	glEnd()	
	glPointSize(2.0)
	glBegin(GL_POLYGON)
	glVertex2f(-19,53)
	glVertex2f(-14,53)
	glVertex2f(-14,58)
	glVertex2f(-19,58)
	glEnd()
	
	glBegin(GL_LINES)
	glVertex2f(-20,53)
	glVertex2f(-8,53)
	glVertex2f(-20,53)
	glVertex2f(-25,53)
	glVertex2f(-8,50)
	glVertex2f(-25,50)	
	glEnd()
	#water
	glColor3f(0.0,1.0,0.0)
	glBegin(GL_LINES)
	glVertex2f(-8,50)
	glVertex2f(-8,50-t)
	glEnd()
	if t>=50:
		t=0
	glPointSize(2.0)
	glBegin(GL_POINTS)
	for a in arange(-10,11,1):
		for r in arange(20,1,-1):
			glVertex2f(a,(t*.01)+e)
	glEnd()
	if e >= 20:
		dt=0
		de=0
	glFlush()
def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
	glutInitWindowPosition(50,50)
	glutInitWindowSize(500,500)
	glutCreateWindow("t")
	glutDisplayFunc(i)
	glutIdleFunc(idle)
	init()
	glutMainLoop()
main()
