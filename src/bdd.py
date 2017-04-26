"""
La base de données des réponses

La clef du dictionnaire est une expression régulière
La valeur est une liste des actions dispos (dit_blabla, joue_fichier etc...)
"""

data = {
	"*(coucou|bonjour|salut)*": ["dit_salut", "dit_bonjour", "dit_coucou"]
	}
	
data = {
	"*(ça va|comment ça va|comment vas tu|comment tu vas)*":  ["dit_ça va bien et toi", "dit_ca va merci et toi"]
	}
	
data = {
	"*(que fais tu|tu fais quoi)*": ["dit_je réflechis au sens de la vie et toi", "dit_je pense au sens de la vie, ca marrive de temps en temps, pas toi", "dit_rien, je mennuie"]
	}
	
data = {
	"*(tu es occupé|es tu occupé)*": ["dit_non je ne fais rien et toi"]
	}
data = {
	"*(raconte moi une blague|dis moi une blague|raconte moi une histoire drole|tu connais une histoire drole)*": ["dit_que dis un papier qui tombe dans leau, je nai pas pieds","cest lhistoire dun x carré qui rentre dans une foret et qui en ressort en x, que sest il passé, il sest pris une racine"]
	}
	
default = ["dit_42", "dit_heu... je ne comprends pas"]
