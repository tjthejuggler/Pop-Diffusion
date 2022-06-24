#ARTIST MORPH PORTRAITS---------------------------------------------------------------------------

people_artists = ['Edward Burne-Jones', 'Karol Bak', 'Jeff Easley', 'Brian Froud', 'Wendy Froud', 'Peter Gric', 'Jim Burns', 'Michael Whelan', 'Tyler Edlin', 'H.P. Lovecraft', 'Tim Burton', 'Yoshitaka Amano', 'Wes Anderson', 'Esao Andrews', 'Giuseppe Arcimboldo', 'Banksy', 'Ivan Bilibin', 'Alexander Bogen', 'Sandro Botticelli', 'Caravaggio', 'Camille Corot', 'Walter Crane', 'Geof Darrow', 'Eugene Delacroix', 'Paul Delvaux', 'Edmund Dulac', 'Albrecht Dürer', 'Larry Elmore', 'John Philip Falter', 'Caspar David Friedrich', 'Francisco Goya', 'Rebecca Guay', 'Winslow Homer', 'Edward Hopper', 'Frida Kahlo', 'Gustav Klimt', 'Ilya Kuvshinov', 'Rene Magritte', 'Don Maitz', 'John Martin', 'Peter Max', 'Robert McCall', 'Ralph McQuarrie', 'Frank Miller', 'Moebius', 'Chris Moore', 'Alphonse Mucha', 'Ted Nasmith', 'Victo Ngai', 'Rafal Olbinski', 'Diego Rivera', 'Hubert Robert', 'Andreas Rocha', 'Norman Rockwell', 'Egon Schiele', 'Ivan Shishkin', 'Marc Simonetti', 'Zack Snyder', 'Joaquín Sorolla', 'Simon Stalenhag', 'Ross Tran', 'Vincent Van Gogh', 'Rembrandt van Rijn', 'Ron Walotsky', 'Andy Warhol', 'Liam Wong', 'Yuumei', 'Amir Zand', 'Edgar Degas', 'Asher Brown Durand', 'Giovanni Battista Gaulli', 'Donato Giancola', 'John Atkinson Grimshaw', 'James Gurney', 'Jamie Hewlett', 'Ernst Ludwig Kirchner', 'Claude Monet', 'Igor Morski', 'Victor Moscoso', 'Craig Mullins', 'Nicholas Roerich', 'Hans Baldung', 'John Bauer', 'Julie Bell', 'Hans Bellmer', 'Mary Blair', 'William Blake', 'Victor Brauner', 'Gaston Bussière', 'Claude Cahun', 'Clyde Caldwell', 'Canaletto', 'Marcel Chagall', 'James C. Christensen', 'Giorgio de Chirico', 'Evelyn De Morgan', 'Henri de Toulouse-Lautrec', 'Gustave Doré', 'Jesper Ejsing', 'Harold Elliott', 'Anton Otto Fischer', 'Art Fitzpatrick', 'Jean-Honoré Fragonard', 'Victoria Francés', 'Frank Frazetta', 'Josan Gonzalez', 'Bastien Lecouffe-Deharme', 'George Luks', 'Victor Adame Minguez', 'Peter Mohrbacher', 'Ilya Repin', 'RHADS', 'Masamune Shirow', 'Coby Whitmore', 'Alex Grey', 'Junji Ito', 'Mati Klarwein', 'Kazimir Malevich', 'Clovis Trouille', 'Diego Velázquez', 'Qian Xuan', 'Nele Zirnite', 'Simon Bisley', 'Pascal Blanché', 'Arnold Böcklin', 'Camille-Pierre Pambu Bodo', 'William-Adolphe Bouguereau', 'Eleanor Vere Boyle', 'Arik Brauer', 'Pieter Bruegel the Elder', 'Paul Cézanne', 'Leonardo da Vinci', 'Richard Dadd', 'Max Ernst', 'Kelly Freas', 'Ernst Fuchs', 'Henry Fuseli', 'Paul Gauguin', 'Emma Geary', 'Artemisia Gentileschi', 'Warwick Goble', 'Rob Gonsalves', 'Jane Graverol', 'Henriette Grindat', 'Matthias Grünewald', 'Thomas Häfner', 'Sydney Prior Hall', 'Keith Haring', 'Rudolf Hausner', 'Brothers Hildebrandt', 'Tim Hildebrandt', 'Greg Hildebrandt', 'William Hogarth', 'Kati Horna', 'Valentine Hugo', 'George Inness', 'Jarosław Jaśnikowski', 'Joe Jusko', 'Filippino Lippi', 'Bob Ringwood', 'Jakub Rozalski', 'Greg Rutkowski', 'Mike Winkelmann', 'Seb McKinnon', 'Daniel Merriam', 'Sylvain Sarrailh', 'Tom Lovell', 'Haddon Sundblom', 'Eddie Mendoza', 'Eugeniusz Zak', 'Frank Zappa', 'Pablo Dominguez', 'Cicely Mary Barker', 'Amy Brown', 'Stephanie Law', 'Neil Welliver', 'Child Hassam', 'Henri Matisse', 'Jules Dupré', 'Pieter Brueghel the Elder', 'Theodore Robinson', 'Alexei Savrasov', 'Arkhip Kuindzhi', 'Claude Lorraine', 'Pablo Amaringo', 'Pascal Blanche', 'Adam Varga', 'Android Jones', 'Simon Hennessey', 'Denis Peterson', 'Robert Bechtle', 'Gustavo Silva Nuez', 'Claudio Bravo', 'Gottfried Helnwein', 'István Sándorfi', 'Nestor Leynes', 'Franz Gertsch', 'Kareem Olamilekan', 'Dragan Malešević Tapi', 'Ian Hornak', 'Otto Duecker', 'Antoni Taulé', 'Willem van Veldhuizen', 'Andrey Lekarski', 'Walther Jervolino', 'Diego Koi', 'Allyssa Monks', 'Luiz Escanuela', 'Dirk Dzimirsky']
import random
random_artist = random.choice(people_artists)
text_prompts = {}

