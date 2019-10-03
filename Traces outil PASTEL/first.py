import pe
import bonobo

def extract():
	with open('cleaned_events.csv') as f:
		buffer = []
		for line in f:
			line = line.strip()
			#if line.startswitch
			buffer.append(line)


def transform(ep):
	match = re.match('^(.*) (.*)$',ep[1])
	date = match.group(1).strip(' ')
	heure = match.group(2)

	return{
		'id': ep[0],
		'timeStamp': ep[1],
		'UserId' : ep[5],
		'Action' : ep[6],
	}

def arg0_to_kwargs(row):
	return bonobo.Bag(**row)



graph = bonobo.Graph(
	extract,
	transform,
	bonobo.PrettyPrinter()
	)