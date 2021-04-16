from Wappalyzer import Wappalyzer, WebPage

with open('/mnt/c/Users/demo/Desktop/wappalyzer_python/python-Wappalyzer/url.txt', 'r') as f:
	#data = f.read()
	#print (data)
	#for line in f:
	#lines = f.readlines()
	#i = 1
	for line in f:
		
		l=line.strip()
		webpage = WebPage.new_from_url(l)
		wappalyzer = Wappalyzer.latest()
		output = wappalyzer.analyze_with_versions_and_categories(webpage)
		print(output)