for i in range(50):
  text_prompts[i] = [
            "Beautiful detailed portrait of an animal demigoddess by Nick Silva," +random.choice(people_artists)+", "+random.choice(people_artists)+", Symmetrical composition with people centered, trending on artstation, colorized:4",
            "text:-2",
            "glasses:-1",
            "color:1"
        ]

image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}



#EVOLUTION MORPH---------------------------------------------------------------------------

text_prompts = {}

evolutions = [
"single celled organism",
"colorful virus",
"green and red fungus",
"beige clam",
"orange shrimp",
"purple octopus",
"red and black scorpion",
"black and green spider",
"red crab",
"brown rat",
"light brown lemur",
"brown monkey",
"orange orangutan",
"brown gorilla",
"bonobo",
"chimpanzee",
"realistically-colored neanderthal",
"flesh-colored human",
"humanoid robot",
"futuristic tech robot"
]

for i in range(len(evolutions) * 30):
    if i == 0:
        text_prompts[i] = ["Beautiful detailed picture of earth by Nick Silva, Jim Burns, Noah Bradley, Symmetrical composition with people centered, colorized, trending on artstation:4", "text:-2", "glasses:-1", "color:1"]

    elif (i%30 == 0):
        j = math.floor(i / 30)
        if j > 0:
          text_prompts[i] = [
              "Beautiful detailed portrait of a hyperrealistic "+evolutions[j-1]+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, greyscale:4",
              "text:-2",
              "glasses:-1"
          ]
image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}

#MORPH RANDOM ARTISTS WITH REVERSE AGING--------------------------------------------------------------

