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
            "Beautiful detailed portrait of a "+str(j-10)+" year old teddy bear by " +random.choice(people_artists)+", Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:4",
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

 #AGING WITH WEIGHT MORPH ------------------------------

text_prompts = {}
x_weight = -10
y_weight = 10
for i in range(120):
    if i > 10:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(i-10)+" year old tree person hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "evil: "+str(x_weight),
            "adorable: "+str(y_weight)
        ]
    elif i > 5:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(i-5)+" month old tree person hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "evil: "+str(x_weight),
            "adorable: "+str(y_weight)
        ]
    else:
        text_prompts[i] = [
            "Beautiful detailed portrait of an adorable "+str(i)+" day old baby tree person hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "evil: "+str(x_weight),
            "adorable: "+str(y_weight),
            "color: 3"
        ]
    if i % 6 == 0:
        x_weight+=1
    if (i+3) % 6 == 0:
        y_weight-=1

image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}

#FULL EVOLUTION LIST-----------------------------------------------------

"planet earth",
"water",
"single-celled organism",
"bacteria",
"viruses",
"land fungi",
"clams",
"shrimp",
"octopus",
"jellyfish",
"scorpions",
"spiders",
"housefly",
"earthworms",
"lizards",
"crabs",
"sharks",
"snakes",
"birds",
"beetles",
"dinosaurs",
"frogs",
"bees",
"crocodiles",
"ants",
"rodents",
"penguins",
"owls",
"parrots",
"bats",
"camels",
"butterflies",
"bears",
"pigs",
"cats",
"pelicans",
"deer",
"ostriches",
"giraffes",
"platypuses",
"Mammoths",
"blue whales",
"swordfish",
"coyotes",
"orangutan",

#NATIONALITIES MORPH------------------------------------------------------
nationalities = ["Afghan","Algerian","Angolan","Argentine","Austrian","Australian","Bangladeshi","Belarusian","Belgian","Bolivian","Bosnian/Herzegovinian","Brazilian","British","Bulgarian","Cambodian","Cameroonian","Canadian","Central African","Chadian","Chinese","Colombian","Costa Rican","Croatian","Czech","Congolese","Danish","Ecuadorian","Egyptian","Salvadoran","English","Estonian","Ethiopian","Finnish","French","German","Ghanaian","Greek","Guatemalan","Dutch","Honduran","Hungarian","Icelandic","Indian","Indonesian","Iranian","Iraqi","Irish","Israeli","Italian","Ivorian","Jamaican","Japanese","Jordanian","Kazakh","Kenyan","Lao","Latvian","Libyan","Lithuanian","Malagasy","Malaysian","Malian","Mauritanian","Mexican","Moroccan","Namibian","New Zealand","Nicaraguan","Nigerien","Nigerian","Norwegian","Omani","Pakistani","Panamanian","Paraguayan","Peruvian","Philippine","Polish","Portuguese","Congolese","Romanian","Russian","Saudi, Saudi Arabian","Scottish","Senegalese","Serbian","Singaporean","Slovak","Somalian","South African","Spanish","Sudanese","Swedish","Swiss","Syrian","Thai","Tunisian","Turkish","Turkmen","Ukranian","Emirati","American","Uruguayan","Vietnamese","Welsh","Zambian","Zimbabwea"]

frames_skip_steps_input = ""
text_prompts = {}
for frame in range(len(nationalities) * 4):
    age = frame//4
    nationality = nationalities[age]
    type = 'senior'
    if age < 5:
        type = 'baby'
    elif age < 12:
        type = 'child'
    elif age < 19:
        type = 'teenager'
    elif age < 55:
        type = 'adult'
    elif age < 65:
        type = 'elderly person'
    
    text_prompts[frame] = ["Beautiful detailed portrait of a "+str(age)+" day old "+nationality+" "+type+" by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation:4",
    "text:-2", "glasses:-1", "color:1" ]
    #frames_skip_steps_input = "1: (85), 50: (65), 100: (85)" #@param{type: 'string'}
    if frame > 0:
        if frame%4 == 0:
            frames_skip_steps_input += str(frame)+":(40),"
        elif frame%4 == 1:
            frames_skip_steps_input += str(frame)+":(60),"
        elif frame%4 == 3:
            frames_skip_steps_input += str(frame)+":(80),"

frames_skip_steps_input = frames_skip_steps_input[:-1]
frames_skip_steps = absolute_key_frame_multiplier(frames_skip_steps_input)

#EXTENDED AGING WITH WEIGHT MORPH---------------------------------

text_prompts = {}
creepy_weight = -10
ador_weight = 12
for i in range(180):
    if i > 160:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(i-160)+" year old haunted demon bones by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "creepy: "+str(creepy_weight),
        ]  
    if i > 130:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(i-130)+" year old tree skeleton hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "creepy: "+str(creepy_weight),
        ]      
    elif i > 30:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(i-30)+" year old tree person hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "creepy: "+str(creepy_weight),
            "adorable: "+str(ador_weight)
        ]
    elif i > 25:
        text_prompts[i] = [
            "Beautiful detailed portrait of a "+str(i-25)+" month old tree person hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
             "adorable: "+str(ador_weight)
        ]
    elif i > 20:
        text_prompts[i] = [
            "Beautiful detailed portrait of an adorable "+str(i-20)+" day old baby tree person hybrid by Nick Silva, Shin JeongHo, Wandah Kurniawan, Symmetrical composition with people centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "adorable: "+str(ador_weight),
            "color: 3"
        ]
    elif i > 10:
          text_prompts[i] = [
            "Beautiful detailed picture of a "+str(i-10)+" year old tree by Nick Silva, Shin JeongHo, Jim Burns, Symmetrical composition with tree centered, trending on artstation, colorized:12",
            "text:-6",
            "glasses:-3",
            "color: 3"
        ]
    else:
          text_prompts[i] = [
            "Beautiful detailed picture of a "+str(i)+" day old plant seedling by Nick Silva, Shin JeongHo, Jim Burns, Symmetrical composition with plant centered, trending on artstation, colorized:12",
            "text:-6",
            "color: 3"
        ]
    
    if i>30 and (i+5) % 10 == 0:
          creepy_weight+=1
    if i>20 and i % 10 == 0:
          ador_weight-=1

image_prompts = {
    # 0:['ImagePromptsWorkButArentVeryGood.png:2',],
}
