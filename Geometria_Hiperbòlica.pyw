from tkinter import * 
from tkinter import messagebox
import math
from PIL import Image, ImageTk
import numpy
import winsound
import os
from threading import Thread
import pygame
import time

#----Basic per inicar programa----

root=Tk()

root2=Tk()

root3=Tk()

myFrame=Frame()

myFrame.pack(fill="both", expand="True")

disc=Canvas(root, bg="black", width="600", height="600", bd=-1)

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

disc.create_circle(300, 300, 300, fill="white", outline="")

#----Personalitzar el programa----

root.title("Geometria Hiperbòlica")

root.iconbitmap("Imatges\\Disc_de_Poincaré.ico")

root.resizable(0,0)

root.config(bd=20, relief="groove", bg="grey")

root2.title("Resultats")

root2.iconbitmap("Imatges\\Disc_de_Poincaré.ico")

root2.config(width=300, height=100)

root2.resizable(0,0)

root2.config(bd=20, relief="sunken", bg="grey")

root3.title("Instruccions")

root3.iconbitmap("Imatges\\Disc_de_Poincaré.ico")

root3.config(width=300, height=100)

root3.resizable(0,0)

root3.config(bd=20, relief="sunken", bg="grey")

myFrame.config(bg="grey")

pygame.init()
pygame.mixer.init()

musica=True

def play_sound_fondo():
	while musica==True:
		pygame.mixer.Channel(0).play(pygame.mixer.Sound("Sons\\Melodyloops-Season-of-joy.wav"))
		time.sleep(38)


thread = Thread(target=play_sound_fondo)
thread.start()

def play_sound_botò():
	pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sons\\Botò.wav"))


def play_sound_clic():
	pygame.mixer.Channel(2).play(pygame.mixer.Sound("Sons\\Clic.wav"))

idioma=StringVar(myFrame)
idioma.set("Català")
idiomes_possibles=["Català", "Español", "English", "Deutsch"]
idiomes_possibles=OptionMenu(myFrame, idioma, *idiomes_possibles)
idiomes_possibles.config(width=10, bg="lightgrey")
idiomes_possibles.grid(row=1, column=0)

funcions_h=StringVar(myFrame)
funcions_h.set("Funcions 1")
funcions_possibles=["Funcions 1", "Funcions 2"]
funcions_possibles=OptionMenu(myFrame, funcions_h, *funcions_possibles)
funcions_possibles.config(width=10, bg="lightgrey")
funcions_possibles.grid(row=0, column=0)

frases_català1=["Recta 2 punts", "Semirecta 2 punts", "Segment 2 punts", "Cercle centre i punt", "Cercle 3 punts", "Cercle complet", "Eliminar linies", "Informació", "Com usar el programa", "Per a usar aquest programa cal clicar els punts del disc desitjats i seguidament clicar la funció que es vulgui dibuixar. Els botons et diràn quants punts son necessaris i al clicar en ells sense haber marcat suficients punts no creara cap dibuix pero el la finestra d'instruccions et donarà informaciò mès detallada sobre com executar correctament dita funció."]
frases_castellà1=["Recta 2 puntos", "Semirecta 2 puntos", "Segmento 2 puntos", "Circulo centro y punto", "Circulo 3 puntos", "Circulo completo", "Eliminar lineas", "Información", "Como usar el programa", "Para usar este programa se deben clicar los puntos del disco deseados y seguidamente clicar la función que se quiera dibujar. Los botones te dirán quantos puntos son necesarios y al clicar en ellos sin haber marcado suficientes puntos no creara dibujo alguno pero en la ventana de instrucciones te dará información más detallada sobre como ejecutar correctamente dicha función."]
frases_anglès1=["Line 2 points", "Ray 2 points", "Line segment 2 points", "Circle center and point", "Circle 3 points", "Complete circle", "Delete lines", "Information", "How to use the program", "To use this program you have to click on the desired points of the disc and then click on the function you want to draw. The buttons will tell you how many points are needed and clicking on them without having marked enough points will not create any drawing but the in instruction window it will give you more detailed information on how to properly execute this function."]
frases_alemà1=["Linie 2 Punkte", "Strahl 2 Punkte", "Liniensegment 2 Punkte", "Kreis Zentrum und Punkt", "Kreis 3 Punkte", "Kreis vervollständigen", "Linien löschen", "Informationen", "Wie man dieses Programm benutzt", "Um dieses Programm zu verwenden, müssen Sie auf die gewünschten Punkte der Disc und dann auf die Funktion klicken, die Sie zeichnen möchten. Die Schaltflächen geben an, wie viele Punkte benötigt werden, und klicken auf diese, ohne genügend Punkte markiert zu haben erstellt keine Zeichnung, aber im Anweisungsfenster erhalten Sie detailliertere Informationen zur ordnungsgemäßen Ausführung dieser Funktion."]

frases_català2=["Triangle 3 punts", "Triangle complet", "Segment complet", "Valor absolut", "Quadrilater 4 punts","Quadrilater complet","Eliminar resultats", "Agraiments", "Agraiments", "Voldria agrair tant als meus tutors d'aquest treball: Vanessa Florenza Royes (docent de Vedruna Balaguer), Roberto Rubio Nuñez (catedràtic de la UAB), al programa Argò, sense el qual no hauria conegut mai aquest tema ni a Roberto, i finalment a ma mare Mª Dolors Díaz Salud, tots ells per haber-me apoiat durant aquest tragecte. D'igual forma voldria donar gracies a Llum Ruiz Capdevila (docent de Vedruna Balaguer) qui ha ajudat a perfeccionar visualment aquest programa."]
frases_castellà2=["Triangulo 3 puntos", "Triangulo completo", "Segmento completo", "Valor absoluto", "Cuadrilatero 4 puntos","Cuadrilateeo completo","Eliminar resultados", "Agraimentos", "Agraimentos", "Queria agrair tanto a mis tutores de este trabajo: Vanessa Florenza Royes (docente de Vedruna Balaguer), Roberto Rubio Nuñez (catedrático de la UAB), al programa Argò, sin el qual no habria conocido nunca este tema ni a Roberto, y finalmente a mi madre Mª Dolors Díaz Salud, todos ellos per haberme apoiado durante este trayecto. De igual forma querria dar gracias a Llum Ruiz Capdevila (docente de Vedruna Balaguer) quien ha ayudado a perfeccionar visualmente este programa."]
frases_anglès2=["Triangle 3 points", "Complete triangle", "Complete segment", "Absolute value", "Quadrilateral 4 points", "Complete quadrilateal", "Delete results", "Agreements", "Agreements", "I would like to thank both my tutors of this work: Vanessa Florenza Royes (docent at Vedruna Balaguer), Roberto Rubio Nuñez (cathedratic at UAB), in the Argò program, without which I would never have known this topic or Roberto, and finally my mother Mª Dolors Díaz Salud, all of them for supporting me during this journey.  The same way I would want to thank Llum Ruiz Capdevila (docent at Vedruna Balaguer) who has helped to perfect this program visualy."]
frases_alemà2=["Dreieck 3 Punkte", "Dreieck vervollständigen", "Segment vervollständigen", "Absolutwert", "Viereck 4 Punkte", "Viereck vervollständigen", "Ergebnisse löschen", "Vereinbarungen", "Vereinbarungen", "Ich möchte Ich danke meinen beiden Tutoren für diese Arbeit: Vanessa Florenza Royes (Dozentin bei Vedruna Balaguer), Roberto Rubio Nuñez (Kathedratisch bei UAB), das Argò-Programm, ohne die ich dieses Thema oder Roberto nie gekannt hätte, und schließlich meine Mutter Mª Dolors Díaz Salud, alle, die mich auf dieser Reise unterstützt haben. Genauso möchte ich mich bei Llum Ruiz Capdevila (Dozentin bei Vedruna Balaguer) bedanken, die dazu beigetragen hat, dieses Programm visuell zu perfektionieren."]

frases=frases_català1[:]
var1=StringVar()
var1.set(frases[0])
var2=StringVar()
var2.set(frases[1])
var3=StringVar()
var3.set(frases[2])
var4=StringVar()
var4.set(frases[3])
var5=StringVar()
var5.set(frases[4])
var6=StringVar()
var6.set(frases[5])
var7=StringVar()
var7.set(frases[6])
var8=StringVar()
var8.set(frases[7])
var9=StringVar()
var9.set(frases[8])
var10=StringVar()
var10.set(frases[9])
vari=IntVar()
vari.set(15)
varia=vari.get()

def change_dropdown(*args):
	thread = Thread(target=play_sound_botò)
	thread.start()
	idioma_elegit=idioma.get()
	funcions_elegides=funcions_h.get()
	if(idioma_elegit=="Català"):
		if(funcions_elegides=="Funcions 1"):
			frases=frases_català1[:]
			vari.set(15)
			varia=vari.get()
		else:
			frases=frases_català2[:]
			vari.set(15)
			varia=vari.get()
		root.title("Geometria Hiperbòlica")
		root2.title("Resultats")
		root3.title("Instruccions")
	elif(idioma_elegit=="Español"):
		if(funcions_elegides=="Funcions 1"):
			frases=frases_castellà1[:]
			vari.set(17)
			varia=vari.get()
		else:
			frases=frases_castellà2[:]
			vari.set(17)
			varia=vari.get()
		root.title("Geometría Hiperbólica")
		root2.title("Resultados")
		root3.title("Instrucciones")
	elif(idioma_elegit=="English"):
		if(funcions_elegides=="Funcions 1"):
			frases=frases_anglès1[:]
			vari.set(17)
			varia=vari.get()
		else:
			frases=frases_anglès2[:]
			vari.set(17)
			varia=vari.get()
		root.title("Hiperbolic Geometry")
		root2.title("Results")
		root3.title("Instrucions")
	elif(idioma_elegit=="Deutsch"):
		if(funcions_elegides=="Funcions 1"):
			frases=frases_alemà1[:]
			vari.set(20)
			varia=vari.get()
		else:
			frases=frases_alemà2[:]
			vari.set(20)
			varia=vari.get()
		root.title("Hyperbolische Geometrie")
		root2.title("Ergebnisse")
		root3.title("Anleitungen")
	var1.set(frases[0])
	var2.set(frases[1])
	var3.set(frases[2])
	var4.set(frases[3])
	var5.set(frases[4])
	var6.set(frases[5])
	var7.set(frases[6])
	var8.set(frases[7])
	var9.set(frases[8])
	var10.set(frases[9])
	botó_recta['width']=varia
	botó_raig['width']=varia
	botó_segment['width']=varia
	botó_cercle['width']=varia
	botó_cercle_2['width']=varia
	botó_arc['width']=varia
	botó_eliminar['width']=varia
	botó_info['width']=varia

