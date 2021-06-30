import time

def setup():
    global grid, dim, pressed, sim, swipe, scoc
    scoc = [-1,-1]
    pressed = True
    size(990,800)
    grid = []
    wide = 15
    swipe = False
    sim = True
    dim = [width/wide,48,wide]
    for rw in range(dim[0]):
        grid.append([])
        for cl in range(dim[1]):
            grid[-1].append(1)

def draw():
    global grid, dim, pressed, sim, swipe, scoc
    background(53)
    rectMode(CORNER)
    stroke(0)
    strokeWeight(4)
    for rw in range(dim[0]):
        for cl in range(dim[1]):
            fill(0)
            if grid[rw][cl] == -1: fill(255)
            rect(dim[2]*rw, dim[2]*cl,dim[2], dim[2])
    textAlign(CENTER)
    textSize(30)
    if sim:
        fill(0,0,0,0)
        strokeWeight(6)
        stroke(255,255,50)
        if int(mouseY/dim[2]) < len(grid[0]): rect(int(mouseX/dim[2])*dim[2], int(mouseY/dim[2])*dim[2],dim[2], dim[2])
        fill(0,255,0)
        stroke(0)
        strokeWeight(3)
        rect(15, 735, 160, 40)
        fill(0)
        text("Start", 95, 765)
        if swipe: fill(0,255,0)
        else: fill(255,0,0)
        rect(190, 735, 160, 40)
        fill(0)
        text("Swipe", 270, 765)
        fill(255,255,0)
        rect(365, 735, 160, 40)
        fill(0)
        text("Clear", 445, 765)
        if pressed and mousePressed:
            pressed = False
            if int(mouseY/dim[2]) < len(grid[0]) and swipe == False: grid[int(mouseX/dim[2])][int(mouseY/dim[2])] *= -1
            if abs(mouseX-95)<=80 and abs(mouseY-755)<=20: sim = False
            if abs(mouseX-270)<=80 and abs(mouseY-755)<=20: swipe = not(swipe)
            if abs(mouseX-445)<=80 and abs(mouseY-755)<=20:
                for rw in range(dim[0]):
                    for cl in range(dim[1]):
                        grid[rw][cl] = 1
        elif pressed == False and not(mousePressed):
            pressed = True
        if swipe:
            if mousePressed and int(mouseY/dim[2]) < len(grid[0]):
                if scoc != [int(mouseX/dim[2]),int(mouseY/dim[2])]:
                    scoc = [int(mouseX/dim[2]),int(mouseY/dim[2])]
                    grid[int(mouseX/dim[2])][int(mouseY/dim[2])] *= -1
            else: scoc = [-1,-1]
    elif sim == False:
        fill(255,0,0)
        stroke(0)
        strokeWeight(3)
        rect(15, 735, 160, 40)
        fill(0)
        text("End", 95, 765)
        if pressed and mousePressed:
            pressed = False
            if abs(mouseX-95)<=80 and abs(mouseY-755)<=20: sim = True
        elif pressed == False and not(mousePressed):
            pressed = True
        
        newgrid = []
        for rw in range(dim[0]):
            newgrid.append([])
            for cl in range(dim[1]):
                newgrid[-1].append(1)
        
        for rw in range(dim[0]):
            for cl in range(dim[1]):
                stuff = []
                gogy = [[rw+1,cl+1],[rw+1,cl],[rw+1,cl-1],[rw,cl-1],[rw-1,cl-1],[rw-1,cl],[rw-1,cl+1],[rw,cl+1]]
                for gog in gogy:
                    stuff.append(grid[(gog[0])%dim[0]][gog[1]%dim[1]])
                '''try: stuff.append(grid[rw+1][cl+1])
                except: pass
                try: stuff.append(grid[rw+1][cl])
                except: pass
                try: stuff.append(grid[rw+1][cl-1])
                except: pass
                try: stuff.append(grid[rw][cl-1])
                except: pass
                try: stuff.append(grid[rw-1][cl-1])
                except: pass
                try: stuff.append(grid[rw-1][cl])
                except: pass
                try: stuff.append(grid[rw-1][cl+1])
                except: pass
                try: stuff.append(grid[rw][cl+1])
                except: pass'''
                if grid[rw][cl] == -1 and (stuff.count(-1) == 3 or stuff.count(-1) == 2): newgrid[rw][cl] = -1
                elif stuff.count(-1) == 3 and grid[rw][cl] == 1: newgrid[rw][cl] = -1
                elif (stuff.count(-1) > 3 or stuff.count(-1) < 2) and grid[rw][cl] == -1: newgrid[rw][cl] = 1
        
        for rw in range(dim[0]):
            grid[rw] = list(newgrid[rw])
            
        time.sleep(0.05)