people_artists = ['Edward Burne-Jones', 'Karol Bak', 'Jeff Easley', 'Brian Froud', 'Wendy Froud', 'Peter Gric', 'Jim Burns', 'Michael Whelan', 'Tyler Edlin', 'H.P. Lovecraft', 'Tim Burton', 'Yoshitaka Amano', 'Wes Anderson', 'Esao Andrews', 'Giuseppe Arcimboldo', 'Banksy', 'Ivan Bilibin', 'Alexander Bogen', 'Sandro Botticelli', 'Caravaggio', 'Camille Corot', 'Walter Crane', 'Geof Darrow', 'Eugene Delacroix', 'Paul Delvaux', 'Edmund Dulac', 'Albrecht Dürer', 'Larry Elmore', 'John Philip Falter', 'Caspar David Friedrich', 'Francisco Goya', 'Rebecca Guay', 'Winslow Homer', 'Edward Hopper', 'Frida Kahlo', 'Gustav Klimt', 'Ilya Kuvshinov', 'Rene Magritte', 'Don Maitz', 'John Martin', 'Peter Max', 'Robert McCall', 'Ralph McQuarrie', 'Frank Miller', 'Moebius', 'Chris Moore', 'Alphonse Mucha', 'Ted Nasmith', 'Victo Ngai', 'Rafal Olbinski', 'Diego Rivera', 'Hubert Robert', 'Andreas Rocha', 'Norman Rockwell', 'Egon Schiele', 'Ivan Shishkin', 'Marc Simonetti', 'Zack Snyder', 'Joaquín Sorolla', 'Simon Stalenhag', 'Ross Tran', 'Vincent Van Gogh', 'Rembrandt van Rijn', 'Ron Walotsky', 'Andy Warhol', 'Liam Wong', 'Yuumei', 'Amir Zand', 'Edgar Degas', 'Asher Brown Durand', 'Giovanni Battista Gaulli', 'Donato Giancola', 'John Atkinson Grimshaw', 'James Gurney', 'Jamie Hewlett', 'Ernst Ludwig Kirchner', 'Claude Monet', 'Igor Morski', 'Victor Moscoso', 'Craig Mullins', 'Nicholas Roerich', 'Hans Baldung', 'John Bauer', 'Julie Bell', 'Hans Bellmer', 'Mary Blair', 'William Blake', 'Victor Brauner', 'Gaston Bussière', 'Claude Cahun', 'Clyde Caldwell', 'Canaletto', 'Marcel Chagall', 'James C. Christensen', 'Giorgio de Chirico', 'Evelyn De Morgan', 'Henri de Toulouse-Lautrec', 'Gustave Doré', 'Jesper Ejsing', 'Harold Elliott', 'Anton Otto Fischer', 'Art Fitzpatrick', 'Jean-Honoré Fragonard', 'Victoria Francés', 'Frank Frazetta', 'Josan Gonzalez', 'Bastien Lecouffe-Deharme', 'George Luks', 'Victor Adame Minguez', 'Peter Mohrbacher', 'Ilya Repin', 'RHADS', 'Masamune Shirow', 'Coby Whitmore', 'Alex Grey', 'Junji Ito', 'Mati Klarwein', 'Kazimir Malevich', 'Clovis Trouille', 'Diego Velázquez', 'Qian Xuan', 'Nele Zirnite', 'Simon Bisley', 'Pascal Blanché', 'Arnold Böcklin', 'Camille-Pierre Pambu Bodo', 'William-Adolphe Bouguereau', 'Eleanor Vere Boyle', 'Arik Brauer', 'Pieter Bruegel the Elder', 'Paul Cézanne', 'Leonardo da Vinci', 'Richard Dadd', 'Max Ernst', 'Kelly Freas', 'Ernst Fuchs', 'Henry Fuseli', 'Paul Gauguin', 'Emma Geary', 'Artemisia Gentileschi', 'Warwick Goble', 'Rob Gonsalves', 'Jane Graverol', 'Henriette Grindat', 'Matthias Grünewald', 'Thomas Häfner', 'Sydney Prior Hall', 'Keith Haring', 'Rudolf Hausner', 'Brothers Hildebrandt', 'Tim Hildebrandt', 'Greg Hildebrandt', 'William Hogarth', 'Kati Horna', 'Valentine Hugo', 'George Inness', 'Jarosław Jaśnikowski', 'Joe Jusko', 'Filippino Lippi', 'Bob Ringwood', 'Jakub Rozalski', 'Greg Rutkowski', 'Mike Winkelmann', 'Seb McKinnon', 'Daniel Merriam', 'Sylvain Sarrailh', 'Tom Lovell', 'Haddon Sundblom', 'Eddie Mendoza', 'Eugeniusz Zak', 'Frank Zappa', 'Pablo Dominguez', 'Cicely Mary Barker', 'Amy Brown', 'Stephanie Law', 'Neil Welliver', 'Child Hassam', 'Henri Matisse', 'Jules Dupré', 'Pieter Brueghel the Elder', 'Theodore Robinson', 'Alexei Savrasov', 'Arkhip Kuindzhi', 'Claude Lorraine', 'Pablo Amaringo', 'Pascal Blanche', 'Adam Varga', 'Android Jones', 'Simon Hennessey', 'Denis Peterson', 'Robert Bechtle', 'Gustavo Silva Nuez', 'Claudio Bravo', 'Gottfried Helnwein', 'István Sándorfi', 'Nestor Leynes', 'Franz Gertsch', 'Kareem Olamilekan', 'Dragan Malešević Tapi', 'Ian Hornak', 'Otto Duecker', 'Antoni Taulé', 'Willem van Veldhuizen', 'Andrey Lekarski', 'Walther Jervolino', 'Diego Koi', 'Allyssa Monks', 'Luiz Escanuela', 'Dirk Dzimirsky']
import random
random_artist = random.choice(people_artists)
text_prompts = {}
frames_scale_input = ""
frame_skip_steps_input = ""