idioma.trace("w", change_dropdown)

funcions_h.trace("w", change_dropdown)

def change_images(*args):
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		load_recta = Image.open("Imatges\\Recta.png")
		render_recta = ImageTk.PhotoImage(load_recta)
		img_recta = Label(myFrame, image=render_recta)
		img_recta.image = render_recta
		img_recta.grid(row=0, column=1)

		load_semirecta = Image.open("Imatges\\Semirecta.jpg")
		render_semirecta = ImageTk.PhotoImage(load_semirecta)
		img_semirecta = Label(myFrame, image=render_semirecta)
		img_semirecta.image = render_semirecta
		img_semirecta.grid(row=0, column=3)

		load_segment = Image.open("Imatges\\Segment.jpg")
		render_segment = ImageTk.PhotoImage(load_segment)
		img_segment = Label(myFrame, image=render_segment)
		img_segment.image = render_segment
		img_segment.grid(row=0, column=5)

		load_cercle = Image.open("Imatges\\Cercle.jpg")
		render_cercle = ImageTk.PhotoImage(load_cercle)
		img_cercle = Label(myFrame, image=render_cercle)
		img_cercle.image = render_cercle
		img_cercle.grid(row=1, column=1)

		load_cercle_2 = Image.open("Imatges\\Cercle_2.jpg")
		render_cercle_2 = ImageTk.PhotoImage(load_cercle_2)
		img_cercle_2 = Label(myFrame, image=render_cercle_2)
		img_cercle_2.image = render_cercle_2
		img_cercle_2.grid(row=1, column=3)

		load_arc = Image.open("Imatges\\Cercle_3.jpg")
		render_arc = ImageTk.PhotoImage(load_arc)
		img_arc = Label(myFrame, image=render_arc)
		img_arc.image = render_arc
		img_arc.grid(row=1, column=5)

		load_basura = Image.open("Imatges\\Eliminar.png")
		render_basura = ImageTk.PhotoImage(load_basura)
		img_basura = Label(myFrame, image=render_basura)
		img_basura.image = render_basura
		img_basura.grid(row=0, column=7)

		load_info = Image.open("Imatges\\Informació.png")
		render_info = ImageTk.PhotoImage(load_info)
		img_info = Label(myFrame, image=render_info)
		img_info.image = render_info
		img_info.grid(row=1, column=7)

		os.chdir("C:\\Users\\USUARIO\\Documents\\Hiperbolic Geometry\\Imatges")
		botó_info.config(cursor="@Question_Mark.cur")
		os.chdir("C:\\Users\\USUARIO\\Documents\\Hiperbolic Geometry")
	else:
		load_recta = Image.open("Imatges\\Triangle.jpg")
		render_recta = ImageTk.PhotoImage(load_recta)
		img_recta = Label(myFrame, image=render_recta)
		img_recta.image = render_recta
		img_recta.grid(row=0, column=1)

		load_semirecta = Image.open("Imatges\\Triangle_2.jpg")
		render_semirecta = ImageTk.PhotoImage(load_semirecta)
		img_semirecta = Label(myFrame, image=render_semirecta)
		img_semirecta.image = render_semirecta
		img_semirecta.grid(row=0, column=3)

		load_segment = Image.open("Imatges\\Segment_2.jpg")
		render_segment = ImageTk.PhotoImage(load_segment)
		img_segment = Label(myFrame, image=render_segment)
		img_segment.image = render_segment
		img_segment.grid(row=0, column=5)

		load_cercle = Image.open("Imatges\\Abs_x.jpg")
		render_cercle = ImageTk.PhotoImage(load_cercle)
		img_cercle = Label(myFrame, image=render_cercle)
		img_cercle.image = render_cercle
		img_cercle.grid(row=1, column=1)

		load_cercle_2 = Image.open("Imatges\\Quadrat.jpg")
		render_cercle_2 = ImageTk.PhotoImage(load_cercle_2)
		img_cercle_2 = Label(myFrame, image=render_cercle_2)
		img_cercle_2.image = render_cercle_2
		img_cercle_2.grid(row=1, column=3)

		load_arc = Image.open("Imatges\\Quadrat_2.jpg")
		render_arc = ImageTk.PhotoImage(load_arc)
		img_arc = Label(myFrame, image=render_arc)
		img_arc.image = render_arc
		img_arc.grid(row=1, column=5)

		load_basura = Image.open("Imatges\\Eliminar_2.jpg")
		render_basura = ImageTk.PhotoImage(load_basura)
		img_basura = Label(myFrame, image=render_basura)
		img_basura.image = render_basura
		img_basura.grid(row=0, column=7)

		load_info = Image.open("Imatges\\Gràcies.jpg")
		render_info = ImageTk.PhotoImage(load_info)
		img_info = Label(myFrame, image=render_info)
		img_info.image = render_info
		img_info.grid(row=1, column=7)

		os.chdir("C:\\Users\\USUARIO\\Documents\\Hiperbolic Geometry\\Imatges")
		botó_info.config(cursor="@Heart.cur")
		os.chdir("C:\\Users\\USUARIO\\Documents\\Hiperbolic Geometry")

funcions_h.trace("w", change_images)

root.counter=0

root.counter2=0

root.false=True

root.false2=True

#----Imatges dels botons----

load_recta = Image.open("Imatges\\Recta.png")
render_recta = ImageTk.PhotoImage(load_recta)
img_recta = Label(myFrame, image=render_recta)
img_recta.image = render_recta
img_recta.grid(row=0, column=1)

load_semirecta = Image.open("Imatges\\Semirecta.jpg")
render_semirecta = ImageTk.PhotoImage(load_semirecta)
img_semirecta = Label(myFrame, image=render_semirecta)
img_semirecta.image = render_semirecta
img_semirecta.grid(row=0, column=3)

load_segment = Image.open("Imatges\\Segment.jpg")
render_segment = ImageTk.PhotoImage(load_segment)
img_segment = Label(myFrame, image=render_segment)
img_segment.image = render_segment
img_segment.grid(row=0, column=5)

load_cercle = Image.open("Imatges\\Cercle.jpg")
render_cercle = ImageTk.PhotoImage(load_cercle)
img_cercle = Label(myFrame, image=render_cercle)
img_cercle.image = render_cercle
img_cercle.grid(row=1, column=1)

load_cercle_2 = Image.open("Imatges\\Cercle_2.jpg")
render_cercle_2 = ImageTk.PhotoImage(load_cercle_2)
img_cercle_2 = Label(myFrame, image=render_cercle_2)
img_cercle_2.image = render_cercle_2
img_cercle_2.grid(row=1, column=3)

load_arc = Image.open("Imatges\\Cercle_3.jpg")
render_arc = ImageTk.PhotoImage(load_arc)
img_arc = Label(myFrame, image=render_arc)
img_arc.image = render_arc
img_arc.grid(row=1, column=5)

load_basura = Image.open("Imatges\\Eliminar.png")
render_basura = ImageTk.PhotoImage(load_basura)
img_basura = Label(myFrame, image=render_basura)
img_basura.image = render_basura
img_basura.grid(row=0, column=7)

load_info = Image.open("Imatges\\Informació.png")
render_info = ImageTk.PhotoImage(load_info)
img_info = Label(myFrame, image=render_info)
img_info.image = render_info
img_info.grid(row=1, column=7)

#----Funcions----

