# get cypher rep
cy_rep = 'ilikekillingpeoplebecauseitissomuchfunitismorefunthankillingwildgameintheforrestbecsusemanisthemoatdangertueanimaloealltokillsomethinggivesmethemoatthrillingefperenceitisevenbetterthangettingyourrocksoffwithagirlthebestpartofitiathaewhenidieiwillbereborninparadicesndalloheihavekilledwillbecomemyslavesiwillnotgiveyoumynamebecauseyouwilltrytosloidownorstopmycollectingofslavesformyafterlifeebeorietemethhputi'
cy_rep = 'reettotheingtothiitretherethergtnoetjrhrertttotherintthtohghfterretheshrehtintheredinthethoehgieihthethtrtortheretheetntthinthereiherhtsirhrhrrehherthedtheoehrtirethrhetherenthenehethohtehrroeingtothereeheesnthrintherttheothitnththerhthrrteeggjdseetherthrnrefeettettenhotherorttherrhotenotrroteetreenrontotnhiitrhheeheeghertheritinerehhnttr'
my_rep = '--------------th---l-------------------l--t-------e------t-----ll--h---l--------l-----t------------h----l----h---t------the----l----l------l-l--h-------------l-el---------l---------------h----e-------l---------l--------t--t-----h-------ll----------------l---------------th---l--h--l-------ll-------------------------------------------t----l'
sim = ''

for x in range(len(cy_rep)):
	if cy_rep[x:x+1] == my_rep[x:x+1]:
		sim += cy_rep[x:x+1]
	else:
		sim += '-'
print(sim)
input()