for i in range(100):
  # text_prompts[i] = ["Beautiful detailed portrait of a man from the year "+str(((i+1)*25)+100)+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation:4",
  #    "text:-2", "glasses:-1"]
  j = i
  if j > 95:
    text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(100 - j)+" year old adorable baby by Nick Silva," +random.choice(people_artists)+", "+random.choice(people_artists)+", Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1"
      ]
  elif j > 85:
    text_prompts[i] =     text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(100 - j)+" year old playful boy by Nick Silva," +random.choice(people_artists)+", "+random.choice(people_artists)+", Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1"
      ]
  else:
    text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(100 - j)+" year serious man by Nick Silva," +random.choice(people_artists)+", "+random.choice(people_artists)+", Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1",
          "color: 1"
      ]

image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}

#RANDOM ARTISTS WITH AGING----------------------------------------------------------

people_artists = ['Edward Burne-Jones', 'Karol Bak', 'Jeff Easley', 'Brian Froud', 'Wendy Froud', 'Peter Gric', 'Jim Burns', 'Michael Whelan', 'Tyler Edlin', 'H.P. Lovecraft', 'Tim Burton', 'Yoshitaka Amano', 'Wes Anderson', 'Esao Andrews', 'Giuseppe Arcimboldo', 'Banksy', 'Ivan Bilibin', 'Alexander Bogen', 'Sandro Botticelli', 'Caravaggio', 'Camille Corot', 'Walter Crane', 'Geof Darrow', 'Eugene Delacroix', 'Paul Delvaux', 'Edmund Dulac', 'Albrecht Dürer', 'Larry Elmore', 'John Philip Falter', 'Caspar David Friedrich', 'Francisco Goya', 'Rebecca Guay', 'Winslow Homer', 'Edward Hopper', 'Frida Kahlo', 'Gustav Klimt', 'Ilya Kuvshinov', 'Rene Magritte', 'Don Maitz', 'John Martin', 'Peter Max', 'Robert McCall', 'Ralph McQuarrie', 'Frank Miller', 'Moebius', 'Chris Moore', 'Alphonse Mucha', 'Ted Nasmith', 'Victo Ngai', 'Rafal Olbinski', 'Diego Rivera', 'Hubert Robert', 'Andreas Rocha', 'Norman Rockwell', 'Egon Schiele', 'Ivan Shishkin', 'Marc Simonetti', 'Zack Snyder', 'Joaquín Sorolla', 'Simon Stalenhag', 'Ross Tran', 'Vincent Van Gogh', 'Rembrandt van Rijn', 'Ron Walotsky', 'Andy Warhol', 'Liam Wong', 'Yuumei', 'Amir Zand', 'Edgar Degas', 'Asher Brown Durand', 'Giovanni Battista Gaulli', 'Donato Giancola', 'John Atkinson Grimshaw', 'James Gurney', 'Jamie Hewlett', 'Ernst Ludwig Kirchner', 'Claude Monet', 'Igor Morski', 'Victor Moscoso', 'Craig Mullins', 'Nicholas Roerich', 'Hans Baldung', 'John Bauer', 'Julie Bell', 'Hans Bellmer', 'Mary Blair', 'William Blake', 'Victor Brauner', 'Gaston Bussière', 'Claude Cahun', 'Clyde Caldwell', 'Canaletto', 'Marcel Chagall', 'James C. Christensen', 'Giorgio de Chirico', 'Evelyn De Morgan', 'Henri de Toulouse-Lautrec', 'Gustave Doré', 'Jesper Ejsing', 'Harold Elliott', 'Anton Otto Fischer', 'Art Fitzpatrick', 'Jean-Honoré Fragonard', 'Victoria Francés', 'Frank Frazetta', 'Josan Gonzalez', 'Bastien Lecouffe-Deharme', 'George Luks', 'Victor Adame Minguez', 'Peter Mohrbacher', 'Ilya Repin', 'RHADS', 'Masamune Shirow', 'Coby Whitmore', 'Alex Grey', 'Junji Ito', 'Mati Klarwein', 'Kazimir Malevich', 'Clovis Trouille', 'Diego Velázquez', 'Qian Xuan', 'Nele Zirnite', 'Simon Bisley', 'Pascal Blanché', 'Arnold Böcklin', 'Camille-Pierre Pambu Bodo', 'William-Adolphe Bouguereau', 'Eleanor Vere Boyle', 'Arik Brauer', 'Pieter Bruegel the Elder', 'Paul Cézanne', 'Leonardo da Vinci', 'Richard Dadd', 'Max Ernst', 'Kelly Freas', 'Ernst Fuchs', 'Henry Fuseli', 'Paul Gauguin', 'Emma Geary', 'Artemisia Gentileschi', 'Warwick Goble', 'Rob Gonsalves', 'Jane Graverol', 'Henriette Grindat', 'Matthias Grünewald', 'Thomas Häfner', 'Sydney Prior Hall', 'Keith Haring', 'Rudolf Hausner', 'Brothers Hildebrandt', 'Tim Hildebrandt', 'Greg Hildebrandt', 'William Hogarth', 'Kati Horna', 'Valentine Hugo', 'George Inness', 'Jarosław Jaśnikowski', 'Joe Jusko', 'Filippino Lippi', 'Bob Ringwood', 'Jakub Rozalski', 'Greg Rutkowski', 'Mike Winkelmann', 'Seb McKinnon', 'Daniel Merriam', 'Sylvain Sarrailh', 'Tom Lovell', 'Haddon Sundblom', 'Eddie Mendoza', 'Eugeniusz Zak', 'Frank Zappa', 'Pablo Dominguez', 'Cicely Mary Barker', 'Amy Brown', 'Stephanie Law', 'Neil Welliver', 'Child Hassam', 'Henri Matisse', 'Jules Dupré', 'Pieter Brueghel the Elder', 'Theodore Robinson', 'Alexei Savrasov', 'Arkhip Kuindzhi', 'Claude Lorraine', 'Pablo Amaringo', 'Pascal Blanche', 'Adam Varga', 'Android Jones', 'Simon Hennessey', 'Denis Peterson', 'Robert Bechtle', 'Gustavo Silva Nuez', 'Claudio Bravo', 'Gottfried Helnwein', 'István Sándorfi', 'Nestor Leynes', 'Franz Gertsch', 'Kareem Olamilekan', 'Dragan Malešević Tapi', 'Ian Hornak', 'Otto Duecker', 'Antoni Taulé', 'Willem van Veldhuizen', 'Andrey Lekarski', 'Walther Jervolino', 'Diego Koi', 'Allyssa Monks', 'Luiz Escanuela', 'Dirk Dzimirsky']
import random
random_artist = random.choice(people_artists)
    text_prompts = {}
    frames_scale_input = ""
    frame_skip_steps_input = ""

    for i in range(110):
    # text_prompts[i] = ["Beautiful detailed portrait of a man from the year "+str(((i+1)*25)+100)+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation:4",
    #    "text:-2", "glasses:-1"]
    j = i
    if j > 10:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(j-15)+" year old teddy bear by " +random.choice(people_artists)+", Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:4",
            "text:-2",
            "glasses:-1"
        ]
    elif j > 5:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(j-5)+" month old teddy bear by " +random.choice(people_artists)+", Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:4",
            "text:-2",
            "glasses:-1"
        ]
    else:
        text_prompts[i] = [
            "Beautiful detailed portrait of an adorable "+str(j)+" day old teddy bear baby by " +random.choice(people_artists)+", Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:4",
            "text:-2",
            "glasses:-1",
            "color: 1"
        ]

    image_prompts = {
        # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
    }