def recta_h():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_recta=Label(root3, text="Per usar la recta feu clic als dos punts del disc desitjats i a continuació feu clic al botó de crear rectes.")
	elif(idioma_elegit=="Español"):
		info_recta=Label(root3, text="Para usar la recta haced clic a los dos puntos del disco deseados y a continuación haced clic al botón de crear rectas.")
	elif(idioma_elegit=="English"):
		info_recta=Label(root3, text="To use the line do click at the two desired points of the disk and then click the button to create lines.")
	elif(idioma_elegit=="Deutsch"):
		info_recta=Label(root3, text="Um die Linie zu verwenden, klicken Sie auf die beiden gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Linien zu erstellen.")
	info_recta.pack()
	if(root.false2==True):
		if(root.counter==2):
			u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
		elif(root.counter==3):
			u1,u2,v1,v2=root.v1,root.v2,root.w1,root.w2
		elif(root.counter==0):
			u1,u2,v1,v2=root.w1,root.w2,root.y1,root.y2
		elif(root.counter==1):
			u1,u2,v1,v2=root.y1,root.y2,root.u1,root.u2
	else:
		u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
	disc.create_circle(u1,u2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(v1,v2,5,outline='blue', fill='#00EEFF')
	if((u1-300)*(300-v2)-(300-u2)*(v1-300)!=0):
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		if((u1**2+u2**2!=90000) or (v1**2+v2**2!=90000)):
			if(u1**2+u2**2!=90000):
				w1=(u1*90000)/(u1**2+u2**2)
				w2=(u2*90000)/(u1**2+u2**2)
			elif(u1**2+u2**2==90000 and v1**2+v2**2!=90000):
				w1=(v1*90000)/(v1**2+v2**2)
				w2=(v2*90000)/(v1**2+v2**2)
			coeficients=numpy.array([[u1,u2,1],[v1,v2,1],[w1,w2,1]])
			resultats=numpy.array([-u1**2-u2**2,-v1**2-v2**2,-w1**2-w2**2])
			solucio=numpy.linalg.solve(coeficients,resultats)
			A=solucio[0]
			B=solucio[1]
			C=solucio[2]
			m=-A/2
			n=-B/2
			r_recta=math.sqrt(A**2+B**2-4*C)/2
		elif(u1**2+u2**2==90000 and v1**2+v2**2==90000):
			coeficients_2=numpy.array([[u1,u2],[v1,v2]])
			resultats_2=numpy.array([u1**2+u2**2,v1**2+v2**2])
			solucio_2=numpy.linalg.solve(coeficients_2,resultats_2)
			m=solucio_2[0]
			n=solucio_2[1]
			r_recta=math.sqrt((u1-m)**2+(u2-n)**2)
		disc.create_circle(m+300, -n+300, r_recta, fill="", outline="black")
	else:
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		vector_x=v1-u1
		vector_y=v2-u2
		x1=v1+1000000*vector_x
		y1=v2+1000000*vector_y
		disc.create_line(x1+300,300-y1,300-x1,300+y1)

def semirecta_h():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_semirecta=Label(root3, text='''Per usar la semiectarecta feu clic als dos punts del disc desitjats, sabent que la semirecta es dibuixara
 en sentit del primer al segon clic, i a continuació feu clic al botó de crear semirectes. ''')
	elif(idioma_elegit=="Español"):
		info_semirecta=Label(root3, text='''Para usar la semirecta haced clic a los dos puntos del disco deseados, sabiendo que la semirecta se dibujara
 en sentido del primer al segundo clic, y a continuación haced clic al botón de crear rectas. ''')
	elif(idioma_elegit=="English"):
		info_semirecta=Label(root3, text='''To use the ray do click at the two desired points of the disk, knowing that the ray will be created
 in the sense of the first to the second click, and then click the button to create rays. ''')
	elif(idioma_elegit=="Deutsch"):
		info_semirecta=Label(root3, text='''Um den Strahl zu verwenden, klicken Sie auf die beiden gewünschten Punkte auf der Scheibe, wobei Sie wissen,
 dass der Strahl im Sinne des ersten bis zweiten Klicks erstellt wird, und klicken Sie dann auf die Schaltfläche,
 um Strahlen zu erstellen. ''')
	info_semirecta.pack()
	if(root.false2==True):
		if(root.counter==2):
			u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
		elif(root.counter==3):
			u1,u2,v1,v2=root.v1,root.v2,root.w1,root.w2
		elif(root.counter==0):
			u1,u2,v1,v2=root.w1,root.w2,root.y1,root.y2
		elif(root.counter==1):
			u1,u2,v1,v2=root.y1,root.y2,root.u1,root.u2
	else:
		u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
	disc.create_circle(u1,u2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(v1,v2,5,outline='blue', fill='#00EEFF')
	if((u1-300)*(300-v2)-(300-u2)*(v1-300)!=0):
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		if((u1**2+u2**2!=90000) or (v1**2+v2**2!=90000)):
			if(u1**2+u2**2!=90000):
				w1=(u1*90000)/(u1**2+u2**2)
				w2=(u2*90000)/(u1**2+u2**2)
			elif(u1**2+u2**2==90000 and v1**2+v2**2!=90000):
				w1=(v1*90000)/(v1**2+v2**2)
				w2=(v2*90000)/(v1**2+v2**2)
			coeficients_semirecta=numpy.array([[u1,u2,1],[v1,v2,1],[w1,w2,1]])
			resultats_semirecta=numpy.array([-u1**2-u2**2,-v1**2-v2**2,-w1**2-w2**2])
			solucio_semirecta=numpy.linalg.solve(coeficients_semirecta,resultats_semirecta)
			D=solucio_semirecta[0]
			E=solucio_semirecta[1]
			F=solucio_semirecta[2]
			i=-D/2
			j=-E/2
			r_semirecta=math.sqrt(D**2+E**2-4*F)/2
		elif(u1**2+u2**2==90000 and v1**2+v2**2==90000):
			coeficients_semirecta_2=numpy.array([[u1,u2],[v1,v2]])
			resultats_semirecta_2=numpy.array([u1**2+u2**2,v1**2+v2**2])
			solucio_semirecta_2=numpy.linalg.solve(coeficients_semirecta_2,resultats_semirecta_2)
			i=solucio_semirecta_2[0]
			j=solucio_semirecta_2[1]
			r_semirecta=math.sqrt((u1-i)**2+(u2-j)**2)
		if(u1==0):
			alpha=math.pi/2
		elif(u1!=0):
			alpha=math.atan(math.fabs(u2/u1))
		if(v1==0):
			beta=math.pi/2
		elif(v1!=0):
			beta=math.atan(math.fabs(v2/v1))
		if(u1>=0 and u2>=0):
			alpha+=0
		elif(u1<=0 and u2>=0):
			alpha=math.pi-alpha
		elif(u1<=0 and u2<=0):
			alpha+=math.pi
		elif(u1>=0 and u2<=0):
			alpha=2*math.pi-alpha
		if(v1>=0 and v2>=0):
			beta+=0
		elif(v1<=0 and v2>=0):
			beta=math.pi-beta
		elif(v1<=0 and v2<=0):
			beta+=math.pi
		elif(v1>=0 and v2<=0):
			beta=2*math.pi-beta
		angle_inicial=math.atan(math.fabs((u2-j)/(u1-i)))
		if(u1-i>=0 and u2-j>=0):
			angle_inicial+=0
		elif(u1-i<=0 and u2-j>=0):
			angle_inicial=math.pi-angle_inicial
		elif(u1-i<=0 and u2-j<=0):
			angle_inicial+=math.pi
		elif(u1-i>=0 and u2-j<=0):
			angle_inicial=2*math.pi-angle_inicial
		if(u1-i==0):
			alpha_2=math.pi/2
		else:
			alpha_2=math.atan(math.fabs((u2-j)/(u1-i)))
		if(v1-i==0):
			beta_2=math.pi/2
		else:
			beta_2=math.atan(math.fabs((v2-j)/(v1-i)))
		if(v1-i>=0 and v2-j>=0):
			beta_2+=0
		elif(v1-i<=0 and v2-j>=0):
			beta_2=math.pi-beta_2
		elif(v1-i<=0 and v2-j<=0):
			beta_2+=math.pi
		elif(v1-i>=0 and v2-j<=0):
			beta_2=2*math.pi-beta_2
		if(u1-i>=0 and u2-j>=0):
			alpha_2+=0
		elif(u1-i<=0 and u2-j>=0):
			alpha_2=math.pi-alpha_2
		elif(u1-i<=0 and u2-j<=0):
			alpha_2+=math.pi
		elif(u1-i>=0 and u2-j<=0):
			alpha_2=2*math.pi-alpha_2
		if(((alpha_2>0 and alpha_2<math.pi/2) and (beta_2>0 and beta_2<math.pi/2)) or ((alpha_2>math.pi/2 and alpha_2<math.pi) and (beta_2>math.pi/2 and beta_2<math.pi)) or ((alpha_2>math.pi and alpha_2<3*math.pi/2) and (beta_2>math.pi and beta_2<3*math.pi/2)) or ((alpha_2>3*math.pi/2 and alpha_2<2*math.pi) and (beta_2>3*math.pi/2 and beta_2<2*math.pi))):
			if(alpha_2>beta_2):
				gamma=-180
			elif(alpha_2<beta_2):
				gamma=180
		elif(((alpha_2>0 and alpha_2<math.pi/2) and ((beta_2>math.pi/2 and beta_2<math.pi) or (beta_2>3*math.pi/2 and beta_2<2*math.pi))) or ((alpha_2>math.pi/2 and alpha_2<math.pi) and ((beta_2>math.pi and beta_2<3*math.pi/2) or (beta_2>0 and beta_2<math.pi/2))) or ((alpha_2>math.pi and alpha_2<3*math.pi/2) and ((beta_2>math.pi/2 and beta_2<math.pi) or (beta_2>3*math.pi/2 and beta_2<2*math.pi))) or ((alpha_2>3*math.pi/2 and alpha_2<2*math.pi) and ((beta_2>math.pi and beta_2<3*math.pi/2) or (beta_2>0 and beta_2<math.pi/2)))):
			if(((alpha_2>0 and alpha_2<math.pi/2) and ((beta_2>3*math.pi/2 and beta_2<2*math.pi))) or ((beta_2>0 and beta_2<math.pi/2) and ((alpha_2>3*math.pi/2 and alpha_2<2*math.pi)))):
				if(alpha_2>beta_2):
					gamma=180
				else:
					gamma=-180
			else:
				if(alpha_2>beta_2):
					gamma=-180
				else:
					gamma=180
		else:
			if(alpha_2>beta_2):
				gamma=180
			elif(alpha_2<beta_2):
				gamma=-180
		disc.create_arc(i+300-r_semirecta, -j+300-r_semirecta, i+300+r_semirecta, -j+300+r_semirecta, start=angle_inicial*180/math.pi, extent=gamma, fill="", outline="black", style="arc")
	else:
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		vector_x=v1-u1
		vector_y=v2-u2
		x1=v1+1000000*vector_x
		y1=v2+1000000*vector_y
		disc.create_line(x1+300,300-y1,u1+300,300-u2)
		
def segment_h():
	if(root.false==False):
		root.false=False
	else:
		for ele in root3.winfo_children():
				ele.destroy()
		idioma_elegit=idioma.get()
		if(idioma_elegit=="Català"):
			info_segment=Label(root3, text="Per usar el segment feu clic als dos punts del disc desitjats i a continuació feu clic al botó de crear segments.")
		elif(idioma_elegit=="Español"):
			info_segment=Label(root3, text="Para usar el segmento haced clic a los dos puntos del disco deseados y a continuación haced clic al botón de crear segmentos.")
		elif(idioma_elegit=="English"):
			info_segment=Label(root3, text="To use the segment do click at the two desired points of the disk and then click the button to create segments.")
		elif(idioma_elegit=="Deutsch"):
			info_segment=Label(root3, text="Um das Segment zu verwenden, klicken Sie auf die beiden gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Segmente zu erstellen.")
		info_segment.pack()
	if(root.false2==False):
		u1,u2,v1,v2=root2.u1,root2.u2,root2.v1,root2.v2
		del root2.u1,root2.u2,root2.v1,root2.v2
	else:
		if(root.counter==2):
			u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
		elif(root.counter==3):
			u1,u2,v1,v2=root.v1,root.v2,root.w1,root.w2
		elif(root.counter==0):
			u1,u2,v1,v2=root.w1,root.w2,root.y1,root.y2
		elif(root.counter==1):
			u1,u2,v1,v2=root.y1,root.y2,root.u1,root.u2
	disc.create_circle(u1,u2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(v1,v2,5,outline='blue', fill='#00EEFF')
	if((u1-300)*(300-v2)-(300-u2)*(v1-300)!=0):
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		if((u1**2+u2**2!=90000) or (v1**2+v2**2!=90000)):
			if(u1**2+u2**2!=90000):
				w1=(u1*90000)/(u1**2+u2**2)
				w2=(u2*90000)/(u1**2+u2**2)
			elif(u1**2+u2**2==90000 and v1**2+v2**2!=90000):
				w1=(v1*90000)/(v1**2+v2**2)
				w2=(v2*90000)/(v1**2+v2**2)
			coeficients_segment=numpy.array([[u1,u2,1],[v1,v2,1],[w1,w2,1]])
			resultats_segment=numpy.array([-u1**2-u2**2,-v1**2-v2**2,-w1**2-w2**2])
			solucio_segment=numpy.linalg.solve(coeficients_segment,resultats_segment)
			G=solucio_segment[0]
			H=solucio_segment[1]
			I=solucio_segment[2]
			k=-G/2
			l=-H/2
			r_segment=math.sqrt(G**2+H**2-4*I)/2
		elif(u1**2+u2**2==90000 and v1**2+v2**2==90000):
			coeficients_segment_2=numpy.array([[u1,u2],[v1,v2]])
			resultats_segment_2=numpy.array([u1**2+u2**2,v1**2+v2**2])
			solucio_segment_2=numpy.linalg.solve(coeficients_segment_2,resultats_segment_2)
			k=solucio_segment_2[0]
			l=solucio_segment_2[1]
			r_segment=math.sqrt((u1-k)**2+(u2-l)**2)
		if(u1==0):
			alpha=math.pi/2
		else:
			alpha=math.atan(math.fabs(u2/u1))
		if(v1==0):
			beta=math.pi/2
		else:
			beta=math.atan(math.fabs(v2/v1))
		if(u1>=0 and u2>=0):
			alpha+=0
		elif(u1<=0 and u2>=0):
			alpha=math.pi-alpha
		elif(u1<=0 and u2<=0):
			alpha+=math.pi
		elif(u1>=0 and u2<=0):
			alpha=2*math.pi-alpha
		if(v1>=0 and v2>=0):
			beta+=0
		elif(v1<=0 and v2>=0):
			beta=math.pi-beta
		elif(v1<=0 and v2<=0):
			beta+=math.pi
		elif(v1>=0 and v2<=0):
			beta=2*math.pi-beta
		if(u1-k==0):
			alpha_2=math.pi/2
		else:
			alpha_2=math.atan(math.fabs((u2-l)/(u1-k)))
		if(v1-k==0):
			beta_2=math.pi/2
		else:
			beta_2=math.atan(math.fabs((v2-l)/(v1-k)))
		if(v1-k>=0 and v2-l>=0):
			beta_2+=0
		elif(v1-k<=0 and v2-l>=0):
			beta_2=math.pi-beta_2
		elif(v1-k<=0 and v2-l<=0):
			beta_2+=math.pi
		elif(v1-k>=0 and v2-l<=0):
			beta_2=2*math.pi-beta_2
		if(u1-k>=0 and u2-l>=0):
			alpha_2+=0
		elif(u1-k<=0 and u2-l>=0):
			alpha_2=math.pi-alpha_2
		elif(u1-k<=0 and u2-l<=0):
			alpha_2+=math.pi
		elif(u1-k>=0 and u2-l<=0):
			alpha_2=2*math.pi-alpha_2
		if(alpha<beta):
			angle_inicial=math.atan(math.fabs((u2-l)/(u1-k)))
			if(u1-k>=0 and u2-l>=0):
				angle_inicial+=0
			elif(u1-k<=0 and u2-l>=0):
				angle_inicial=math.pi-angle_inicial
			elif(u1-k<=0 and u2-l<=0):
				angle_inicial+=math.pi
			elif(u1-k>=0 and u2-l<=0):
				angle_inicial=2*math.pi-angle_inicial
			gamma=beta_2-alpha_2
		elif(beta<alpha):
			angle_inicial=math.atan(math.fabs((v2-l)/(v1-k)))
			if(v1-k>=0 and v2-l>=0):
				angle_inicial+=0
			elif(v1-k<=0 and v2-l>=0):
				angle_inicial=math.pi-angle_inicial
			elif(v1-k<=0 and v2-l<=0):
				angle_inicial+=math.pi
			elif(v1-k>=0 and v2-l<=0):
				angle_inicial=2*math.pi-angle_inicial
			gamma=alpha_2-beta_2
		if(gamma>=math.pi):
			angle_inicial+=gamma
			gamma=2*math.pi-gamma
		disc.create_arc(k+300-r_segment, -l+300-r_segment, k+300+r_segment, -l+300+r_segment, start=angle_inicial*180/math.pi, extent=gamma*180/math.pi, fill="", outline="black", style="arc")

	else:
		disc.create_line(u1,u2,v1,v2)

def cercle_h():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_cercle=Label(root3, text='''Per usar el cercle feu clic als dos punts del disc desitjats, el primer sera el centre
 i el segon un punt de la circumferencia, i a continuació feu clic al botó de crear cercles.''')
	elif(idioma_elegit=="Español"):
		info_cercle=Label(root3, text='''Para usar el circulo haced clic a los dos puntos del disco deseados, el primero sera el centro
 y el segundo un punto de la circumferencia, y a continuación haced clic al botón de crear circulos.''')
	elif(idioma_elegit=="English"):
		info_cercle=Label(root3, text='''To use the circle do click at the two desired points of the disk, the first will be the center
 and the second a point of the circle, and then click the button to create circles.''')
	elif(idioma_elegit=="Deutsch"):
		info_cercle=Label(root3, text='''Um den Kreis zu verwenden, klicken Sie auf die beiden gewünschten Punkte der Scheibe. Der erste ist die Mitte
 vund der zweite ein Punkt des Kreises, und klicken Sie dann auf die Schaltfläche, um Kreisen zu erstellen.''')
	info_cercle.pack()
	if(root.counter==2):
		u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
	elif(root.counter==3):
		u1,u2,v1,v2=root.v1,root.v2,root.w1,root.w2
	elif(root.counter==0):
		u1,u2,v1,v2=root.w1,root.w2,root.y1,root.y2
	elif(root.counter==1):
		u1,u2,v1,v2=root.y1,root.y2,root.u1,root.u2
	disc.create_circle(u1,u2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(v1,v2,5,outline='blue', fill='#00EEFF')
	u1-=300
	u2=300-u2
	v1-=300
	v2=300-v2
	if(v1**2+v2**2==90000):
		disc.create_circle(300, 300, 300, outline="blue")
	else:
		p1,p2=0,300
		if((p1-300)*(300-u2)-(300-p2)*(u1-300)!=0):
			if((p1**2+p2**2!=90000) or (u1**2+u2**2!=90000)):
				if(p1**2+p2**2!=90000):
					w1=(p1*90000)/(p1**2+p2**2)
					w2=(p2*90000)/(p1**2+p2**2)
				elif(p1**2+p2**2==90000 and u1**2+u2**2!=90000):
					w1=(u1*90000)/(u1**2+u2**2)
					w2=(u2*90000)/(u1**2+u2**2)
				coeficients=numpy.array([[p1,p2,1],[u1,u2,1],[w1,w2,1]])
				resultats=numpy.array([-p1**2-p2**2,-u1**2-u2**2,-w1**2-w2**2])
				solucio=numpy.linalg.solve(coeficients,resultats)
				A=solucio[0]
				B=solucio[1]
				C=solucio[2]
				m=-A/2
				n=-B/2
				r_recta=math.sqrt(A**2+B**2-4*C)/2
			elif(p1**2+p2**2==90000 and v1**2+v2**2==90000):
					coeficients_2=numpy.array([[p1,p2],[u1,u2]])
					resultats_2=numpy.array([p1**2+p2**2,u1**2+u2**2])
					solucio_2=numpy.linalg.solve(coeficients_2,resultats_2)
					m=solucio_2[0]
					n=solucio_2[1]
					r_recta=math.sqrt((p1-m)**2+(p2-n)**2)
		x1=v1-m
		y1=v2-n
		w5=(x1*r_recta**2)/(x1**2+y1**2)+m
		w6=(y1*r_recta**2)/(x1**2+y1**2)+n
		p1,p2=600,300
		if((p1-300)*(300-u2)-(300-p2)*(u1-300)!=0):
			if((p1**2+p2**2!=90000) or (u1**2+u2**2!=90000)):
				if(p1**2+p2**2!=90000):
					w1=(p1*90000)/(p1**2+p2**2)
					w2=(p2*90000)/(p1**2+p2**2)
				elif(p1**2+p2**2==90000 and u1**2+u2**2!=90000):
					w1=(u1*90000)/(u1**2+u2**2)
					w2=(u2*90000)/(u1**2+u2**2)
				coeficients=numpy.array([[p1,p2,1],[u1,u2,1],[w1,w2,1]])
				resultats=numpy.array([-p1**2-p2**2,-u1**2-u2**2,-w1**2-w2**2])
				solucio=numpy.linalg.solve(coeficients,resultats)
				A=solucio[0]
				B=solucio[1]
				C=solucio[2]
				m=-A/2
				n=-B/2
				r_recta=math.sqrt(A**2+B**2-4*C)/2
			elif(p1**2+p2**2==90000 and v1**2+v2**2==90000):
					coeficients_2=numpy.array([[p1,p2],[u1,u2]])
					resultats_2=numpy.array([p1**2+p2**2,u1**2+u2**2])
					solucio_2=numpy.linalg.solve(coeficients_2,resultats_2)
					m=solucio_2[0]
					n=solucio_2[1]
					r_recta=math.sqrt((p1-m)**2+(p2-n)**2)
		x2=v1-m
		y2=v2-n
		w3=(x2*r_recta**2)/(x2**2+y2**2)+m
		w4=(y2*r_recta**2)/(x2**2+y2**2)+n
		coeficients_cercle=numpy.array([[v1,v2,1],[w3,w4,1],[w5,w6,1]])
		resultats_cercle=numpy.array([-v1**2-v2**2,-w3**2-w4**2,-w5**2-w6**2])
		solucio_cercle=numpy.linalg.solve(coeficients_cercle,resultats_cercle)
		O=solucio_cercle[0]
		P=solucio_cercle[1]
		Q=solucio_cercle[2]
		s=-O/2
		t=-P/2
		r_cercle=math.sqrt(O**2+P**2-4*Q)/2
		if(v1**2+v2**2>90000):
			disc.create_circle(s+300,300-t,r_cercle,outline="red")
		elif(u1==0 and u2==0):
			s,t=u1,u2
			r_cercle=math.sqrt(v1**2+v2**2)
			disc.create_circle(s+300,300-t,r_cercle, outline="blue")
		else:
			disc.create_circle(s+300,300-t,r_cercle,outline="blue")

def cercle_2_h():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_cercle_2=Label(root3, text='''Per usar el cercle feu clic als tres punts del disc desitjats per on passara el cercle
 i a continuació feu clic al botó de crear cercles amb 3 punts.''')
	elif(idioma_elegit=="Español"):
		info_cercle_2=Label(root3, text='''Para usar el circulo haced clic a los tres puntos del disco deseados por donde passara el circulo
 y a continuación haced clic al botón de crear circulos con 3 puntos.''')
	elif(idioma_elegit=="English"):
		info_cercle_2=Label(root3, text='''To use the circle do click at the three desired points of the disk through which the circle will pass
 and then click the button to create circles with 3 points.''')
	elif(idioma_elegit=="Deutsch"):
		info_cercle_2=Label(root3, text='''Um den Kreis zu verwenden, klicken Sie auf die drei gewünschten Punkte der Scheibe, durch die der Kreis wird durch sie gehen
 Klicken Sie dann auf die Schaltfläche, um Kreise mit 3 Punkten zu erstellen.''')
	info_cercle_2.pack()
	if(root.counter==3 or root.counter==7 or root.counter==11):
		u1,u2,v1,v2,w1,w2=root.u1,root.u2,root.v1,root.v2,root.w1,root.w2
	elif(root.counter==4 or root.counter==8 or root.counter==0):
		u1,u2,v1,v2,w1,w2=root.v1,root.v2,root.w1,root.w2,root.y1,root.y2
	elif(root.counter==5 or root.counter==9 or root.counter==1):
		u1,u2,v1,v2,w1,w2=root.w1,root.w2,root.y1,root.y2,root.u1,root.u2
	elif(root.counter==6 or root.counter==10 or root.counter==2):
		u1,u2,v1,v2,w1,w2=root.y1,root.y2,root.u1,root.u2,root.v1,root.v2
	disc.create_circle(u1,u2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(v1,v2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(w1,w2,5,outline='blue', fill='#00EEFF')
	if((w1-v1==0 and u1==v1) or (w2-v2==0 and u2==v2)):
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		vector_x=v1-u1
		vector_y=v2-u2
		x1=v1+1000000*vector_x
		y1=v2+1000000*vector_y
		disc.create_line(x1+300,300-y1,300-x1,300+y1,fill="red")
	elif((v1-u1)/(w1-v1)==(v2-u2)/(w2-v2)):
		vector_x=v1-u1
		vector_y=v2-u2
		x1=v1+1000000*vector_x
		y1=v2+1000000*vector_y
		disc.create_line(x1,y1,-x1,-y1,fill="red")
	else:
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		w1-=300
		w2=300-w2
		coeficients=numpy.array([[u1,u2,1],[v1,v2,1],[w1,w2,1]])
		resultats=numpy.array([-u1**2-u2**2,-v1**2-v2**2,-w1**2-w2**2])
		solucio=numpy.linalg.solve(coeficients,resultats)
		A=solucio[0]
		B=solucio[1]
		C=solucio[2]
		l=-A/2
		k=-B/2
		r_cercle=math.sqrt(A**2+B**2-4*C)/2
		if(math.sqrt(l**2+k**2)+r_cercle>300):
			disc.create_circle(l+300,300-k,r_cercle,outline="red")
		else:
			disc.create_circle(l+300,300-k,r_cercle,outline="blue")

def triangle_h():
	for ele in root3.winfo_children():
			ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_segment=Label(root3, text="Per usar el triangle feu clic als tres punts del disc desitjats i a continuació feu clic al botó de crear triangles.")
	elif(idioma_elegit=="Español"):
		info_segment=Label(root3, text="Para usar el triangulo haced clic a los tres puntos del disco deseados y a continuación haced clic al botón de crear triangulos.")
	elif(idioma_elegit=="English"):
		info_segment=Label(root3, text="To use the triangle do click at the three desired points of the disk and then click the button to create triangles.")
	elif(idioma_elegit=="Deutsch"):
		info_segment=Label(root3, text="Um das Dreieck zu verwenden, klicken Sie auf die drei gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Dreiecke zu erstellen.")
	info_segment.pack()
	root.false=False
	root.false2=False
	if(root.counter==3):
		root2.u1,root2.u2,root2.v1,root2.v2=root.u1,root.u2,root.v1,root.v2
	elif(root.counter==0):
		root2.u1,root2.u2,root2.v1,root2.v2=root.v1,root.v2,root.w1,root.w2
	elif(root.counter==1):
		root2.u1,root2.u2,root2.v1,root2.v2=root.w1,root.w2,root.y1,root.y2
	elif(root.counter==2):
		root2.u1,root2.u2,root2.v1,root2.v2=root.y1,root.y2,root.u1,root.u2
	segment_h()
	if(root.counter==3):
		root2.u1,root2.u2,root2.v1,root2.v2=root.v1,root.v2,root.w1,root.w2
	elif(root.counter==0):
		root2.u1,root2.u2,root2.v1,root2.v2=root.w1,root.w2,root.y1,root.y2
	elif(root.counter==1):
		root2.u1,root2.u2,root2.v1,root2.v2=root.y1,root.y2,root.u1,root.u2
	elif(root.counter==2):
		root2.u1,root2.u2,root2.v1,root2.v2=root.u1,root.u2,root.v1,root.v2
	segment_h()
	if(root.counter==3):
		root2.u1,root2.u2,root2.v1,root2.v2=root.w1,root.w2,root.u1,root.u2
	elif(root.counter==0):
		root2.u1,root2.u2,root2.v1,root2.v2=root.y1,root.y2,root.v1,root.v2
	elif(root.counter==1):
		root2.u1,root2.u2,root2.v1,root2.v2=root.u1,root.u2,root.w1,root.w2
	elif(root.counter==2):
		root2.u1,root2.u2,root2.v1,root2.v2=root.v1,root.v2,root.y1,root.y2
	segment_h()
	root.false=True
	root.false2=True

def distancia_h(print_d,cercle):
	u1,u2,v1,v2=root2.u1,root2.u2,root2.v1,root2.v2
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		escrit1="El radi és: "
		escrit2="La distancia hiperbòlica és: "
	elif(idioma_elegit=="Español"):
		escrit1="El radio es: "
		escrit2="La distancía hiperbólica es: "
	elif(idioma_elegit=="English"):
		escrit1="The radius is: "
		escrit2="The hiperbolic distance is: "
	elif(idioma_elegit=="Deutsch"):
		escrit1="Der Radius ist: "
		escrit2="Der hyperbolische Abstand beträgt: "
	u1=(u1-300)/300
	u2=(300-u2)/300
	v1=(v1-300)/300
	v2=(300-v2)/300
	if(u1**2+u2**2<1 and v1**2+v2**2<1):
		distancia_hiperbolica=math.log((math.sqrt((-u1*v2+u2*v1)**2+(1-u1*v1-u2*v2)**2)+math.sqrt((v1-u1)**2+(v2-u2)**2))/(math.sqrt((-u1*v2+u2*v1)**2+(1-u1*v1-u2*v2)**2)-math.sqrt((v1-u1)**2+(v2-u2)**2)))
		if(cercle==True):
			distancia=(escrit1+str(distancia_hiperbolica))
		else:
			distancia=(escrit2+str(distancia_hiperbolica))
	else:
		distancia_hiperbolica=math.inf
		if(cercle==True):
			distancia=(escrit1+"∞")
		else:
			distancia=(escrit2+"∞")
	if(print_d==True):
		label_distancia=Label(root2,text=distancia, width=50)
		label_distancia.pack(expand=1)
	return distancia_hiperbolica

def area_h(print_d):
	root2.u1,root2.u2,root2.v1,root2.v2=root3.u1,root3.u2,root3.v1,root3.v2
	a=distancia_h(print_d,False)
	root2.u1,root2.u2,root2.v1,root2.v2=root3.w1,root3.w2,root3.v1,root3.v2
	b=distancia_h(print_d,False)
	root2.u1,root2.u2,root2.v1,root2.v2=root3.w1,root3.w2,root3.u1,root3.u2
	c=distancia_h(print_d,False)
	u1,u2,v1,v2,w1,w2=root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2
	del root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2
	if((w1-300)**2+(w2-300)**2==90000):
		A=0
	else:
		cos_A=(math.cosh(b)*math.cosh(c)-math.cosh(a))/(math.sinh(b)*math.sinh(c))
		A=math.acos(cos_A)
	if((u1-300)**2+(u2-300)**2==90000):
		B=0
	else:
		sin_B=(math.sin(A)/math.sinh(a))*math.sinh(b)
		B=math.asin(sin_B)
	if((v1-300)**2+(v2-300)**2==90000):
		C=0
	else:
		sin_C=(math.sin(B)/math.sinh(b))*math.sinh(c)
		C=math.asin(sin_C)
	if(numpy.isnan(A)==True):
		u1_nou=u1
		u2_nou=u2
		v1_nou=v1
		v2_nou=v2
		if((u1-300)**2+(300-u2)**2==90000):
			if(u2<300):
				u2_nou=u2+0.00001
			elif(u2>300):
				u2_nou=u2-0.00001
			else:
				if(u1<300):
					u1_nou=u1+0.00001
				elif(u1>300):
					u1_nou=u1-0.00001
		if((v1-300)**2+(300-v2)**2==90000):
			if(v2<300):
				v2_nou=v2+0.00001
			elif(v2>300):
				v2_nou=v2-0.00001
			else:
				if(v1<300):
					v1_nou=v1+0.00001
				elif(v1>300):
					v1_nou=v1-0.00001
		a=distancia_h(u1_nou,u2_nou,v1_nou,v2_nou,False,False)
		b=distancia_h(w1,w2,v1_nou,v2_nou,False,False)
		c=distancia_h(u1_nou,u2_nou,w1,w2,False,False)
		cos_A=(math.cosh(b)*math.cosh(c)-math.cosh(a))/(math.sinh(b)*math.sinh(c))
		A=math.acos(cos_A)
	if(numpy.isnan(B)==True):
		w1_nou=w1
		w2_nou=w2
		v1_nou=v1
		v2_nou=v2
		if((w1-300)**2+(300-w2)**2==90000):
			if(w2<300):
				w2_nou=w2+0.00001
			elif(w2>300):
				w2_nou=w2-0.00001
			else:
				if(w1<300):
					w1_nou=w1+0.00001
				elif(w1>300):
					w1_nou=w1-0.00001
		if((v1-300)**2+(300-v2)**2==90000):
			if(v2<300):
				v2_nou=v2+0.00001
			elif(v2>300):
				v2_nou=v2-0.00001
			else:
				if(v1<300):
					v1_nou=v1+0.00001
				elif(v1>300):
					v1_nou=v1-0.00001
		a=distancia_h(u1_nou,u2_nou,v1_nou,v2_nou,False,False)
		b=distancia_h(w1,w2,v1_nou,v2_nou,False,False)
		c=distancia_h(u1_nou,u2_nou,w1,w2,False,False)
		cos_B=(math.cosh(c)*math.cosh(a)-math.cosh(b))/(math.sinh(c)*math.sinh(a))
		B=math.acos(cos_B)
	if(numpy.isnan(C)==True):
		w1_nou=w1
		w2_nou=w2
		u1_nou=u1
		u2_nou=u2
		if((w1-300)**2+(300-w2)**2==90000):
			if(w2<300):
				w2_nou=w2+0.00001
			elif(w2>300):
				w2_nou=w2-0.00001
			else:
				if(w1<300):
					w1_nou=w1+0.00001
				elif(w1>300):
					w1_nou=w1-0.00001
		if((u1-300)**2+(300-u2)**2==90000):
			if(u2<300):
				u2_nou=u2+0.00001
			elif(u2>300):
				u2_nou=u2-0.00001
			else:
				if(u1<300):
					u1_nou=u1+0.00001
				elif(u1>300):
					u1_nou=u1-0.00001
		a=distancia_h(u1_nou,u2_nou,v1_nou,v2_nou,False,False)
		b=distancia_h(w1,w2,v1_nou,v2_nou,False,False)
		c=distancia_h(u1_nou,u2_nou,w1,w2,False,False)
		cos_C=(math.cosh(a)*math.cosh(b)-math.cosh(c))/(math.sinh(a)*math.sinh(b))
		C=math.acos(cos_C)
	area=math.pi-(A+B+C)
	if(print_d==True):
		if(area==math.pi):
			area="π"
		else:
			area=str(area)
		idioma_elegit=idioma.get()
		if(idioma_elegit=="Català"):
			text_a="L'angule A és: "+str(A*180/math.pi)
			text_b="L'angule B és: "+str(B*180/math.pi)
			text_c="L'angule C és: "+str(C*180/math.pi)
			text_d="L'àrea és: "+area
		elif(idioma_elegit=="Español"):
			text_a="El angulo A es: "+str(A*180/math.pi)
			text_b="El angulo B es: "+str(B*180/math.pi)
			text_c="El angulo C es: "+str(C*180/math.pi)
			text_d="El area es: "+area
		elif(idioma_elegit=="English"):
			text_a="The angle A is: "+str(A*180/math.pi)
			text_b="The angle B is: "+str(B*180/math.pi)
			text_c="The angle C is: "+str(C*180/math.pi)
			text_d="The area is: "+area
		elif(idioma_elegit=="Deutsch"):
			text_a="Der Winkel A ist: "+str(A*180/math.pi)
			text_b="Der Winkel B ist: "+str(B*180/math.pi)
			text_c="Der Winkel C ist: "+str(C*180/math.pi)
			text_d="Das Gebiet ist: "+area
		label_angle_a=Label(root2, text=text_a, width=50)
		label_angle_b=Label(root2, text=text_b, width=50)
		label_angle_c=Label(root2, text=text_c, width=50)
		label_area=Label(root2, text=text_d, width=50)
		label_angle_a.pack(expand=1)
		label_angle_b.pack(expand=1)
		label_angle_c.pack(expand=1)
		label_area.pack(expand=1)
	else:
		root.area,root.a,root.b,root.c=area,A,B,C

def triangle_h_full():
	for ele in root3.winfo_children():
			ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_segment=Label(root3, text="Per usar el triangle feu clic als tres punts del disc desitjats i a continuació feu clic al botó de crear triangles.")
	elif(idioma_elegit=="Español"):
		info_segment=Label(root3, text="Para usar el triangulo haced clic a los tres puntos del disco deseados y a continuación haced clic al botón de crear triangulos.")
	elif(idioma_elegit=="English"):
		info_segment=Label(root3, text="To use the triangle do click at the three desired points of the disk and then click the button to create triangles.")
	elif(idioma_elegit=="Deutsch"):
		info_segment=Label(root3, text="Um das Dreieck zu verwenden, klicken Sie auf die drei gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Dreiecke zu erstellen.")
	info_segment.pack()
	triangle_h()
	if(root.counter==3 or root.counter==7 or root.counter==11):
		root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2=root.u1,root.u2,root.v1,root.v2,root.w1,root.w2
	elif(root.counter==4 or root.counter==8 or root.counter==0):
		root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2=root.v1,root.v2,root.w1,root.w2,root.y1,root.y2
	elif(root.counter==5 or root.counter==9 or root.counter==1):
		root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2=root.w1,root.w2,root.y1,root.y2,root.u1,root.u2
	elif(root.counter==6 or root.counter==10 or root.counter==2):
		root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2=root.y1,root.y2,root.u1,root.u2,root.v1,root.v2
	area_h(True)

def segment_h_full():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_segment=Label(root3, text="Per usar el segment feu clic als dos punts del disc desitjats i a continuació feu clic al botó de crear segments.")
	elif(idioma_elegit=="Español"):
		info_segment=Label(root3, text="Para usar el segmento haced clic a los dos puntos del disco deseados y a continuación haced clic al botón de crear segmentos.")
	elif(idioma_elegit=="English"):
		info_segment=Label(root3, text="To use the segment do click at the two desired points of the disk and then click the button to create segments.")
	elif(idioma_elegit=="Deutsch"):
			info_segment=Label(root3, text="Um das Segment zu verwenden, klicken Sie auf die beiden gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Segmente zu erstellen.")
	info_segment.pack()
	if(root.false2==True):
		if(root.counter==2):
			root2.u1,root2.u2,root2.v1,root2.v2=root.u1,root.u2,root.v1,root.v2
		elif(root.counter==3):
			root2.u1,root2.u2,root2.v1,root2.v2=root.v1,root.v2,root.w1,root.w2
		elif(root.counter==0):
			root2.u1,root2.u2,root2.v1,root2.v2=root.w1,root.w2,root.y1,root.y2
		elif(root.counter==1):
			root2.u1,root2.u2,root2.v1,root2.v2=root.y1,root.y2,root.u1,root.u2
	else:
		root2.u1,root2.u2,root2.v1,root2.v2=root2.u1,root2.u2,root2.v1,root2.v2
	distancia_h(True,False)
	segment_h()

def perimetre_cercle():
	perimetre=2*math.pi*math.sinh(distancia_h(False,True))
	idioma_elegit=idioma.get()
	if(perimetre==math.inf):
		perimetre="∞"
	if(idioma_elegit=="Català"):
		text_peri="El perimetre és: "+str(perimetre)
	elif(idioma_elegit=="Español"):
		text_peri="El perimetro es: "+str(perimetre)
	elif(idioma_elegit=="English"):
		text_peri="The circumference is: "+str(perimetre)
	elif(idioma_elegit=="Deutsch"):
		text_peri="Der Umfang ist: "+str(perimetre)
	label_peri=Label(root2, text=text_peri, width=50)
	label_peri.pack(expand=1)

def area_cercle():
	area=2*math.pi*(math.cosh(distancia_h(False,True))-1)
	idioma_elegit=idioma.get()
	if(area==math.inf):
		area="∞"
	if(idioma_elegit=="Català"):
		text_a_c="L'àrea és: "+str(area)
	elif(idioma_elegit=="Español"):
		text_a_c="El area es: "+str(area)
	elif(idioma_elegit=="English"):
 		text_a_c="The area is: "+str(area)
	elif(idioma_elegit=="Deutsch"):
 		text_a_c="Das Gebiet ist: "+str(area)
	label_a_c=Label(root2, text=text_a_c, width=50)
	label_a_c.pack(expand=1)

def cercle_h_full():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_cercle=Label(root3, text='''Per usar el cercle feu clic als dos punts del disc desitjats, el primer sera el centre
 i el segon un punt de la circumferencia, i a continuació feu clic al botó de crear cercles.''')
	elif(idioma_elegit=="Español"):
		info_cercle=Label(root3, text='''Para usar el circulo haced clic a los dos puntos del disco deseados, el primero sera el centro
 y el segundo un punto de la circumferencia, y a continuación haced clic al botón de crear circulos.''')
	elif(idioma_elegit=="English"):
		info_cercle=Label(root3, text='''To use the circle do click at the two desired points of the disk, the first will be the center
 and the second a point of the circle, and then click the button to create segments.''')
	elif(idioma_elegit=="Deutsch"):
		info_cercle=Label(root3, text='''Um den Kreis zu verwenden, klicken Sie auf die beiden gewünschten Punkte der Scheibe. Der erste ist die Mitte
 vund der zweite ein Punkt des Kreises, und klicken Sie dann auf die Schaltfläche, um Kreisen zu erstellen.''')
	info_cercle.pack()
	if(root.counter==2):
		root2.u12,root2.u22,root2.v12,root2.v22=root.u1,root.u2,root.v1,root.v2
	elif(root.counter==3):
		root2.u12,root2.u22,root2.v12,root2.v22=root.v1,root.v2,root.w1,root.w2
	elif(root.counter==0):
		root2.u12,root2.u22,root2.v12,root2.v22=root.w1,root.w2,root.y1,root.y2
	elif(root.counter==1):
		root2.u12,root2.u22,root2.v12,root2.v22=root.y1,root.y2,root.u1,root.u2
	cercle_h()
	root2.u1,root2.u2,root2.v1,root2.v2=root2.u12,root2.u22,root2.v12,root2.v22
	distancia_h(True,True)
	root2.u1,root2.u2,root2.v1,root2.v2=root2.u12,root2.u22,root2.v12,root2.v22
	perimetre_cercle()
	root2.u1,root2.u2,root2.v1,root2.v2=root2.u12,root2.u22,root2.v12,root2.v22
	area_cercle()

def eliminar():
	disc.delete("all")
	disc.create_circle(300, 300, 300, fill="white", outline="")

def info():
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		messagebox.showinfo(frases_català1[8], frases_català1[9])
	elif(idioma_elegit=="Español"):
		messagebox.showinfo(frases_castellà1[8], frases_castellà1[9])
	elif(idioma_elegit=="English"):
		messagebox.showinfo(frases_anglès1[8], frases_anglès1[9])
	elif(idioma_elegit=="Deutsch"):
		messagebox.showinfo(frases_alemà1[8], frases_alemà1[9])

def agrair():
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		messagebox.showinfo(frases_català2[8], frases_català2[9])
	elif(idioma_elegit=="Español"):
		messagebox.showinfo(frases_castellà2[8], frases_castellà2[9])
	elif(idioma_elegit=="English"):
		messagebox.showinfo(frases_anglès2[8], frases_anglès2[9])
	elif(idioma_elegit=="Deutsch"):
		messagebox.showinfo(frases_alemà2[8], frases_alemà2[9])

def eliminar_resultats():
	for ele in root2.winfo_children():
  		ele.destroy()

def abs_x():
	root.false2=False
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_recta=Label(root3, text='''Per usar la recta en valor absolut feu clic als dos punts del disc desitjats
 i a continuació feu clic al botó de crear rectes en valor absolut.''')
	elif(idioma_elegit=="Español"):
		info_recta=Label(root3, text='''Para usar la recta en valor absoluto haced clic a los dos puntos del disco deseados
 y a continuación haced clic al botón de crear rectas en valor absoluto.''')
	elif(idioma_elegit=="English"):
		info_recta=Label(root3, text='''To use the line in absolute value do click at the two desired points of the disk
 and then click the button to create lines in absolute value.''')
	elif(idioma_elegit=="Deutsch"):
		info_recta=Label(root3, text='''Um die Linie in absoluten Wert zu verwenden, klicken Sie auf die beiden gewünschten Punkte der Scheibe
 Klicken Sie dann auf die Schaltfläche, um Linien in absoluten Werten zu erstellen.''')
	info_recta.pack()
	if(root.counter==2):
		u1,u2,v1,v2=root.u1,root.u2,root.v1,root.v2
	elif(root.counter==3):
		u1,u2,v1,v2=root.v1,root.v2,root.w1,root.w2
	elif(root.counter==0):
		u1,u2,v1,v2=root.w1,root.w2,root.y1,root.y2
	elif(root.counter==1):
		u1,u2,v1,v2=root.y1,root.y2,root.u1,root.u2
	disc.create_circle(u1,u2,5,outline='blue', fill='#00EEFF')
	disc.create_circle(v1,v2,5,outline='blue', fill='#00EEFF')
	if((u1-300)*(300-v2)-(300-u2)*(v1-300)!=0):
		u1-=300
		u2=300-u2
		v1-=300
		v2=300-v2
		if((u1**2+u2**2!=90000) or (v1**2+v2**2!=90000)):
			if(u1**2+u2**2!=90000):
				w1=(u1*90000)/(u1**2+u2**2)
				w2=(u2*90000)/(u1**2+u2**2)
			elif(u1**2+u2**2==90000 and v1**2+v2**2!=90000):
				w1=(v1*90000)/(v1**2+v2**2)
				w2=(v2*90000)/(v1**2+v2**2)
			coeficients=numpy.array([[u1,u2,1],[v1,v2,1],[w1,w2,1]])
			resultats=numpy.array([-u1**2-u2**2,-v1**2-v2**2,-w1**2-w2**2])
			solucio=numpy.linalg.solve(coeficients,resultats)
			A=solucio[0]
			B=solucio[1]
			C=solucio[2]
			m=-A/2
			n=-B/2
			r_recta=math.sqrt(A**2+B**2-4*C)/2
		elif(u1**2+u2**2==90000 and v1**2+v2**2==90000):
			coeficients_2=numpy.array([[u1,u2],[v1,v2]])
			resultats_2=numpy.array([u1**2+u2**2,v1**2+v2**2])
			solucio_2=numpy.linalg.solve(coeficients_2,resultats_2)
			m=solucio_2[0]
			n=solucio_2[1]
			r_recta=math.sqrt((u1-m)**2+(u2-n)**2)
		if(r_recta**2-n**2<0):
			if(u2<0):
				root.u1,root.u2,root.v1,root.v2=u1+300,300+u2,v1+300,300+v2
				recta_h()
			else:
				root.u1,root.u2,root.v1,root.v2=u1+300,300-u2,v1+300,300-v2
				recta_h()
		else:
			tall_x=math.sqrt(r_recta**2-n**2)-m
			if(tall_x>300 or tall_x<-300):
				tall_x=-math.sqrt(r_recta**2-n**2)-m
			if(u2>0 and v2<0):
				root.u1,root.u2,root.v1,root.v2=300-tall_x,300,u1+300,300-u2
				semirecta_h()
				root.u1,root.u2,root.v1,root.v2=300-tall_x,300,v1+300,300+v2
				semirecta_h()
			elif(u2<0 and v2>0):
				root.u1,root.u2,root.v1,root.v2=300-tall_x,300,v1+300,300-v2
				semirecta_h()
				root.u1,root.u2,root.v1,root.v2=300-tall_x,300,u1+300,300+u2
				semirecta_h()
			else:
				w2=10
				w1=math.sqrt(r_recta**2-(w2-n)**2)-m
				w4=-10
				w3=math.sqrt(r_recta**2-(w4-n)**2)-m
				if(w1<-300 or w1>300):
					w1=-math.sqrt(r_recta**2-(w2-n)**2)-m
				if(w3<-300 or w3>300):
					w3=-math.sqrt(r_recta**2-(w4-n)**2)-m
				if(u2<0 and v2<0):
					root.u1,root.u2,root.v1,root.v2=300-tall_x,300,300-w1,290
					semirecta_h()
					root.u1,root.u2,root.v1,root.v2=300-tall_x,300,300-w3,290
					semirecta_h()
				else:
					root.u1,root.u2,root.v1,root.v2=300-tall_x,300,300-w3,290
					semirecta_h()
					root.u1,root.u2,root.v1,root.v2=300-tall_x,300,u1+300,300-u2
					semirecta_h()
	elif(u2<300 and v2>300):
		root.u1,root.u2,root.v1,root.v2=300,300,u1,u2
		semirecta_h()
		root.u1,root.u2,root.v1,root.v2=300,300,v1,-v2
		semirecta_h()
	elif(u2>300 and v2<300):
		root.u1,root.u2,root.v1,root.v2=300,300,u1,-u2
		semirecta_h()
		root.u1,root.u2,root.v1,root.v2=300,300,v1,v2
		semirecta_h()
	elif(u2<300 and v2<300):
		root.u1,root.u2,root.v1,root.v2=300,300,u1,u2
		semirecta_h()
		root.u1,root.u2,root.v1,root.v2=300,300,300-v1,v2
		semirecta_h()
	elif(u2>300 and v2>300):
		root.u1,root.u2,root.v1,root.v2=300,300,u1,-u2
		semirecta_h()
		root.u1,root.u2,root.v1,root.v2=300,300,300-v1,-v2
		semirecta_h()
	root.false2=True

def quadrat_h():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_recta=Label(root3, text="Per usar el quadrilater feu clic als 4 punts del disc desitjats i a continuació feu clic al botó de crear quadrilaters.")
	elif(idioma_elegit=="Español"):
		info_recta=Label(root3, text="Para usar el cuadrilatero haced clic a los 4 puntos del disco deseados y a continuación haced clic al botón de crear cuadrilateros.")
	elif(idioma_elegit=="English"):
		info_recta=Label(root3, text="To use the quadrilateral do click at the 4 desired points of the disk and then click the button to create quadrilaterals.")
	elif(idioma_elegit=="Deutsch"):
		info_recta=Label(root3, text="Um das Viereck zu verwenden, klicken Sie auf die 4 gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Vierecke zu erstellen.")
	info_recta.pack()
	u1,u2,v1,v2,w1,w2,y1,y2=root.u1,root.u2,root.v1,root.v2,root.w1,root.w2,root.y1,root.y2
	root.false=False
	root.false2=False
	root2.u1,root2.u2,root2.v1,root2.v2=u1,u2,v1,v2
	segment_h()
	root2.u1,root2.u2,root2.v1,root2.v2=v1,v2,w1,w2
	segment_h()
	root2.u1,root2.u2,root2.v1,root2.v2=w1,w2,y1,y2
	segment_h()
	root2.u1,root2.u2,root2.v1,root2.v2=y1,y2,u1,u2
	segment_h()
	root.false=True
	root.false2=True

def quadrat_h_full():
	for ele in root3.winfo_children():
		ele.destroy()
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		info_recta=Label(root3, text="Per usar el quadrilater feu clic als 4 punts del disc desitjats i a continuació feu clic al botó de crear quadrilaters.")
	elif(idioma_elegit=="Español"):
		info_recta=Label(root3, text="Para usar el cuadrilatero haced clic a los 4 puntos del disco deseados y a continuación haced clic al botón de crear quadrilateros.")
	elif(idioma_elegit=="English"):
		info_recta=Label(root3, text="To use the quadrilateral do click at the 4 desired points of the disk and then click the button to create quadrilaterals.")
	elif(idioma_elegit=="Deutsch"):
		info_recta=Label(root3, text="Um das Viereck zu verwenden, klicken Sie auf die 4 gewünschten Punkte der Scheibe und dann auf die Schaltfläche, um Vierecke zu erstellen.")
	info_recta.pack()
	root.false2=False
	root2.u1,root2.u2,root2.v1,root2.v2=root.u1,root.u2,root.v1,root.v2
	segment_h_full()
	root2.u1,root2.u2,root2.v1,root2.v2=root.v1,root.v2,root.w1,root.w2
	segment_h_full()
	root2.u1,root2.u2,root2.v1,root2.v2=root.w1,root.w2,root.y1,root.y2
	segment_h_full()
	root2.u1,root2.u2,root2.v1,root2.v2=root.y1,root.y2,root.u1,root.u2
	segment_h_full()
	root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2=root.u1,root.u2,root.v1,root.v2,root.w1,root.w2
	area_h(False)
	a1,a,b,c=root.area,root.a,root.b,root.c
	root3.u1,root3.u2,root3.v1,root3.v2,root3.w1,root3.w2=root.w1,root.w2,root.y1,root.y2,root.u1,root.u2
	area_h(False)
	a2,d,e,f=root.area,root.a,root.b,root.c
	A=a+e
	B=c
	C=b+d
	D=f
	area_t=a1+a2
	if(area_t==math.pi):
		area_t="π"
	elif(area_t==2*math.pi):
		area_t="2π"
	else:
		area_t=str(area_t)
	idioma_elegit=idioma.get()
	if(idioma_elegit=="Català"):
		text_a="L'angule A és: "+str(A*180/math.pi)
		text_b="L'angule B és: "+str(B*180/math.pi)
		text_c="L'angule C és: "+str(C*180/math.pi)
		text_d="L'angule D és: "+str(D*180/math.pi)
		text_e="L'àrea és: "+area_t
	elif(idioma_elegit=="Español"):
		text_a="El angulo A es: "+str(A*180/math.pi)
		text_b="El angulo B es: "+str(B*180/math.pi)
		text_c="El angulo C es: "+str(C*180/math.pi)
		text_d="El angulo D es: "+str(D*180/math.pi)
		text_e="El area es: "+area_t
	elif(idioma_elegit=="Deutsch"):
		text_a="The angle A is: "+str(A*180/math.pi)
		text_b="The angle B is: "+str(B*180/math.pi)
		text_c="The angle C is: "+str(C*180/math.pi)
		text_d="The angle D is: "+str(D*180/math.pi)
		text_e="The area is: "+area_t
	label_angle_a=Label(root2, text=text_a, width=50)
	label_angle_b=Label(root2, text=text_b, width=50)
	label_angle_c=Label(root2, text=text_c, width=50)
	label_angle_d=Label(root2, text=text_d, width=50)
	label_area=Label(root2, text=text_e, width=50)
	label_angle_a.pack(expand=1)
	label_angle_b.pack(expand=1)
	label_angle_c.pack(expand=1)
	label_angle_d.pack(expand=1)
	label_area.pack(expand=1)
	root.false2=True

def click(event):
	thread = Thread(target=play_sound_clic)
	thread.start()
	x = event.x_root - disc.winfo_rootx() 
	y = event.y_root - disc.winfo_rooty()
	root.counter+=1
	root.counter2+=1
	if(root.counter==1):
		try:
			del root.u1,root.u2
			root.u1,root.u2=x,y
		except:
			root.u1,root.u2=x,y
	elif(root.counter==2):
		try:
			del root.v1,root.v2
			root.v1,root.v2=x,y
		except:
			root.v1,root.v2=x,y
	elif(root.counter==3):
		try:
			del root.w1,root.w2
			root.w1,root.w2=x,y
		except:
			root.w1,root.w2=x,y
	elif(root.counter==4):
		try:
			del root.y1,root.y2
			root.y1,root.y2=x,y
		except:
			root.y1,root.y2=x,y
		root.counter=0
	if(root.counter==12):
		root.counter=0
disc.bind("<Button-1>", click)

#----Assignar funcions a cada botó----

def a_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		recta_h()
	elif(funcions_elegides=="Funcions 2"):
		triangle_h()

def b_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		semirecta_h()
	elif(funcions_elegides=="Funcions 2"):
		triangle_h_full()

def c_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		segment_h()
	elif(funcions_elegides=="Funcions 2"):
		segment_h_full()

def d_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		cercle_h()
	elif(funcions_elegides=="Funcions 2"):
		abs_x()

def e_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		cercle_2_h()
	elif(funcions_elegides=="Funcions 2"):
		quadrat_h()

def f_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		cercle_h_full()
	elif(funcions_elegides=="Funcions 2"):
		quadrat_h_full()

def g_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		eliminar()
	elif(funcions_elegides=="Funcions 2"):
		eliminar_resultats()

def h_h():
	winsound.PlaySound("Sons\\Botò", winsound.SND_FILENAME)
	funcions_elegides=funcions_h.get()
	if(funcions_elegides=="Funcions 1"):
		info()
	elif(funcions_elegides=="Funcions 2"):
		agrair()

#----Botons----

botó_recta=Button(myFrame,textvariable=var1, fg="red", bg="#875F5F", activebackground="red", activeforeground="#875F5F", width=15, cursor="hand2", command=a_h)
botó_recta.grid(row=0, column=2 )

botó_raig=Button(myFrame,textvariable=var2, fg="#FF9700", bg="#80715B", activebackground="#FF9700", activeforeground="#80715B", width=15, cursor="hand2", command=b_h)
botó_raig.grid(row=0, column=4)

botó_segment=Button(myFrame,textvariable=var3, fg="#FFEC00", bg="#7E8041", activebackground="#FFEC00", activeforeground="#7E8041", width=15, cursor="hand2", command=c_h)
botó_segment.grid(row=0, column=6)

botó_cercle=Button(myFrame,textvariable=var4, fg="#00FBFF", bg="#547E81", activebackground="#00FBFF", activeforeground="#547E81", width=15, cursor="hand2", command=d_h)
botó_cercle.grid(row=1, column=2)

botó_cercle_2=Button(myFrame,textvariable=var5, fg="#002BFF", bg="#454D79", activebackground="#002BFF", activeforeground="#454D79", width=15, cursor="hand2", command=e_h)
botó_cercle_2.grid(row=1, column=4)

botó_arc=Button(myFrame,textvariable=var6, fg="#9700FF", bg="#694483", activebackground="#9700FF", activeforeground="#694483", width=15, cursor="hand2", command=f_h)
botó_arc.grid(row=1, column=6)

os.chdir("C:\\Users\\USUARIO\\Documents\\Hiperbolic Geometry\\Imatges")

botó_eliminar=Button(myFrame,textvariable=var7, fg="#1EB700", bg="#406F36", activebackground="#1EB700", activeforeground="#406F36", width=15, cursor="@Trash.cur", command=g_h)
botó_eliminar.grid(row=0, column=8)

botó_info=Button(myFrame,textvariable=var8, fg="#D500FF", bg="#65386E", activebackground="#D500FF", activeforeground="#65386E", width=15, cursor="@Question_Mark.cur", command=h_h)
botó_info.grid(row=1, column=8)

os.chdir("C:\\Users\\USUARIO\\Documents\\Hiperbolic Geometry")

#----Final----

disc.pack()
root.mainloop()
musica=False
pygame.mixer.stop()