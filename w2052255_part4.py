from graphics import * #import the graphics.py module

def histogram(GraphList):
#open the histogram window
    win = GraphWin("Histogram", 800, 600)
    win.setBackground("Mint Cream")

    maximum_count = 20
    Scale = 1200/maximum_count
    Progress_count = GraphList.count("Progress")
    Trailer_count = GraphList.count("Progress(module trailer)")
    Retriever_count = GraphList.count("Module retriever")
    Exclude_count = GraphList.count("Exclude")

    my_heading = Text(Point(120, 20), 'Histogram Result')
    my_heading.setSize(15)
    my_heading.draw(win)

    Rectangle1=Rectangle(Point(100,570),Point(210,570-(Scale*Progress_count)))
    Rectangle1.setFill("Green")
    Rectangle1.setWidth(1)
    Rectangle1.draw(win)
    text1=Text(Point(153, 583),'Progress')
    text1.draw(win)
    Rectangle1_text = Text(Point(150,550-(Scale*Progress_count)),Progress_count)
    Rectangle1_text.draw(win)
                                 

    Rectangle2=Rectangle(Point(218,570), Point(328,570-(Scale*Trailer_count)))
    Rectangle2.setFill("Blue")
    Rectangle2.setWidth(1)
    Rectangle2.draw(win)
    text2=Text(Point(274, 583), 'Trailer')
    text2.draw(win)
    Rectangle2_text = Text(Point(268,550-(Scale*Trailer_count)),Trailer_count)
    Rectangle2_text.draw(win)
                              
    
    Rectangle3=Rectangle(Point(336,570), Point(446,570-(Scale*Retriever_count)))
    Rectangle3.setFill("yellow")
    Rectangle3.setWidth(1)
    Rectangle3.draw(win)
    text3=Text(Point(390, 583), 'Retriever')
    text3.draw(win)
    Rectangle3_text = Text(Point(386,550-(Scale*Retriever_count)),Retriever_count)
    Rectangle3_text.draw(win)
                              

    Rectangle4=Rectangle(Point(454,570), Point(564,570-(Scale*Exclude_count)))
    Rectangle4.setFill("Red")
    Rectangle4.setWidth(1)
    Rectangle4.draw(win)
    text4=Text(Point(510, 583), 'Exclude')
    text4.draw(win)
    Rectangle4_text = Text(Point(504,550-(Scale*Exclude_count)),Exclude_count)
    Rectangle4_text.draw(win)
                              

    line=Line(Point(50,570), Point(614,570))
    line.setWidth(2)
    line.draw(win)