#-------------------------
#ARTIST MORPH PORTRAITS

people_artists = ['Edward Burne-Jones', 'Karol Bak', 'Jeff Easley', 'Brian Froud', 'Wendy Froud', 'Peter Gric', 'Jim Burns', 'Michael Whelan', 'Tyler Edlin', 'H.P. Lovecraft', 'Tim Burton', 'Yoshitaka Amano', 'Wes Anderson', 'Esao Andrews', 'Giuseppe Arcimboldo', 'Banksy', 'Ivan Bilibin', 'Alexander Bogen', 'Sandro Botticelli', 'Caravaggio', 'Camille Corot', 'Walter Crane', 'Geof Darrow', 'Eugene Delacroix', 'Paul Delvaux', 'Edmund Dulac', 'Albrecht Dürer', 'Larry Elmore', 'John Philip Falter', 'Caspar David Friedrich', 'Francisco Goya', 'Rebecca Guay', 'Winslow Homer', 'Edward Hopper', 'Frida Kahlo', 'Gustav Klimt', 'Ilya Kuvshinov', 'Rene Magritte', 'Don Maitz', 'John Martin', 'Peter Max', 'Robert McCall', 'Ralph McQuarrie', 'Frank Miller', 'Moebius', 'Chris Moore', 'Alphonse Mucha', 'Ted Nasmith', 'Victo Ngai', 'Rafal Olbinski', 'Diego Rivera', 'Hubert Robert', 'Andreas Rocha', 'Norman Rockwell', 'Egon Schiele', 'Ivan Shishkin', 'Marc Simonetti', 'Zack Snyder', 'Joaquín Sorolla', 'Simon Stalenhag', 'Ross Tran', 'Vincent Van Gogh', 'Rembrandt van Rijn', 'Ron Walotsky', 'Andy Warhol', 'Liam Wong', 'Yuumei', 'Amir Zand', 'Edgar Degas', 'Asher Brown Durand', 'Giovanni Battista Gaulli', 'Donato Giancola', 'John Atkinson Grimshaw', 'James Gurney', 'Jamie Hewlett', 'Ernst Ludwig Kirchner', 'Claude Monet', 'Igor Morski', 'Victor Moscoso', 'Craig Mullins', 'Nicholas Roerich', 'Hans Baldung', 'John Bauer', 'Julie Bell', 'Hans Bellmer', 'Mary Blair', 'William Blake', 'Victor Brauner', 'Gaston Bussière', 'Claude Cahun', 'Clyde Caldwell', 'Canaletto', 'Marcel Chagall', 'James C. Christensen', 'Giorgio de Chirico', 'Evelyn De Morgan', 'Henri de Toulouse-Lautrec', 'Gustave Doré', 'Jesper Ejsing', 'Harold Elliott', 'Anton Otto Fischer', 'Art Fitzpatrick', 'Jean-Honoré Fragonard', 'Victoria Francés', 'Frank Frazetta', 'Josan Gonzalez', 'Bastien Lecouffe-Deharme', 'George Luks', 'Victor Adame Minguez', 'Peter Mohrbacher', 'Ilya Repin', 'RHADS', 'Masamune Shirow', 'Coby Whitmore', 'Alex Grey', 'Junji Ito', 'Mati Klarwein', 'Kazimir Malevich', 'Clovis Trouille', 'Diego Velázquez', 'Qian Xuan', 'Nele Zirnite', 'Simon Bisley', 'Pascal Blanché', 'Arnold Böcklin', 'Camille-Pierre Pambu Bodo', 'William-Adolphe Bouguereau', 'Eleanor Vere Boyle', 'Arik Brauer', 'Pieter Bruegel the Elder', 'Paul Cézanne', 'Leonardo da Vinci', 'Richard Dadd', 'Max Ernst', 'Kelly Freas', 'Ernst Fuchs', 'Henry Fuseli', 'Paul Gauguin', 'Emma Geary', 'Artemisia Gentileschi', 'Warwick Goble', 'Rob Gonsalves', 'Jane Graverol', 'Henriette Grindat', 'Matthias Grünewald', 'Thomas Häfner', 'Sydney Prior Hall', 'Keith Haring', 'Rudolf Hausner', 'Brothers Hildebrandt', 'Tim Hildebrandt', 'Greg Hildebrandt', 'William Hogarth', 'Kati Horna', 'Valentine Hugo', 'George Inness', 'Jarosław Jaśnikowski', 'Joe Jusko', 'Filippino Lippi', 'Bob Ringwood', 'Jakub Rozalski', 'Greg Rutkowski', 'Mike Winkelmann', 'Seb McKinnon', 'Daniel Merriam', 'Sylvain Sarrailh', 'Tom Lovell', 'Haddon Sundblom', 'Eddie Mendoza', 'Eugeniusz Zak', 'Frank Zappa', 'Pablo Dominguez', 'Cicely Mary Barker', 'Amy Brown', 'Stephanie Law', 'Neil Welliver', 'Child Hassam', 'Henri Matisse', 'Jules Dupré', 'Pieter Brueghel the Elder', 'Theodore Robinson', 'Alexei Savrasov', 'Arkhip Kuindzhi', 'Claude Lorraine', 'Pablo Amaringo', 'Pascal Blanche', 'Adam Varga', 'Android Jones', 'Simon Hennessey', 'Denis Peterson', 'Robert Bechtle', 'Gustavo Silva Nuez', 'Claudio Bravo', 'Gottfried Helnwein', 'István Sándorfi', 'Nestor Leynes', 'Franz Gertsch', 'Kareem Olamilekan', 'Dragan Malešević Tapi', 'Ian Hornak', 'Otto Duecker', 'Antoni Taulé', 'Willem van Veldhuizen', 'Andrey Lekarski', 'Walther Jervolino', 'Diego Koi', 'Allyssa Monks', 'Luiz Escanuela', 'Dirk Dzimirsky']
import random
random_artist = random.choice(people_artists)
text_prompts = {}
frames_scale_input = ""
frame_skip_steps_input = ""


