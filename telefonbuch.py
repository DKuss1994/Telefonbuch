import os
import json
#telefonbuch
print("Das hier ist ein Telefonbuch was Namen und Nummern speichert. Viel Spaß.")

class Telefonbuch:
  def __init__(self):
    self.telefonbuch = {}
    # Eine Liste mit Begriefen für Nein, falls der User was anderes eingibt als nein
    self.nein = [wort.lower() for wort in """Nein
Nee
      Ne
      Nö
      Nööp
      Nope
      Naa
      Nä
      Nääh
      Nix da
      Keinesfalls
      Auf keinen Fall
      Vergiss es
      Kommt nicht in Frage
      Never
      No
      Non
      Neinpein
      Nada
      Nyet
      Neva
      Not
      Njet
      Null
      Ohne mich
      N""".splitlines() if wort.strip()]
    # Eine Liste mit Begriefen für Ja, falls der User was anderes eingibt als ja
    self.ja = [wort.lower() for wort in"""J
Ja
Jawohl
Jau
Jep
Jo
Jop
Jupp
Yup
Yep
Yo
Okay
Oke
Oki
Sicher
Klar
Genau
Richtig
Jaa
Jaja
Alles klar
Läuft
Passt
Safe
True
Word
Yes
Yeah
Yessir
Oui
Si
Da
Hai
Ye
Aye
Ouais
Jawel
""".splitlines() if wort.strip()]
  # Einfach Json speicherung des Telefonbuches
  def speichern (self):
    speichern = {"Telefonbuch": self.telefonbuch,}
    with open ("speichern.json", "w") as file:
      json.dump(speichern, file, indent=2)
      print("Telefonbuch wurde erfolgreich gespeichert!")
  # Hier wird die Jsondatei geladen.
  def laden (self):
    if os.path.exists("speichern.json"):
      tuen = self.eingabe("Möchtest du den Spielstand laden? (ja/nein) ",str).strip().lower()
      if tuen in self.ja:
        with open ("speichern.json", "r") as file:
          daten = json.load(file)
          self.telefonbuch = daten["Telefonbuch"]
          print("Telefonbuch wurd erfolgreich geladen")
          self.buch()
      elif tuen in self.nein:
        print ("Neues Telefonbuch wird erstellt")
    else:
      print("Kein Speicherstand gefunden. Es wird ein neues Telefonbuch erstellt.")
  # Hier ist eine Allgemeine Inputabfrage für den User. Die wir immer wieder verwenden können um den Code Robuster zu machen
  def eingabe (self, Frage:str, typ):

    while True:
      try:
        eingabe = input(Frage)
        if eingabe == "":
          print("Du hast nichts eingegeben. Bitte gib was an.")
          continue
        elif typ == int:
          return int(eingabe)
        elif typ == str:
          return str(eingabe)
        elif typ == float:
          return float(eingabe)
        else:
          pass
        
      except ValueError:
        print(f"Du hast eine Falsche Eingabe gemacht. Deine Eingabe: {eingabe} ist kein {typ.__name__}")
        continue
  # Hier wird die Rufnummer in schön Formatiert.
  def nummer_formatieren(self, nummer):
    nummer_str = str(nummer)
    if len(nummer_str) >= 6:
      
      nummer_mit = " ".join(nummer_str[i:i+2] for i in range (0,len(nummer_str),2))
      nummer = nummer_mit[0:7]+ " - " + nummer_mit[7:]
      return nummer

    else:
      nummer = " ".join(nummer_str[i:i+2] for i in range (0,len(nummer_str),2))
      return nummer
  #Hier wird das Telefonbuch angezeigt
  def buch(self):
    print("Einmal das komplette Telefonbuch.")
    print(self.telefonbuch)
    print("Einmal nur die Namen im Telefonbuch")
    print(self.telefonbuch.keys())   
  # Hier kann man nach einer bestimmten Person suchen
  def anzeigen(self):
    name = self.eingabe("Wenn suchst du ? ",str)
    if name in self.telefonbuch:
      print(f"{name}s Telefonnummer ist {self.telefonbuch[name]}")
    else:
      print(f"Der {name} ist nicht im Telefonbuch.")
      hinzufügen = self.eingabe(f"Möchtest du {name} dem Telefonbuch hinzufügen? (ja/nein)",str).strip().lower()
      if hinzufügen in self.ja:
        nummer = self.eingabe(f"Welche Rufnummer hat {name} ? ",int)
        nummer = self.nummer_formatieren(nummer)
        self.telefonbuch[name] = nummer
        print(f"Die Nummer: {nummer} von {name} wurde hinzugefügt")
      elif hinzufügen in self.nein:
        print(f"{name} wird nicht hinzugefügt!")
      else: 
        print ("Es ist ein Fehler passiert")
        
  # Hier wird Name und Rufnummer hinzugefügt
  def hinzufügen (self):
    hinzufügen = self. eingabe("Welchen Namen möchtest du hinzufügen? ",str)
    nummer = self.eingabe("Welche Nummer möchtest du hinzufügen? ",int)
    nummer = self.nummer_formatieren(nummer)
    # Falls es den Namen schon gibt wird gefragt ob man überschreiben will
    if hinzufügen in self.telefonbuch:
      weiter_machen = self.eingabe(f"{hinzufügen} ist schon vorhanden willst du es überschreiben? (ja) ",str).strip().lower()
      if weiter_machen in self.ja:
        self.telefonbuch[hinzufügen] = nummer
        print (f"{hinzufügen}´s Nummer {self.telefonbuch[hinzufügen]} wurde hinzugefügt. ")
      else:
        print(hinzufügen, "wurde nicht überschrieben.")      
    else:
        self.telefonbuch[hinzufügen] = nummer
        print (f"{hinzufügen}´s Nummer {self.telefonbuch[hinzufügen]} wurde hinzugefügt. ")
  # Hier wird der Kontakt gelöscht werden.
  def entfernen (self):
    while True:
      name = self.eingabe("Welchen Namen willst du mit Nummer Entfernen? ",str)
      if name in self.telefonbuch:
        wirklich = self.eingabe(f"Willst du {name} wirklich löschen? (j/n)").strip().lower()
        if wirklich in self.ja:
          self.telefonbuch.pop(name)
          print(f"{name} wurde erfolgreich gelöscht!")
          break
        elif wirklich in self.nein:
          print(f"{name} wird nicht gelöscht.")
          break
        else:
          print("Bitte eine richtige Eingabe machen")
          continue
      else:
        print(f"{name} ist nicht in der Liste.")
        continue
  # Hier wird das Programm beendet und es wird noch einmal gefragt ob man noch Speichern möchte
  def beenden(self):
    tuen = self.eingabe("Möchtest du dein Telefonbuch speichern (ja/nein) ",str).strip().lower()
    if tuen in self.ja:
      self.speichern()
      print("Telefonbuch wurde gespeichert!")
      tuen = self.eingabe("Möchtest du das Programm beenden? (ja/nein) ").strip().lower()
      if tuen in self.ja:
        print("Programm wurde beendet!")
        return False
      elif tuen in self.nein:
        print("Prgroamm wird nicht beendet")
        return True
    elif tuen in self.nein:
      print("Telefonbuch wird nicht gespeichert!")
      tuen = self.eingabe("Möchtest du das Programm beenden? (ja/nein) ").strip().lower()
      if tuen in self.ja:
        return False
      elif tuen in self.nein:
        print("Prgroamm wird nicht beendet")
        return True
    
  # Das hier ist das Hauptprogramm.
  def start(self):
    while True:
      Machen = self.eingabe("Was möchtest du machen(hinzufügen/entfernen/anzeigen/Telefonbuch/beenden/speichern ",str).strip().lower()
          # Hier wird die gesuchte Namens Nummer angezeigt.
      if Machen=="anzeigen":
        self.anzeigen()
      # Hier wird Name und Nummer hinzugefügt.
      elif Machen == "hinzufügen":
        self.hinzufügen()
    # Hier wird das ganze Telefonbuch angezeigt.
      elif Machen == "telefonbuch":
        self.buch()
      elif Machen == "entfernen":
        self.entfernen()
      elif Machen == "speichern":
        self.speichern()
      elif Machen == "beenden":
        x = self.beenden()
        if x == False:
          break
        elif x == True:
          continue
        
      else:
        print(f"Deine Angabe {Machen} war falsch. Versuch es gleich nochmal.")
        print ("Gib hinzufügen ein um ein Namen und die Nummer hinzufügen.")
        print ("Gib Telefonbuch ein um das komplette Telefonbuch anzuzeigen")
        print ("Gib entfernen ein um ein Namen und die Nummer zu entfernen.")
        print ("Gib beenden ein um das Programm zu beenden.")

telefonbuch = Telefonbuch()
telefonbuch.laden()
telefonbuch.start()


    
  


    
  
