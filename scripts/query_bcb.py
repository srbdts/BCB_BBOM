import os, re

querydic = {
	"juridisch":
		{
			"FR": [r"[Ii]ndig[eè]nes?",r"[EeÉé]volu[ée]e?s?"],
			"NL":[r"[bB]oy'?s?",r"[Ii]nlanders?",r"[Ii]nboorling(en)?"]
		},
	"geografisch":
		{
			"FR": [r"[Cc]ongolaise?s?",r"[Aa]fricaine?s?"],
			"NL": [r"[CKck]ongole(sischen?|e?s(ch)?e?|zen|nses?)",r"[Aa]frika(an(s(ch)?e?n?)?|an(ers?)?|nd?e(n|rs?))"]
		},
	"ontmenselijkend":
		{
			"FR": [r"[Ss]auvages?",r"[Cc]ivilis[ée]e?s?"],
			"NL": [r"[Ww]ild(ste|e?n?)?",r"[Ww]ilder?(man(nen)?|ling(en)?)",r"[Bb]eschaafde?"]
		},
	"biologisch":
		{
			"FR": [r"[Nn][èe]gres?",r"[Nn]oire?s?"],
			"NL": [r"[Nn]egers?",r"[Nn]egerin(nen)?",r"[Nn]eger(jongens?|bevolking|chef|dokters?|hoofd(en)?|koning|predikant|stijl|hut(ten)?|dorp|volk)",r"[Zz]wart(en?|jes?)?"]
		}
}


def get_context(tokens,index,window=50):
	left = tokens[max(0,index-window):index]
	hit = tokens[index]
	right = tokens[index+1:min(len(tokens),index+window+1)]
	return (" ".join(left),hit," ".join(right))

main_dir = "alle_bestanden"
volumes = [vol for vol in os.listdir(main_dir) if vol.startswith("vol")]

for category,queries_per_language in querydic.items():
	opf_category = open("hits_%s.txt"%category,"w",encoding="utf-8")
	opf_category.write("volume\ttaal\trecord\tquery\trelatieve_positie\tlinkercontext\thit\trechtercontext\n")
	for vol in volumes:
		for language,queries in queries_per_language.items():
			corpusdir = os.path.join(main_dir,vol,language)
			corpuslist = os.listdir(corpusdir)
			for f in corpuslist:
				ipf = open(os.path.join(corpusdir,f),"r",encoding="utf-8")
				text = ipf.read()
				words = text.split(" ")
				hits = []
				template = "%s\t%s\t%s"%(vol,language,f)
				for i,word in enumerate(words):
					for query in queries:
						if re.match(query,word):
							hits.append((i,query))
				for (tokenpos,query) in hits:
					(left,hit,right) = get_context(words,tokenpos)
					rel_pos = 100*tokenpos/len(words)
					row = "%s\t%s\t%s\t%s\t%s\t%s\n"% (template,query,rel_pos,left,hit,right)
					opf_category.write(row)
	opf_category.close()