for i in range(110):
  # text_prompts[i] = ["Beautiful detailed portrait of a man from the year "+str(((i+1)*25)+100)+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation:4",
  #    "text:-2", "glasses:-1"]
  j = i
  if j > 10:
    text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(j-10)+" year old mech elf by " +random.choice(people_artists)+", " +random.choice(people_artists)+", Shin JeongHo, Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1"
      ]
  elif j > 5:
    text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(j-5)+" month old mech elf by " +random.choice(people_artists)+", " +random.choice(people_artists)+", Shin JeongHo, Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1"
      ]
  else:
    text_prompts[i] = [
          "Beautiful detailed portrait of an adorable "+str(j)+" day old mech elf by " +random.choice(people_artists)+", " +random.choice(people_artists)+", Shin JeongHo, Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1",
          "color: 1"
      ]

image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}
#----------------------------------
text_prompts = {}


for i in range(110):
  # text_prompts[i] = ["Beautiful detailed portrait of a man from the year "+str(((i+1)*25)+100)+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation:4",
  #    "text:-2", "glasses:-1"]
  j = i
  if i % 8 == 0:
    cur_dir = 'left'
  elif i % 8 == 1:
    cur_dir = 'left and down'
  elif i % 8 == 2:
    cur_dir = 'down'
  elif i % 8 == 3:
    cur_dir = 'down and right'
  elif i % 8 == 4:
    cur_dir = 'right'
  elif i % 8 == 5:
    cur_dir = 'right and up'
  elif i % 8 == 6:
    cur_dir = 'up'
  elif i % 8 == 7:
    cur_dir = 'up and left'
  if j > 10:
    text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(j-15)+" year old wizard looking "+cur_dir+" by Nick Silva, Gottfried Helnwein, Jim Burns, Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1"
      ]
  elif j > 5:
    text_prompts[i] = [
          "Beautiful detailed portrait of a "+str(j-5)+" month old wizard looking "+cur_dir+" by Nick Silva, Gottfried Helnwein, Jim Burns, Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1"
      ]
  else:
    text_prompts[i] = [
          "Beautiful detailed portrait of an adorable "+str(j)+" day old wizard looking "+cur_dir+" baby by Nick Silva, Gottfried Helnwein, Jim Burns, Symmetrical composition with people centered, trending on artstation, colorized:4",
          "text:-2",
          "glasses:-1",
          "color: 1"
      ]

image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}